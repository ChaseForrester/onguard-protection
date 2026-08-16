import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import {
    getAuth,
    GoogleAuthProvider,
    signInWithPopup,
    signInWithEmailAndPassword,
    signInWithPhoneNumber,
    RecaptchaVerifier,
    onAuthStateChanged,
    signOut
} from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
import { firebaseConfig } from "./firebase-app.js";

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const mode = document.body.dataset.authMode || "guard";
const portalUrl = new URL("../platform/", window.location.href).href;

const errorBox = document.getElementById("auth-error");
const statusBox = document.getElementById("auth-status");
const googleBtn = document.getElementById("google-signin-btn");
const emailForm = document.getElementById("email-login-form");
const phoneBtn = document.getElementById("phone-signin-btn");
const smsModal = document.getElementById("sms-modal");
const smsInput = document.getElementById("sms-otp-code");
const smsConfirm = document.getElementById("sms-confirm-btn");
const smsCancel = document.getElementById("sms-cancel-btn");

let confirmationResult = null;
let recaptchaVerifier = null;
let routing = false;

function showError(message) {
    if (!errorBox) return;
    errorBox.hidden = !message;
    errorBox.textContent = message || "";
    if (statusBox) {
        statusBox.hidden = true;
        statusBox.textContent = "";
    }
}

function showStatus(message) {
    if (statusBox) {
        statusBox.hidden = !message;
        statusBox.textContent = message || "";
    }
    if (errorBox && message) {
        errorBox.hidden = true;
        errorBox.textContent = "";
    }
}

function friendlyAuthError(err) {
    const code = String(err?.code || "");
    const message = String(err?.message || "");
    if (code.includes("-47") || message.includes("-47") || message.includes("error-code:-47")) {
        return "Google sign-in hit a server block. Try again in a moment. If it repeats, use email or the apply form.";
    }
    if (code === "auth/popup-closed-by-user") return "Google sign-in was cancelled.";
    if (code === "auth/popup-blocked") return "Your browser blocked the Google popup. Allow popups and try again.";
    if (code === "auth/unauthorized-domain") return "This domain is not authorised in Firebase Auth yet.";
    if (code === "auth/operation-not-allowed") return "That sign-in method is not enabled yet in Firebase.";
    if (code === "auth/invalid-credential" || code === "auth/wrong-password" || code === "auth/user-not-found") {
        return "Email or password is not correct.";
    }
    if (code === "auth/too-many-requests") return "Too many attempts. Wait a moment and try again.";
    if (code === "auth/invalid-phone-number") return "Enter an Australian mobile, for example 0432 893 343.";
    if (code === "auth/missing-phone-number") return "Enter your mobile number first.";
    if (code === "auth/captcha-check-failed" || code === "auth/invalid-app-credential") {
        return "Phone verification could not start. Complete the reCAPTCHA and try again.";
    }
    if (code === "auth/quota-exceeded") return "SMS quota is exhausted. Use Google or email, or apply without signing in.";
    if (code === "auth/argument-error") return "Sign-in could not start. Refresh the page and try again.";
    return err?.message || "Sign-in failed.";
}

function toE164(raw) {
    const digits = String(raw || "").replace(/[^\d+]/g, "");
    if (digits.startsWith("+")) return digits;
    if (digits.startsWith("61") && digits.length >= 11) return `+${digits}`;
    if (digits.startsWith("0") && digits.length === 10) return `+61${digits.slice(1)}`;
    if (digits.length === 9) return `+61${digits}`;
    return digits;
}

async function routeSignedInUser(user) {
    if (routing) return;
    routing = true;
    try {
        const token = await user.getIdTokenResult(true);
        const email = (user.email || "").toLowerCase();
        const staffInbox = email === "hello@techaidaustralia.com.au" || email === "admin@ogprotection.com.au";
        const isSuper = token.claims.superadmin === true || staffInbox;
        if (mode === "super") {
            if (!isSuper) {
                await signOut(auth);
                showError("This account is not authorised for Super Admin access.");
                routing = false;
                return;
            }
            showStatus("Authorised. Opening the operations console…");
            window.location.replace(portalUrl);
            return;
        }
        showStatus("Signed in. Opening the guard portal…");
        window.location.replace(portalUrl);
    } catch (err) {
        showError(friendlyAuthError(err));
        routing = false;
    }
}

onAuthStateChanged(auth, (user) => {
    if (!user) return;
    routeSignedInUser(user);
});

googleBtn?.addEventListener("click", async () => {
    showError("");
    googleBtn.disabled = true;
    try {
        const provider = new GoogleAuthProvider();
        provider.setCustomParameters({ prompt: "select_account" });
        await signInWithPopup(auth, provider);
    } catch (err) {
        showError(friendlyAuthError(err));
    } finally {
        googleBtn.disabled = false;
    }
});

emailForm?.addEventListener("submit", async (event) => {
    event.preventDefault();
    showError("");
    const email = document.getElementById("login-email")?.value.trim();
    const password = document.getElementById("login-password")?.value;
    const submit = emailForm.querySelector('button[type="submit"]');
    if (submit) submit.disabled = true;
    try {
        await signInWithEmailAndPassword(auth, email, password);
    } catch (err) {
        showError(friendlyAuthError(err));
    } finally {
        if (submit) submit.disabled = false;
    }
});

const phonePanel = document.getElementById("phone-panel");
const phoneInput = document.getElementById("phone-number");
const phoneSend = document.getElementById("phone-send-btn");

phoneBtn?.addEventListener("click", () => {
    if (phonePanel) phonePanel.hidden = !phonePanel.hidden;
    if (phonePanel && !phonePanel.hidden) phoneInput?.focus();
});

async function ensureRecaptcha() {
    if (recaptchaVerifier) return recaptchaVerifier;
    const host = document.getElementById("recaptcha-visible") || document.getElementById("recaptcha-container");
    if (!host) throw new Error("reCAPTCHA container missing");
    recaptchaVerifier = new RecaptchaVerifier(auth, host, { size: "normal" });
    await recaptchaVerifier.render();
    return recaptchaVerifier;
}

phoneSend?.addEventListener("click", async () => {
    const phoneNumber = toE164(phoneInput?.value || "");
    if (!phoneNumber.startsWith("+61") || phoneNumber.length < 12) {
        showError("Enter an Australian mobile, for example 0432 893 343.");
        return;
    }
    showError("");
    phoneSend.disabled = true;
    try {
        const verifier = await ensureRecaptcha();
        confirmationResult = await signInWithPhoneNumber(auth, phoneNumber, verifier);
        smsModal?.classList.add("is-active");
        smsInput?.focus();
        showStatus("SMS code sent.");
    } catch (err) {
        try { recaptchaVerifier?.clear(); } catch { /* ignore */ }
        recaptchaVerifier = null;
        showError(friendlyAuthError(err));
    } finally {
        phoneSend.disabled = false;
    }
});

smsCancel?.addEventListener("click", () => {
    smsModal?.classList.remove("is-active");
});

smsConfirm?.addEventListener("click", async () => {
    const code = smsInput?.value.trim();
    if (!code || code.length !== 6) {
        showError("Enter the 6-digit SMS code.");
        return;
    }
    try {
        await confirmationResult.confirm(code);
        smsModal?.classList.remove("is-active");
    } catch (err) {
        showError(friendlyAuthError(err));
    }
});
