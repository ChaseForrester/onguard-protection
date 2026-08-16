# Screen specification — Phase 1

## Public (no auth)
1. `/login` — Google button, email/password, phone (FirebaseUI or custom). Footer: NSW Class 1 operatives only.
2. `/login/phone` — SMS code confirm.

## Authenticated, not verified
3. `/kyc` — only if `accessState == kyc_required`.
   - Upload licence front + back (Storage)
   - Multi-select Schedule D 1A–1F (exact labels)
   - Licence number + expiry
   - Mobile + email
   - BSB + account + account name
   - Super: USI **or** fund name
   - First-aid expiry (optional at submit; required later for 1A crowd/event roster)
   - Jurisdiction locked to NSW
4. `/kyc/pending` — wait state. No other nav.
5. `/denied` — after force-logout. Explains OG-LEG-2026-001 restricted access.

## Verified guard
6. `/admin` — home: next assigned jobs, verification badge, subclasses chips.
7. `/admin/availability` — week picker (Mon start, Australia/Sydney), per-day windows.
8. `/admin/jobs` — assigned jobs only. Status, suburb, start/finish, required activities.
9. `/admin/profile` — read-only licence + subclasses. Edit display name / FCM opt-in. Bank/super not shown in full (last 3 account digits).
10. `/admin/notifications` — list + mark read.

## Super admin (`superadmin` claim)
11. `/super` — verified count, pending KYC count, open jobs.
12. `/super/kyc` — queue. Open licence images. Approve / reject + reason.
13. `/super/guards` — search name, licence number, subclass, suburb/phone. Table of verified only.
14. `/super/guards/:uid` — full KYC (including bank), availability, job history.
15. `/super/jobs/new` — suburb, postcode, window, required activities, first-aid flag, dog flag, armed flag. Jurisdiction locked NSW.
16. `/super/jobs/:id` — assign from search of verified guards whose subclasses pass `rosterAllows`.
17. `/super/jobs` — all jobs filter by status.

## Phase 2 (disabled in rules + `platformConfig.phase2Enabled`)
18. Public search — location, time, experience, subclasses.
19. Public roster / profile pages.
20. Dynamic sitemap >2000. Do not build until `verifiedGuardCount >= 10`.
