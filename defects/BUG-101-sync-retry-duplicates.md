# BUG-101 — Retrying a Queued Offline Change Creates a Duplicate

**Status:** Hypothetical example — not a verified production defect  
**Component:** Mobile sync / task API  
**Proposed severity:** High if duplicate records affect user data  
**Priority:** To be agreed after triage

## Preconditions
- Use a dedicated non-production environment.
- A synthetic test account can create tasks offline.
- Sync retry behavior is enabled.

## Steps to reproduce
1. Disable network connectivity.
2. Create one task and confirm it is queued locally.
3. Restore connectivity.
4. Simulate or observe a timeout after the server may have accepted the request.
5. Trigger the documented retry mechanism.
6. Compare the client queue, API response, and server-side records.

## Actual result
In this hypothetical scenario, two server records appear for one user action.

## Expected result
The operation is processed according to the documented retry/idempotency contract without an unintended duplicate.

## Evidence required
Timestamped recording, redacted request/response IDs, client build, server correlation ID, and read-only database evidence.

## Triage questions
- Does the API support idempotency keys?
- Was the first request committed before the timeout?
- Is the duplicate created by the client queue or server write path?
- Can the issue be reproduced without network simulation?
