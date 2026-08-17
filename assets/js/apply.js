import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, doc, setDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getStorage, ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-storage.js";
import { firebaseConfig } from "./firebase-app.js";

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const storage = getStorage(app);
const STAFF_MAIL = "admin@ogprotection.com.au";
const STAFF_CC = "hello@techaidaustralia.com.au";
const STAFF_INBOXES = [STAFF_MAIL, STAFF_CC];

const form = document.getElementById("apply-form");
if (!form) throw new Error("apply form missing");

const steps = [...form.querySelectorAll(".wizard-step")];
const dots = [...form.querySelectorAll("[data-step-dot]")];
const errorBox = document.getElementById("form-error");
const review = document.getElementById("apply-review");
const submitBtn = document.getElementById("apply-submit");
let current = 1;

const params = new URLSearchParams(window.location.search);
const prefillRole = (params.get("role") || "").toUpperCase();
if (prefillRole) {
    const role = form.elements.role;
    if (role && [...role.options].some((opt) => opt.value === prefillRole)) {
        role.value = prefillRole;
    }
    const box = form.querySelector(`input[name="subclass"][value="${prefillRole}"]`);
    if (box) box.checked = true;
}

function subclasses() {
    return [...form.querySelectorAll('input[name="subclass"]:checked')].map((el) => el.value);
}

function showError(message) {
    if (!errorBox) return;
    errorBox.hidden = !message;
    errorBox.textContent = message || "";
}

function showStep(n) {
    current = n;
    steps.forEach((step) => {
        const active = Number(step.dataset.step) === n;
        step.hidden = !active;
        step.classList.toggle("is-active", active);
    });
    dots.forEach((dot) => {
        const value = Number(dot.dataset.stepDot);
        dot.classList.toggle("is-active", value === n);
        dot.classList.toggle("is-done", value < n);
    });
    if (n === 4) updateReview();
    showError("");
    form.scrollIntoView({ behavior: "smooth", block: "start" });
}

function fileOk(file, label) {
    if (!file) return `Add the ${label}.`;
    if (file.size > 8 * 1024 * 1024) return `${label} must be under 8MB.`;
    if (!/^image\/(jpeg|png|webp)$/.test(file.type)) return `${label} must be a JPG, PNG or WebP.`;
    return "";
}

function validate(n) {
    if (n === 1) {
        if (!(form.elements.role.value || "").trim()) return "Pick the role you want.";
        if (!subclasses().length) return "Tick at least one NSW Class 1 subclass.";
    }
    if (n === 2) {
        if (!(form.elements.licenceNumber.value || "").trim()) return "Enter your licence number.";
        if (!form.elements.licenceExpiry.value) return "Enter the licence expiry.";
        return fileOk(form.elements.licenceFront.files[0], "licence front")
            || fileOk(form.elements.licenceBack.files[0], "licence back");
    }
    if (n === 3) {
        if (!(form.elements.fullName.value || "").trim()) return "We need your name.";
        if (!(form.elements.mobile.value || "").trim()) return "We need a mobile number.";
        const email = (form.elements.email.value || "").trim();
        if (!email) return "We need an email.";
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return "That email does not look right.";
        if (!(form.elements.suburb.value || "").trim()) return "Enter your home suburb.";
        if (!form.elements.availability.value) return "Tell us your availability.";
    }
    if (n === 4) {
        if (!(form.elements.accountName.value || "").trim()) return "Enter the bank account name.";
        if (!/^\d{6}$/.test((form.elements.bsb.value || "").replace(/\s/g, ""))) return "BSB must be 6 digits.";
        if (!(form.elements.accountNumber.value || "").trim()) return "Enter the account number.";
        if (!(form.elements.superUsi.value || "").trim()) return "Enter a Super USI or fund name.";
    }
    return "";
}

function updateReview() {
    if (!review) return;
    review.innerHTML = `
    <div><strong>${form.elements.fullName.value || "—"}</strong> · ${form.elements.email.value || ""} · ${form.elements.mobile.value || ""}</div>
    <div>Role <strong>${form.elements.role.value || "—"}</strong> · Subclasses <strong>${subclasses().join(", ") || "—"}</strong></div>
    <div>Licence <strong>${form.elements.licenceNumber.value || "—"}</strong> exp ${form.elements.licenceExpiry.value || "—"}</div>
    <div>${form.elements.suburb.value || ""} · ${form.elements.availability.value || ""}</div>
  `;
}

