# Sample Test Summary — Reusable Template

**Product:** [Product or feature]  
**Build:** [Build identifier]  
**Environment:** [QA/UAT environment]  
**Test window:** [Start–end]  
**Prepared by:** [Name]

> This file is a blank template. Replace every placeholder with actual execution evidence before using it for a real project report. For a filled fictional example, see [Illustrative Execution Summary](illustrative-execution-summary.md).

## Executive summary
[Briefly describe scope, outcome, main risks and release recommendation.]

## Execution snapshot
| Status | Count |
|---|---:|
| Passed | [n] |
| Failed | [n] |
| Blocked | [n] |
| Not run | [n] |
| Total planned | [n] |

Do not calculate a pass rate until the denominator and treatment of blocked/not-run tests are explicitly defined.

## Defect snapshot
| Severity | Open | Closed | Notes |
|---|---:|---:|---|
| Critical | [n] | [n] | [Summary] |
| High | [n] | [n] | [Summary] |
| Medium | [n] | [n] | [Summary] |
| Low | [n] | [n] | [Summary] |

## Coverage and limitations
- Critical journeys covered: [list]
- Platforms/builds covered: [list]
- Areas not tested and rationale: [list]
- Environment or test-data constraints: [list]

## Release recommendation
**Recommendation:** [Go / Conditional go / No-go]

**Rationale:** [Evidence, open risks, workarounds, and acceptance decision owner]

**Required follow-up:** [Owner, action, target date]

A high pass rate alone is not sufficient for release approval if a critical data-integrity or authorization risk remains unresolved.
