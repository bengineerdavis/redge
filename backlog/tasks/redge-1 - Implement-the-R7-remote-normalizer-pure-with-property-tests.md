---
id: REDGE-1
title: Implement the R7 remote normalizer (pure) with property tests
status: To Do
created_date: 2026-10-18 20:03
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Pure function normalize(remote) -> host/owner/repo covering SSH vs HTTPS, trailing .git, host aliases. Manifest and registry key repos by this identity, never basename (SPEC R7).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 normalize() handles SSH, HTTPS, trailing .git, host aliases
- [ ] #2 property tests over generated remote forms pass
- [ ] #3 distinct URL forms of one repo normalize identically
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
