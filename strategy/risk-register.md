# Risk Register — Example

The scores below are illustrative. For a real release, use the team's agreed risk scale and decision policy.

## Priority definitions

- **P0 — Critical:** credible risk of major data loss, security/privacy breach, or a core journey being unusable for many users. Escalate immediately; release requires an explicit risk-owner decision.
- **P1 — High:** important workflow broken or unreliable, with material user impact and no acceptable workaround. Fix and retest before release where feasible; exceptions need documented acceptance.
- **P2 — Medium:** limited impact or degraded workflow with a reasonable workaround. Deferral needs an owner and follow-up plan.
- **P3 — Low:** cosmetic or low-impact behaviour with little effect on task completion. Prioritise by user impact and capacity.

Priority is not severity alone. Consider impact, likelihood, scope, detectability, workarounds, data integrity and the cost of a late fix.

## Example risk register

| ID | Risk | Impact (1–5) | Likelihood (1–5) | Priority | Release response / evidence |
|---|---|---:|---:|---|---|
| R-01 | Offline progress is lost after reconnect | 5 | 3 | P0 | Block release if confirmed; test persistence, retry and final state |
| R-02 | Retry creates duplicate progress or content | 4 | 3 | P1 | Verify repeated requests, retry behaviour and idempotency |
| R-03 | User can access another account's data | 5 | 2 | P0 | Escalate immediately; verify access boundaries with controlled test accounts |
| R-04 | Download appears complete but content is unusable | 4 | 3 | P1 | Verify interruption, metadata and recovery across supported platforms |
| R-05 | Android app becomes unresponsive during a critical flow | 4 | 3 | P1 | Reproduce on representative devices and inspect ANR evidence |
| R-06 | Search/filter count disagrees with displayed results | 3 | 4 | P1 | Test combinations, pagination, reset and count behaviour |
| R-07 | UI alignment issue on an uncommon supported viewport | 1 | 3 | P3 | Assess accessibility and task impact; schedule a visual fix if appropriate |

## Prioritisation under time constraints

1. Test P0 risks first: data integrity, access control and core journey availability.
2. Test P1 risks next: sync/download recovery, authentication and high-use workflows.
3. Select P2/P3 checks based on changed components, supported platforms and defect history.
4. Record untested areas, evidence, residual risk, owner and release decision. Never imply that unexecuted tests passed.

Reassess risks after major changes, incidents, repeated defect patterns, platform changes or discovery of a new user journey.
