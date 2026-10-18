---
id: REDGE-6
title: 'Implement redge upgrade: ff-only, clean attached non-diverged only'
status: To Do
created_date: 2026-10-18 20:03
dependencies:
- REDGE-5
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The binding safety contract: git merge --ff-only toward the locked/upstream ref, only when clean + attached + non-diverged. Never merge/rebase/reset/stash. Verdicts per repo: fast-forwarded / skipped:reason; diverged or detached sets blocked-since. Advance the pin only when the merge succeeds. Repo-local problem exits 0; provider/config defect fails the run (R4, R5).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 clean ahead-only repo fast-forwards
- [ ] #2 dirty repo fetched, skipped: dirty, tree untouched
- [ ] #3 diverged repo blocked-since set, tree untouched, no merge/rebase/reset/stash ever invoked (mutation-proven)
- [ ] #4 pin advances only on successful ff merge
- [ ] #5 repo-local failure exits 0; provider/config defect fails the run
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
