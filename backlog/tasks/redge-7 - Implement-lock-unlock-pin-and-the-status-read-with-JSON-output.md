---
id: REDGE-7
title: Implement lock/unlock/pin and the status read with JSON output
status: To Do
created_date: 2026-10-18 20:03
dependencies:
- REDGE-6
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
lock/unlock record or clear a pinned ref (explicit, user-initiated); never enforce by rewriting the tree. status reports per-repo verdicts + staleness from the state store. JSON output mode; stable machine-readable contract (SPEC The pinning split, R5).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 lock/unlock record and clear pins without tree mutation
- [ ] #2 status reports verdicts + staleness from state records
- [ ] #3 JSON output contract stable and tested
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
