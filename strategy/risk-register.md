# Risk Register — Illustrative

Scores and priorities below are examples for portfolio demonstration, not measured product data or actual production incidents. In a real release, align the scale and release decision with the team's risk policy.

## Priority definitions

- **P0 — Critical:** credible risk of major data loss/corruption, security or privacy breach, or a core journey being unusable for a broad set of users. Stop release or escalate immediately; release requires an explicit risk-owner decision.
- **P1 — High:** an important workflow is broken or unreliable, with material user impact and no acceptable workaround. Fix and retest before release where feasible; any exception needs documented acceptance.
- **P2 — Medium:** limited impact or a degraded workflow with a reasonable workaround. Assess scope and regression risk; deferral needs an owner and follow-up plan.
- **P3 — Low:** cosmetic or low-impact behaviour with little effect on task completion. Fix based on user impact and available capacity.

Priority is not severity alone. I consider user impact, likelihood, scope, detectability, workaround, data integrity and the cost of a late fix.

## Example risk register

| ID | Risk | Impact (1–5) | Likelihood (1–5) | Priority | Release response / evidence |
|---|---|---:|---:|---|---|
| R-01 | Offline progress is lost after reconnect | 5 | 3 | P0 | Block release for a confirmed data-loss path; test queue persistence, retry and final persisted state |
| R-02 | Retry creates duplicate progress or content records | 4 | 3 | P1 | Verify repeated requests, retry behaviour and idempotency; regression-test sync |
| R-03 | User can access another account's data | 5 | 2 | P0 | Escalate immediately; verify access boundaries using controlled test accounts |
| R-04 | Download appears complete but content is unusable | 4 | 3 | P1 | Verify interrupted download, metadata/state and recovery across supported platforms |
| R-05 | Android app becomes unresponsive during a critical flow | 4 | 3 | P1 | Reproduce on representative devices; inspect ANR evidence and re-test fix |
| R-06 | Search/filter count disagrees with displayed results | 3 | 4 | P1 | Test combinations, pagination, reset and count reconciliation |
| R-07 | UI alignment issue on an uncommon supported viewport | 1 | 3 | P3 | Check impact and accessibility; schedule a visual fix if it blocks no critical action |

## Release prioritisation under time constraints

If only a short regression window remains, I would:

1. Run P0 scenarios first: data integrity, security/access control and core journey availability.
2. Run P1 scenarios next: sync/download recovery, authentication/session handling and high-use workflows.
3. Select P2 and P3 checks based on changed components, supported-platform coverage and defect history.
4. Document untested areas, evidence, residual risk, owner and the release decision—never imply that unexecuted tests passed.

## Reassessment triggers

Re-score risks after architecture changes, major feature work, incidents, repeated defect patterns, changes to supported platforms, or discovery of a new user journey.
