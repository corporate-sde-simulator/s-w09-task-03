# DEVTOOLS-101: Resolve Merge Conflicts in User Auth Module

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 30 · **Story Points:** 3
**Reporter:** Vikram Shah (Tech Lead) · **Assignee:** You (Intern)
**Due:** End of day
**Labels:** `git`, `merge`, `auth`, `python`
**Task Type:** Bug Fix

---

## Description

Two developers (Priya and Arjun) both modified `authService.py` on separate branches.
Arjun's branch was merged first. Now Priya's branch has merge conflicts.

Your job: resolve the conflicts so that **both** sets of changes are preserved correctly.

The file `src/authService.py` contains Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
You need to manually resolve each conflict by choosing the correct combination.

## Requirements

- Preserve Priya's new `validate_token()` method
- Preserve Arjun's improved `hash_password()` using bcrypt
- Keep the updated import statements from both branches
- Remove ALL conflict markers

## Acceptance Criteria

- [ ] No conflict markers remain (`<<<<<<<`, `=======`, `>>>>>>>`)
- [ ] `validate_token()` method exists and works
- [ ] `hash_password()` uses bcrypt (Arjun's version)
- [ ] Both sets of imports are present
- [ ] All tests pass
