# SQL Checks for Data Investigation

I use SQL as supporting evidence during a manual investigation—not as proof of root cause by itself. Adapt table and column names to the approved test schema; names below are illustrative.

## Look for duplicate progress records

```sql
SELECT user_id, content_id, COUNT(*) AS record_count
FROM user_progress
WHERE user_id = :test_user_id
GROUP BY user_id, content_id
HAVING COUNT(*) > 1;
```

Use this when the business rule expects one record per user/content pair.

## Find progress records without matching content

```sql
SELECT p.user_id, p.content_id
FROM user_progress AS p
LEFT JOIN content_items AS c ON c.id = p.content_id
WHERE p.user_id = :test_user_id
  AND c.id IS NULL;
```

## Review pending or failed synchronization events

```sql
SELECT event_id, entity_id, status, created_at, updated_at
FROM sync_events
WHERE user_id = :test_user_id
  AND status IN ('pending', 'failed')
ORDER BY created_at;
```

## Investigation sequence

1. Capture the starting state, user action, timestamp and connectivity state.
2. Reproduce the issue and record the final UI state.
3. Check available API responses and client/server logs.
4. Use read-only SQL in an authorised test database to compare expected and stored state.
5. Correlate evidence before forming a root-cause hypothesis.
6. Retest the fix and nearby cases such as retry, restart and repeated synchronization.

Use parameterised queries and read-only access wherever possible. A UI mismatch alone does not establish a database defect; caching, API behaviour, delayed processing or expected product rules may explain it.
