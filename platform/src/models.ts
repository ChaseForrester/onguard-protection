import type { Activity, Class1Code } from "./licence";

export type AccessState =
    | "unverified"
    | "kyc_required"
    | "kyc_pending"
    | "verified"
    | "rejected"
    | "blocked";

export type Role = "applicant" | "guard" | "superadmin";

export type Jurisdiction = "NSW";

export interface UserDoc {
    uid: string;
    role: Role;
    accessState: AccessState;
    email: string | null;
    phone: string | null;
    displayName: string | null;
    jurisdiction: Jurisdiction;
    createdAt: FirebaseFirestore.Timestamp;
    updatedAt: FirebaseFirestore.Timestamp;
    lastAuthAt: FirebaseFirestore.Timestamp;
    verifiedAt: FirebaseFirestore.Timestamp | null;
    verifiedByUid: string | null;
    rejectedReason: string | null;
    /** Custom-claim mirror. Never trust the client to set this. */
    claimsVersion: number;
}

export interface KycDoc {
    uid: string;
    licenceNumber: string;
    licenceExpiry: string; // YYYY-MM-DD
    subclasses: Class1Code[];
    licenceFrontPath: string;
    licenceBackPath: string;
    mobile: string;
    email: string;
    bank: {
        bsb: string; // 6 digits
        accountNumber: string;
        accountName: string;
    };
    superannuation:
    | { kind: "usi"; usi: string }
    | { kind: "fund"; fundName: string; usi?: string };
    firstAidExpiry: string | null; // required before 1A crowd/event roster
    submittedAt: FirebaseFirestore.Timestamp;
    reviewedAt: FirebaseFirestore.Timestamp | null;
    reviewedByUid: string | null;
    reviewNotes: string | null;
}

export interface AvailabilityWeek {
    uid: string;
    weekStart: string; // Monday YYYY-MM-DD, Australia/Sydney
    days: {
        mon: TimeWindow[];
        tue: TimeWindow[];
        wed: TimeWindow[];
        thu: TimeWindow[];
        fri: TimeWindow[];
        sat: TimeWindow[];
        sun: TimeWindow[];
    };
    notes: string;
    updatedAt: FirebaseFirestore.Timestamp;
}

export interface TimeWindow {
    start: string; // HH:mm
    end: string;
}

export interface JobDoc {
    id: string;
    status: "draft" | "open" | "assigned" | "in_progress" | "completed" | "cancelled";
    jurisdiction: Jurisdiction;
    suburb: string;
    postcode: string;
    siteAddress: string | null;
    startAt: FirebaseFirestore.Timestamp;
    finishAt: FirebaseFirestore.Timestamp;
    requiredActivities: Activity[];
    requiredSubclassesHint: Class1Code[];
    requiresFirstAid: boolean;
    requiresDog: boolean;
    requiresArmed: boolean;
    clientName: string;
    clientPhone: string | null;
    brief: string;
    assignedUid: string | null;
    assignedSubclasses: Class1Code[] | null;
    assignedLicenceNumber: string | null;
    createdByUid: string;
    createdAt: FirebaseFirestore.Timestamp;
    updatedAt: FirebaseFirestore.Timestamp;
    rosterRuleCheckedAt: FirebaseFirestore.Timestamp | null;
    rosterRulePassed: boolean;
}

export interface NotificationDoc {
    uid: string;
    title: string;
    body: string;
    jobId: string | null;
    read: boolean;
    createdAt: FirebaseFirestore.Timestamp;
}

export interface PlatformConfig {
    phase2Enabled: boolean;
    verifiedGuardCount: number;
    phase2Threshold: 10;
    jurisdiction: Jurisdiction;
    masterLicence: "000110094";
    legalPack: "OG-LEG-2026-001";
}
