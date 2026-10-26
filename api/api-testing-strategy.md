# REST API Testing Strategy — Sample

## Scope
Validate API behavior at the contract boundary and through persistence checks where authorized. Treat status codes, schemas, and business rules as requirements to confirm—not assumptions to invent.

## Test dimensions
- **Contract:** method, path, headers, content type, response schema, required fields
- **Validation:** missing, null, malformed, invalid enum, boundary values, oversized input
- **Authorization:** unauthenticated requests, expired credentials, role boundaries, object-level access
- **State:** create/read/update/delete transitions and behavior for missing or already-processed resources
- **Resilience:** timeout, retry, rate limits, transient errors, duplicate submissions, idempotency
- **Pagination and search:** boundary pages, stable ordering, combined filters, count consistency
- **Data integrity:** persisted values, derived fields, timestamps, relationships, and no partial writes on failure
- **Observability:** correlation IDs and useful error messages without leaking sensitive internals

## Evidence
Keep request/response examples, environment, test data, timestamps, and correlation IDs. Redact tokens, personal data, and secrets. Use synthetic data and only authorized non-production endpoints.

## Exit considerations
Prioritize unresolved security, data-loss, duplicate-write, and critical workflow risks over raw pass rate. Document untested endpoints and residual risk.

## Runnable smoke-test example

The [Postman Echo smoke collection](postman-echo-smoke.postman_collection.json) is a small, runnable demonstration of sending a GET request and checking the response with Postman tests. It calls the public Postman Echo service; it does **not** test an application API or prove business behaviour. Import the JSON into Postman and run the collection with network access enabled.

For product-specific API testing, replace the example with an authorized non-production endpoint and assertions derived from the actual API contract. Never commit credentials or production customer data.
