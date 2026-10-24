# Risk Register — Illustrative

Scores below are example assessments, not measured product data. Use the team's agreed scoring model in real work.

| ID | Risk | Impact | Likelihood | Priority | Mitigation / evidence |
|---|---|---:|---:|---|---|
| R-01 | Offline edits are lost during reconnect | 5 | 3 | High | Test queue persistence, retry, conflict handling, and repeated sync |
| R-02 | Duplicate records after retry | 4 | 3 | High | Validate idempotency and duplicate prevention at API and UI layers |
| R-03 | User sees another user's data | 5 | 2 | High | Verify authorization boundaries using controlled test accounts |
| R-04 | Search/filter results disagree with displayed count | 3 | 4 | High | Test combined filters, pagination, reset, and count reconciliation |
| R-05 | App crashes after background/foreground transition | 4 | 3 | High | Lifecycle matrix across supported OS/device classes |
| R-06 | Validation differs between UI and API | 3 | 3 | Medium | Compare contract rules and invalid-input cases at both layers |
| R-07 | Cosmetic alignment issue on uncommon viewport | 1 | 3 | Low | Responsive visual spot checks on supported breakpoints |

## Reassessment triggers
Re-score risks after architectural changes, major feature work, incidents, repeated defect patterns, changes to supported platforms, or discovery of a new user journey.
