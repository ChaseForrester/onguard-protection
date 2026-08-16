/**
 * Client gate. Call after every Firebase Auth state change.
 * Unverified / rejected / blocked → signOut immediately.
 * kyc_required / kyc_pending → KYC routes only.
 * verified or superadmin → app.
 */
import { getAuth, signOut } from "firebase/auth";
import { getFunctions, httpsCallable } from "firebase/functions";

export type AccessState =
    | "unverified"
    | "kyc_required"
    | "kyc_pending"
    | "verified"
    | "rejected"
    | "blocked";

export async function enforceAccess(): Promise<
    | { route: "/kyc"; accessState: AccessState }
    | { route: "/kyc/pending"; accessState: AccessState }
    | { route: "/admin"; accessState: AccessState }
    | { route: "/super"; accessState: AccessState }
> {
    const auth = getAuth();
    const user = auth.currentUser;
    if (!user) throw new Error("unauthenticated");
    await user.getIdToken(true);
    const token = await user.getIdTokenResult();

    if (token.claims.superadmin === true) {
        return { route: "/super", accessState: "verified" };
    }

    try {
        const fn = httpsCallable(getFunctions(), "assertAccess");
        const res = await fn({});
        const accessState = (res.data as { accessState: AccessState }).accessState;
        if (accessState === "kyc_required") return { route: "/kyc", accessState };
        if (accessState === "kyc_pending") return { route: "/kyc/pending", accessState };
        if (accessState === "verified") return { route: "/admin", accessState };
        await signOut(auth);
        throw new Error("force_logout");
    } catch {
        await signOut(auth);
        throw new Error("force_logout");
    }
}
