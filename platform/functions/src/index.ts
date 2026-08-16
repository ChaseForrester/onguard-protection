/**
 * OnGuard Guard Platform — Cloud Functions
 * OG-LEG-2026-001 · NSW Class 1 only · Master Licence 000110094
 */
import * as admin from "firebase-admin";
import { beforeUserCreated, beforeUserSignedIn } from "firebase-functions/v2/identity";
import { onDocumentCreated, onDocumentWritten } from "firebase-functions/v2/firestore";
import { HttpsError, onCall } from "firebase-functions/v2/https";
import { CLASS1_CODES, dogWorkLegal, rosterAllows, type Activity, type Class1Code } from "../../src/licence";

admin.initializeApp();
const db = admin.firestore();
const auth = admin.auth();

const LEGAL_PACK = "OG-LEG-2026-001";
const MASTER_LICENCE = "000110094";
const PHASE2_THRESHOLD = 10;
const SUPER_EMAILS = new Set([
    "hello@techaidaustralia.com.au",
    "admin@ogprotection.com.au",
]);

type AccessState =
    | "unverified"
    | "kyc_required"
    | "kyc_pending"
    | "verified"
    | "rejected"
    | "blocked";

async function setClaims(uid: string, input: {
    accessState: AccessState;
    role: "applicant" | "guard" | "superadmin";
    verified: boolean;
    subclasses?: Class1Code[];
}): Promise<void> {
    const user = await auth.getUser(uid);
    const existing = user.customClaims || {};
    const superadmin = existing.superadmin === true;
    await auth.setCustomUserClaims(uid, {
        ...existing,
        superadmin,
        role: superadmin ? "superadmin" : input.role,
        verified: superadmin ? true : input.verified,
        accessState: superadmin ? "verified" : input.accessState,
        jurisdiction: "NSW",
        legalPack: LEGAL_PACK,
        masterLicence: MASTER_LICENCE,
        subclasses: input.subclasses || [],
        claimsVersion: Date.now(),
    });
}

async function forceLogout(uid: string, reason: string): Promise<void> {
    await auth.revokeRefreshTokens(uid);
    await db.collection("users").doc(uid).set(
        { accessState: "blocked", rejectedReason: reason, updatedAt: admin.firestore.FieldValue.serverTimestamp() },
        { merge: true },
    );
}

async function userDoc(uid: string) {
    const snap = await db.collection("users").doc(uid).get();
    return snap.exists ? snap.data() : null;
}

async function ensureApplicantDoc(event: { data?: { uid?: string; email?: string; phoneNumber?: string; displayName?: string } }) {
    const uid = event.data?.uid;
    if (!uid) throw new HttpsError("invalid-argument", "Missing user id.");
    await db.collection("users").doc(uid).set({
        uid,
        role: "applicant",
        accessState: "kyc_required",
        email: event.data?.email || null,
        phone: event.data?.phoneNumber || null,
        displayName: event.data?.displayName || null,
        jurisdiction: "NSW",
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        lastAuthAt: admin.firestore.FieldValue.serverTimestamp(),
        verifiedAt: null,
        verifiedByUid: null,
        rejectedReason: null,
        claimsVersion: Date.now(),
    }, { merge: true });
    return uid;
}

/** Blocking: every new account starts as kyc_required, NSW only, never verified. */
export const beforeCreate = beforeUserCreated({ region: "us-east1" }, async (event) => {
    await ensureApplicantDoc(event);
    const email = (event.data?.email || "").toLowerCase();
    if (SUPER_EMAILS.has(email)) {
        return {
            customClaims: {
                role: "superadmin",
                verified: true,
                accessState: "verified",
                jurisdiction: "NSW",
                superadmin: true,
                legalPack: LEGAL_PACK,
                subclasses: [],
            },
        };
    }
    return {
        customClaims: {
            role: "applicant",
            verified: false,
            accessState: "kyc_required",
            jurisdiction: "NSW",
            superadmin: false,
            legalPack: LEGAL_PACK,
            subclasses: [],
        },
    };
});

/**
 * Blocking sign-in.
 * rejected/blocked → deny.
 * verified / kyc_required / kyc_pending / superadmin → allow (client route-gates).
 * Anyone else → deny (force-logout equivalent at the identity layer).
 */
export const beforeSignIn = beforeUserSignedIn({ region: "us-east1" }, async (event) => {
    const user = event.data;
    if (!user?.uid) throw new HttpsError("invalid-argument", "Missing user.");
    const uid = user.uid;
    const email = (user.email || "").toLowerCase();
    let doc = await userDoc(uid);
    const claims = user.customClaims || {};
    if (claims.superadmin === true || SUPER_EMAILS.has(email)) {
        return { sessionClaims: { ...claims, superadmin: true, verified: true, accessState: "verified", role: "superadmin" } };
    }
    if (!doc) {
        await ensureApplicantDoc(event);
        doc = await userDoc(uid);
    }
    const state: AccessState = (doc?.accessState as AccessState) || "kyc_required";
    if (state === "rejected" || state === "blocked") {
        throw new HttpsError("permission-denied", "Access restricted to verified NSW Class 1 operatives (OG-LEG-2026-001).");
    }
    const accessState: AccessState =
        state === "verified" || state === "kyc_pending" || state === "kyc_required"
            ? state
            : "kyc_required";
    await db.collection("users").doc(uid).set(
        { lastAuthAt: admin.firestore.FieldValue.serverTimestamp(), accessState },
        { merge: true },
    );
    return {
        sessionClaims: {
            role: accessState === "verified" ? "guard" : "applicant",
            verified: accessState === "verified",
            accessState,
            jurisdiction: "NSW",
            legalPack: LEGAL_PACK,
        },
    };
});