form.querySelectorAll(".wizard-next").forEach((btn) => {
    btn.addEventListener("click", () => {
        const message = validate(current);
        if (message) {
            showError(message);
            return;
        }
        showStep(Math.min(4, current + 1));
    });
});

form.querySelectorAll(".wizard-back").forEach((btn) => {
    btn.addEventListener("click", () => showStep(Math.max(1, current - 1)));
});

dots.forEach((dot) => {
    dot.addEventListener("click", () => {
        const target = Number(dot.dataset.stepDot);
        if (target < current) showStep(target);
    });
});

async function uploadLicence(appId, file, name) {
    const ext = (file.name.split(".").pop() || "jpg").toLowerCase();
    const path = `applications/${appId}/${name}.${ext}`;
    const snap = await uploadBytes(ref(storage, path), file, { contentType: file.type });
    return getDownloadURL(snap.ref);
}

async function postFormSubmit(to, payload, front, back) {
    const body = new FormData();
    body.append("_subject", `OnGuard Protection — job application — ${payload.fullName || "applicant"} (${payload.role || "role"})`);
    body.append("_template", "table");
    body.append("_captcha", "false");
    body.append("_replyto", payload.email || "");
    Object.entries(payload).forEach(([key, value]) => {
        if (value == null || value === "") return;
        body.append(key, String(value));
    });
    if (front) body.append("licenceFront", front, front.name);
    if (back) body.append("licenceBack", back, back.name);
    const res = await fetch(`https://formsubmit.co/ajax/${to}`, {
        method: "POST",
        body,
        headers: { Accept: "application/json" }
    });
    if (!res.ok) throw new Error(`Email delivery failed for ${to}`);
    return res;
}

async function emailAdmin(payload, front, back) {
    const results = await Promise.allSettled(
        STAFF_INBOXES.map((inbox) => postFormSubmit(inbox, payload, front, back))
    );
    if (!results.some((result) => result.status === "fulfilled")) {
        throw new Error("Email delivery failed");
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if ((form.elements._honey.value || "").trim()) return;
    const message = validate(4);
    if (message) {
        showError(message);
        return;
    }

    const front = form.elements.licenceFront.files[0];
    const back = form.elements.licenceBack.files[0];
    const appId = crypto.randomUUID();
    const payload = {
        id: appId,
        source: "public_form",
        status: "pending",
        jurisdiction: "NSW",
        role: form.elements.role.value,
        subclasses: subclasses(),
        fullName: form.elements.fullName.value.trim(),
        email: form.elements.email.value.trim(),
        mobile: form.elements.mobile.value.trim(),
        suburb: form.elements.suburb.value.trim(),
        availability: form.elements.availability.value,
        notes: (form.elements.notes.value || "").trim(),
        licenceNumber: form.elements.licenceNumber.value.trim().toUpperCase(),
        licenceExpiry: form.elements.licenceExpiry.value,
        firstAidExpiry: form.elements.firstAidExpiry.value || null,
        accountName: form.elements.accountName.value.trim(),
        bsb: form.elements.bsb.value.replace(/\s/g, ""),
        accountNumber: form.elements.accountNumber.value.replace(/\s/g, ""),
        superUsi: form.elements.superUsi.value.trim()
    };

    submitBtn.disabled = true;
    submitBtn.textContent = "Sending application…";
    showError("");

    let emailed = false;
    let stored = false;

    try {
        await emailAdmin({
            ...payload,
            subclasses: payload.subclasses.join(", ")
        }, front, back);
        emailed = true;
    } catch {
        emailed = false;
    }

    try {
        const [frontUrl, backUrl] = await Promise.all([
            uploadLicence(appId, front, "licence-front"),
            uploadLicence(appId, back, "licence-back")
        ]);
        await setDoc(doc(db, "applications", appId), {
            ...payload,
            licenceFrontPath: frontUrl,
            licenceBackPath: backUrl,
            emailed,
            createdAt: serverTimestamp(),
            updatedAt: serverTimestamp(),
            reviewedAt: null,
            reviewedByUid: null,
            reviewNotes: null
        });
        stored = true;
    } catch {
        stored = false;
    }

    if (!stored && !emailed) {
        showError("The application did not send. Call 0432 893 343 or email admin@ogprotection.com.au.");
        submitBtn.disabled = false;
        submitBtn.textContent = "Send application";
        return;
    }

    window.location.assign("./thanks.html");
});

showStep(1);
