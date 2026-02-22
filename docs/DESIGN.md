# ADR-020: Auth Service Merge Strategy

**Date:** · **Status:** Accepted

## Context
Two features developed in parallel need to be merged.

## Decision
Keep BOTH features: bcrypt hashing (Arjun) + JWT tokens (Priya).
Login should return a JWT token, passwords should use bcrypt.

## Resolution Strategy
| Conflict | Resolution |
|----------|-----------|
| Imports | Keep both: `bcrypt`, `jwt`, `secrets` |
| `hash_password` | Use Arjun's bcrypt version |
| `validate_token` | Keep Priya's JWT implementation |
| `login` return | Use Priya's token approach with Arjun's session ID as backup |
