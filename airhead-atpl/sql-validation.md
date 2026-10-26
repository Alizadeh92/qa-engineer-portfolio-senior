# SQL and Data-Consistency Validation

This document shows how I use database checks to support a manual investigation. The SQL is generic and must be adapted to the approved test schema. Table and column names below are illustrative; they are not a claim about Airhead's internal database structure.

## 1. Compare expected and actual records

When investigating a missing or duplicated item, first define the business key and expected state. For example, in a demo schema with a user_progress table:

```sql
SELECT user_id, content_id, COUNT(*) AS record_count
FROM user_progress
WHERE user_id = :test_user_id
GROUP BY user_id, content_id
HAVING COUNT(*) > 1;
```

**Purpose:** identify multiple records for the same user/content pair if the schema expects that pair to be unique.

## 2. Find progress records without a matching content item

```sql
SELECT p.user_id, p.content_id
FROM user_progress AS p
LEFT JOIN content_items AS c
  ON c.id = p.content_id
WHERE p.user_id = :test_user_id
  AND c.id IS NULL;
```

**Purpose:** find orphaned progress references in a demo relational model.

## 3. Review pending synchronization events

For a demo table named sync_events:

```sql
SELECT event_id, user_id, entity_id, status, created_at, updated_at
FROM sync_events
WHERE user_id = :test_user_id
  AND status IN ('pending', 'failed')
ORDER BY created_at;
```

**Purpose:** help correlate a user-visible synchronization issue with pending or failed events, if the system exposes this information to QA.

## 4. Investigation sequence

1. Capture the initial state and the exact user action.
2. Record timestamps and the device's connectivity state.
3. Reproduce the issue and capture the final UI state.
4. Check available API responses and logs.
5. Use read-only SQL checks in an authorised test database to compare expected and stored state.
6. Correlate evidence before forming a root-cause hypothesis.
7. Retest the fix and check adjacent cases such as retry, app restart and repeated synchronization.

## Safety and accuracy

Use parameterised queries and read-only access wherever possible. Never run illustrative queries against production data. Do not infer that a database issue exists just because the UI is inconsistent; local caching, API behaviour, delayed processing and expected product rules may also explain the observation.
