# API Validation — Offline Content and Synchronization

## Purpose

This document demonstrates how I approach API testing for a mobile learning product with downloadable content and progress synchronisation. It intentionally describes the **test strategy and expected behaviour**, not the production API contract.

The real service may use private endpoints, payloads, identifiers, authentication rules and internal data structures. None of those are reproduced here. The scenarios below are portfolio examples and should be mapped to an approved test environment and its current API documentation before execution.

## What I validate

- **Contract and response:** documented status codes, response structure, required fields, data types and error format.
- **Authentication and access:** unauthenticated requests, expired credentials, and access to resources belonging to another account.
- **Content metadata:** consistency of content identifiers, versions, availability and download metadata between the service and the client.
- **Synchronization:** progress and state changes are retained after reconnecting, repeated sync attempts, app restart and session renewal.
- **Failure handling:** timeouts, interrupted connections, server errors, and retry behaviour do not leave the client in a misleading or inconsistent state.
- **Data integrity:** repeated requests do not unexpectedly create duplicate progress or content records; the final state follows the product's documented conflict-resolution rules.
- **Compatibility:** supported app versions and platforms handle responses consistently.

## Example test scenarios

| ID | Scenario | Checks and expected result |
|---|---|---|
| API-01 | Request a resource with valid authentication | The response matches the approved contract and contains only fields the client is allowed to receive. |
| API-02 | Send a request without credentials | The service rejects the request according to its documented authentication behaviour; no protected data is returned. |
| API-03 | Use an expired session | The client receives a defined authentication response and can recover through the supported sign-in flow. |
| API-04 | Request a resource outside the user's permissions | Access is denied without exposing another user's data. |
| API-05 | Retrieve content metadata | Identifiers, version, availability and required metadata are internally consistent with the approved test fixture. |
| API-06 | Interrupt a content download | The client does not mark incomplete content as ready for use; recovery follows the documented retry/resume behaviour. |
| API-07 | Change progress while offline, then reconnect | Local changes are synchronised according to the product's rules and remain correct after refresh or app restart. |
| API-08 | Retry a sync request after a timeout | Repeating the operation does not produce unintended duplicate changes; the resulting state is deterministic. |
| API-09 | Simulate a server error during sync | The client preserves recoverable local state, communicates the failure appropriately and can retry safely. |
| API-10 | Compare the same account across supported clients | Content availability and synchronised progress agree after sync completes, allowing for documented platform differences. |
| API-11 | Submit missing or invalid input | The service returns the documented validation response and does not persist invalid state. |
| API-12 | Check a response after a content update | The client handles the new version and any required refresh or re-download without mixing incompatible content states. |

## Evidence I collect

For a defect or failed check, I capture only information permitted by the test environment:

- environment and app/build version;
- scenario, preconditions and reproducible steps;
- request method and a sanitised route label, where disclosure is permitted;
- status code, relevant response fields and correlation/request ID, if available;
- timestamp, client logs and a redacted network trace when useful;
- actual versus expected result and whether the issue is reproducible.

## Example defect report structure

**Title:** Progress state is not reconciled after reconnecting

**Preconditions:** An authorised test account has synchronisation enabled and a known starting progress state.

**Steps:**
1. Open a supported client and confirm the starting state.
2. Disconnect the device from the network.
3. Change progress locally.
4. Restore connectivity and allow synchronisation to finish.
5. Refresh the relevant view or restart the client, then compare the state.

**Expected:** The final state follows the documented synchronisation and conflict-resolution rules and remains consistent after refresh.

**Actual:** Record the observed result, frequency, affected build/platform and supporting redacted evidence. This field must be filled only after reproducing a real issue; the scenario above is not a claim that such a production defect occurred.

## Confidentiality and safe sharing

This portfolio does not include real production URLs, endpoint paths, tokens, credentials, customer data, private payloads, internal schemas, or screenshots of authenticated systems. Names and structures are kept generic deliberately. If a hiring team needs a runnable collection, I would build it against an authorised demo or sandbox API using public documentation and synthetic test data, with secrets stored in local environment variables rather than committed to Git.

**Note:** These are illustrative scenarios that demonstrate my testing approach, not a copy of the Airhead ATPL API specification and not evidence of actual production incidents.
