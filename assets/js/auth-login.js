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
    const code = err?.code || "";
    if (code === "auth/popup-closed-by-user") return "Google sign-in was cancelled.";
    if (code === "auth/popup-blocked") return "Your browser blocked the Google popup. Allow popups and try again.";
    if (code === "auth/unauthorized-domain") return "This domain is not authorised in Firebase Auth yet.";
    if (code === "auth/invalid-credential" || code === "auth/wrong-password" || code === "auth/user-not-found") {
        return "Email or password is not correct.";
    }
    if (code === "auth/too-many-requests") return "Too many attempts. Wait a moment and try again.";
    if (code === "auth/invalid-phone-number") return "Use international format, for example +61432893343.";
    return err?.message || "Sign-in failed.";
}

async function routeSignedInUser(user) {
    if (routing) return;
    routing = true;
    try {
        const token = await user.getIdTokenResult(true);
        const isSuper = token.claims.superadmin === true;
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

phoneBtn?.addEventListener("click", async () => {
    const phoneNumber = window.prompt("Enter your mobile in international format (e.g. +61432893343):");
    if (!phoneNumber) return;
    showError("");
    try {
        if (!recaptchaVerifier) {
            recaptchaVerifier = new RecaptchaVerifier(auth, "recaptcha-container", { size: "invisible" });
        }
        confirmationResult = await signInWithPhoneNumber(auth, phoneNumber, recaptchaVerifier);
        smsModal?.classList.add("is-active");
        smsInput?.focus();
        showStatus("SMS code sent.");
    } catch (err) {
        showError(friendlyAuthError(err));
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