/** Safety net if blocking functions are skipped (emulator / existing users). */
export const assertAccess = onCall(async (request) => {
    if (!request.auth) throw new HttpsError("unauthenticated", "Sign in required.");
    const uid = request.auth.uid;
    const doc = await userDoc(uid);
    if (request.auth.token.superadmin === true) {
        return { ok: true, accessState: "verified", role: "superadmin" };
    }
    const state = (doc?.accessState as AccessState) || "unverified";
    if (state === "rejected" || state === "blocked" || state === "unverified") {
        await forceLogout(uid, "Non-verified or rejected NSW Class 1 access");
        throw new HttpsError("permission-denied", "Logged out: not a verified NSW Class 1 operative.");
    }
    return { ok: true, accessState: state, role: doc?.role || "applicant" };
});

export const submitKyc = onCall(async (request) => {
    if (!request.auth) throw new HttpsError("unauthenticated", "Sign in required.");
    const uid = request.auth.uid;
    const d = request.data || {};
    const subclasses = (d.subclasses || []) as Class1Code[];
    if (!subclasses.length || subclasses.some((c) => !CLASS1_CODES.includes(c))) {
        throw new HttpsError("invalid-argument", "Select one or more current Class 1 subclasses (Schedule D).");
    }
    if (!d.licenceNumber || !d.licenceExpiry) {
        throw new HttpsError("invalid-argument", "Licence number and expiry are required.");
    }
    if (!d.licenceFrontPath || !d.licenceBackPath) {
        throw new HttpsError("invalid-argument", "Front and back of the physical NSW licence are required.");
    }
    if (!d.mobile || !d.email) {
        throw new HttpsError("invalid-argument", "Mobile and email are required.");
    }
    const bsb = String(d.bsb || "").replace(/\s/g, "");
    const accountNumber = String(d.accountNumber || "").replace(/\s/g, "");
    if (!/^\d{6}$/.test(bsb) || accountNumber.length < 4) {
        throw new HttpsError("invalid-argument", "BSB must be 6 digits. Account number is required.");
    }
    const superannuation = d.usi
        ? { kind: "usi" as const, usi: String(d.usi) }
        : d.fundName
            ? { kind: "fund" as const, fundName: String(d.fundName), usi: d.fundUsi || null }
            : null;
    if (!superannuation) {
        throw new HttpsError("invalid-argument", "Provide a USI or a superannuation fund name.");
    }

    await db.collection("kyc").doc(uid).set({
        uid,
        jurisdiction: "NSW",
        legalPack: LEGAL_PACK,
        licenceNumber: String(d.licenceNumber).toUpperCase(),
        licenceExpiry: d.licenceExpiry,
        subclasses,
        licenceFrontPath: d.licenceFrontPath,
        licenceBackPath: d.licenceBackPath,
        mobile: d.mobile,
        email: d.email,
        bank: {
            bsb,
            accountNumber,
            accountName: d.accountName || "",
        },
        superannuation,
        firstAidExpiry: d.firstAidExpiry || null,
        submittedAt: admin.firestore.FieldValue.serverTimestamp(),
        reviewedAt: null,
        reviewedByUid: null,
        reviewNotes: null,
    });
    await db.collection("users").doc(uid).set(
        {
            accessState: "kyc_pending",
            role: "applicant",
            email: d.email,
            phone: d.mobile,
            updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        },
        { merge: true },
    );
    await setClaims(uid, { accessState: "kyc_pending", role: "applicant", verified: false, subclasses });
    return { ok: true, accessState: "kyc_pending" };
});

export const reviewKyc = onCall(async (request) => {
    if (!request.auth?.token.superadmin) {
        throw new HttpsError("permission-denied", "Super admin only.");
    }
    const targetUid = String(request.data?.uid || "");
    const decision = request.data?.decision as "verified" | "rejected";
    if (!targetUid || !["verified", "rejected"].includes(decision)) {
        throw new HttpsError("invalid-argument", "uid and decision required.");
    }
    const kyc = await db.collection("kyc").doc(targetUid).get();
    if (!kyc.exists) throw new HttpsError("not-found", "No KYC on file.");
    const subclasses = (kyc.get("subclasses") || []) as Class1Code[];

    if (decision === "rejected") {
        await db.collection("users").doc(targetUid).set({
            accessState: "rejected",
            role: "applicant",
            rejectedReason: request.data?.reason || "KYC rejected",
            updatedAt: admin.firestore.FieldValue.serverTimestamp(),
        }, { merge: true });
        await setClaims(targetUid, { accessState: "rejected", role: "applicant", verified: false });
        await forceLogout(targetUid, request.data?.reason || "KYC rejected");
        return { ok: true, accessState: "rejected" };
    }

    await db.collection("users").doc(targetUid).set({
        accessState: "verified",
        role: "guard",
        verifiedAt: admin.firestore.FieldValue.serverTimestamp(),
        verifiedByUid: request.auth.uid,
        rejectedReason: null,
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });
    await db.collection("kyc").doc(targetUid).set({
        reviewedAt: admin.firestore.FieldValue.serverTimestamp(),
        reviewedByUid: request.auth.uid,
        reviewNotes: request.data?.notes || null,
    }, { merge: true });
    await setClaims(targetUid, {
        accessState: "verified",
        role: "guard",
        verified: true,
        subclasses,
    });
    return { ok: true, accessState: "verified" };
});

