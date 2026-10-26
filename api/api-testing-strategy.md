# REST API Testing Strategy

## Scope

Validate API behaviour against the approved contract and, where authorised, verify persisted state.

## Test dimensions

- **Contract:** method, headers, content type, response schema and required fields
- **Validation:** missing, null, malformed and boundary values
- **Authorisation:** unauthenticated requests, expired credentials, role and object-level access
- **State:** create/read/update/delete transitions and already-processed resources
- **Resilience:** timeouts, retries, rate limits, duplicate submissions and idempotency
- **Search and pagination:** boundary pages, stable ordering, combined filters and count consistency
- **Data integrity:** persisted values, relationships, timestamps and partial writes on failure
- **Observability:** correlation IDs and useful errors without exposing sensitive information

## Evidence and release considerations

Record the environment, test data, request/response details, timestamps and correlation IDs where available. Use synthetic data, authorised non-production environments and redact secrets. Prioritise unresolved security, data-loss, duplicate-write and critical-workflow risks over raw pass rate; document gaps and residual risk.

## Runnable smoke-test example

The [Postman Echo smoke collection](postman-echo-smoke.postman_collection.json) sends a GET request and checks the response using Postman tests. It exercises the public Postman Echo service, not a private application API or business workflow. Import the JSON into Postman and run it with network access enabled.

For product-specific tests, use an authorised sandbox and assertions derived from its API contract. Never commit credentials or production customer data.
