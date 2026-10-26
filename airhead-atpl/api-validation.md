# API Checks for Offline and Synchronization Workflows

This page applies the general [API testing strategy](../api/api-testing-strategy.md) to the learning-product case study. The scenarios below describe what I would verify against the approved API contract; they are not claims about private endpoints or confirmed production incidents.

| Scenario | Main checks |
|---|---|
| Content metadata is retrieved | Required identifiers, version and availability fields match the test fixture and documented contract. |
| Download is interrupted | Incomplete content is not shown as ready; retry or resume follows the documented behaviour. |
| Progress changes while offline | After reconnecting, the final state follows the product's conflict-resolution rules and survives refresh or app restart. |
| Sync request is retried after timeout | Retry does not create unintended duplicate changes; final state is deterministic. |
| Server error occurs during sync | Recoverable local state is retained, the failure is communicated clearly, and retry is safe. |
| Same account is checked across clients | Content availability and progress agree after synchronization, allowing for documented platform differences. |
| Session expires during an operation | The client handles authentication recovery without falsely reporting that the operation completed. |

## Evidence for a failed check

Record the build/environment, preconditions, reproduction steps, expected and actual result, status code, relevant redacted response fields, timestamp and correlation ID when available. Attach a sanitised network trace or client log only when it helps reproduce or isolate the issue.

For a real defect, fill in the observed behaviour and impact after reproducing it. Do not infer a backend defect from a UI mismatch alone: caching, delayed processing, client logic and documented product rules may also explain the result.
