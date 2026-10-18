---
id: REDGE-3
title: Implement the R6 state store contract
status: To Do
created_date: 2026-10-18 20:03
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Machine-local store under $XDG_STATE_HOME/redge: last-fetch advances only on successful fetch; blocked-since resets only when a clean ff-only clears the reason. Never committed/synced/backed up; no URLs or userinfo. Good run derives from these records, never exit 0 (R6).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 state records persist machine-locally under XDG_STATE_HOME
- [ ] #2 last-fetch does not advance on a failed fetch (mutation-proven)
- [ ] #3 blocked-since resets only on cleared reason
- [ ] #4 store contains no URLs or userinfo
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