export const assignJob = onCall(async (request) => {
    if (!request.auth?.token.superadmin) {
        throw new HttpsError("permission-denied", "Super admin only.");
    }
    const jobId = String(request.data?.jobId || "");
    const guardUid = String(request.data?.guardUid || "");
    const jobRef = db.collection("jobs").doc(jobId);
    const jobSnap = await jobRef.get();
    if (!jobSnap.exists) throw new HttpsError("not-found", "Job not found.");
    if (jobSnap.get("jurisdiction") !== "NSW") {
        throw new HttpsError("failed-precondition", "NSW only (OG-LEG-2026-001).");
    }
    const userSnap = await db.collection("users").doc(guardUid).get();
    if (!userSnap.exists || userSnap.get("accessState") !== "verified") {
        throw new HttpsError("failed-precondition", "Guard is not verified.");
    }
    const kycSnap = await db.collection("kyc").doc(guardUid).get();
    const held = (kycSnap.get("subclasses") || []) as Class1Code[];
    const required = (jobSnap.get("requiredActivities") || []) as Activity[];
    if (jobSnap.get("requiresDog") && !dogWorkLegal(held)) {
        throw new HttpsError("failed-precondition", "Roster rule: dog work requires 1D. 1A/1B/1C/1E/1F cannot do dog work.");
    }
    if (jobSnap.get("requiresArmed") && !held.includes("1F")) {
        throw new HttpsError("failed-precondition", "Roster rule: armed work requires 1F.");
    }
    if (required.includes("cash_in_transit") && !held.includes("1C")) {
        throw new HttpsError("failed-precondition", "Roster rule: CIT requires current 1C. A 1A is not a cash escort.");
    }
    if (required.includes("bodyguard") && !held.includes("1B")) {
        throw new HttpsError("failed-precondition", "Roster rule: bodyguard work requires 1B.");
    }
    if (!rosterAllows(held, required)) {
        throw new HttpsError("failed-precondition", "Roster rule failed: subclass does not match the activity (Schedule D).");
    }
    if (jobSnap.get("requiresFirstAid")) {
        const fa = kycSnap.get("firstAidExpiry");
        if (!fa || new Date(fa) < new Date()) {
            throw new HttpsError("failed-precondition", "1A crowd/event post requires current first aid (typically HLTAID011).");
        }
    }

    await jobRef.set({
        status: "assigned",
        assignedUid: guardUid,
        assignedSubclasses: held,
        assignedLicenceNumber: kycSnap.get("licenceNumber") || null,
        rosterRuleCheckedAt: admin.firestore.FieldValue.serverTimestamp(),
        rosterRulePassed: true,
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });

    await db.collection("notifications").add({
        uid: guardUid,
        title: "New job assigned",
        body: `${jobSnap.get("suburb")} · ${jobSnap.get("brief") || "See job details"}`,
        jobId,
        read: false,
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
    });

    const tokens = await db.collection("fcmTokens").where("uid", "==", guardUid).get();
    const list = tokens.docs.map((t) => t.get("token")).filter(Boolean);
    if (list.length) {
        await admin.messaging().sendEachForMulticast({
            tokens: list,
            notification: { title: "New job assigned", body: String(jobSnap.get("suburb") || "OnGuard") },
            data: { jobId },
        });
    }
    return { ok: true, assignedUid: guardUid, subclasses: held };
});

export const onVerifiedCount = onDocumentWritten("users/{uid}", async (event) => {
    const after = event.data?.after?.data();
    const before = event.data?.before?.data();
    const became = after?.accessState === "verified" && before?.accessState !== "verified";
    const left = before?.accessState === "verified" && after?.accessState !== "verified";
    if (!became && !left) return;
    const snap = await db.collection("users").where("accessState", "==", "verified").count().get();
    const count = snap.data().count;
    await db.collection("platformConfig").doc("live").set({
        verifiedGuardCount: count,
        phase2Enabled: count >= PHASE2_THRESHOLD,
        phase2Threshold: PHASE2_THRESHOLD,
        jurisdiction: "NSW",
        masterLicence: MASTER_LICENCE,
        legalPack: LEGAL_PACK,
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });
});

export const onNotificationCreated = onDocumentCreated("notifications/{id}", async () => {
    return;
});
