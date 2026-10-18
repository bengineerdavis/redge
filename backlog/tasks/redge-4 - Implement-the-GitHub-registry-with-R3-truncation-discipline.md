---
id: REDGE-4
title: Implement the GitHub registry with R3 truncation discipline
status: To Do
created_date: 2026-10-18 20:03
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Registry seam: enumerate an owner via gh/API list endpoints (never Search; Search caps at 1000 and hides incomplete_results). Full/truncated/auth-failed/rate-limited pages read UNKNOWN, never empty; never unregister from an incomplete listing. At most 10 additions per run; archived skipped by default; account scope recorded (R3). Auth via gh auth / SSH; no persisted plaintext token (R8).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 owner enumeration uses list endpoints
- [ ] #2 truncation/auth/rate-limit failures read UNKNOWN, never empty
- [ ] #3 at most 10 repos added per run
- [ ] #4 account scope of listing recorded
- [ ] #5 no plaintext token persisted anywhere
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done
<!-- DOD:BEGIN -->
<!-- DOD:END -->
