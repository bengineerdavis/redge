---
id: REDGE-8
title: 'Land the Ansible role: install + trigger, never logic or state'
status: To Do
created_date: 2026-10-18 20:03
dependencies:
- REDGE-6
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
role/ installs redge (uvx/pip/git) and may trigger runs; it never contains redge logic or state (SPEC Boundary). Graduates to an installable role later.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 role installs redge and smoke-checks redge --version
- [ ] #2 no redge logic or state in the role
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
