# Writing Mitigations

Mitigations describe or implement defensive controls that reduce exposure.

Mitigation guidance should include:

- What the control changes
- Where it should be applied
- How to verify it
- Known limitations
- Regression expectations

Reusable mitigation code belongs in `src/aisec/mitigations/`. Vulnerability-specific examples belong under the pack's `secure/` directory.
