---
id: REDGE-5
title: 'Implement redge update: fetch-all, never mutate a working tree'
status: To Do
created_date: 2026-10-18 20:03
dependencies:
- REDGE-2
- REDGE-3
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Fetch every repo including dirty ones (fetch never touches the working tree); refresh index/available state. A failed fetch reads UNKNOWN freshness and must not advance last-fetch (R4).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 every repo fetched; dirty repos fetched too
- [ ] #2 no working-tree mutation under any input (mutation-proven)
- [ ] #3 failed fetch -> UNKNOWN, last-fetch not advanced
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
