# Risk-Based Test Catalog

All scenarios are illustrative.

| ID | Risk / area | Scenario | Expected evidence | Risk |
|---|---|---|---|---|
| TC-001 | Core workflow | Create a task with valid required fields | Task persists and is visible after refresh | High |
| TC-002 | Validation | Submit without required title | Contracted validation; no task created | High |
| TC-003 | Authorization | Request a task belonging to another test user | Access is denied or data is appropriately filtered | Critical |
| TC-004 | Idempotency | Retry the same create operation after a simulated timeout | No unintended duplicate resource | High |
| TC-005 | Pagination | Move through pages while filters are active | No unintended gaps/duplicates; counts align with contract | Medium |
| TC-006 | Search | Search using mixed case and leading/trailing spaces | Behavior matches documented normalization rules | Medium |
| TC-007 | Synchronization | Create offline, reconnect, and retry sync | Change arrives once and reaches a stable state | High |
| TC-008 | Conflict | Edit the same entity on two clients | Documented conflict strategy is applied | High |
| TC-009 | Lifecycle | Background app during an in-progress operation | Recovery follows specification; no silent data loss | High |
| TC-010 | Regression | Reset filters after applying several values | Defaults and result set are restored consistently | Medium |
| TC-011 | API errors | Send malformed payload | Safe, documented client error; no partial write | High |
| TC-012 | Data integrity | Compare UI result with persisted record | Relevant fields and status match | High |

## Selection approach
For each release, select tests based on changed components, dependency graph, defect history, risk score, and affected user journeys. Do not blindly execute the entire suite if a targeted strategy is more effective—but document what was omitted and why.
