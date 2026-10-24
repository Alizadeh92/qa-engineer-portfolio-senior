# SQL Investigation Patterns

These examples use illustrative table/column names. Adapt them to an approved demo schema and use read-only access unless a change is explicitly authorized.

## Find likely duplicate records
```sql
SELECT user_id, external_key, COUNT(*) AS record_count
FROM tasks
GROUP BY user_id, external_key
HAVING COUNT(*) > 1;
```

## Check for orphan child rows
```sql
SELECT c.id, c.task_id
FROM task_events AS c
LEFT JOIN tasks AS t ON t.id = c.task_id
WHERE t.id IS NULL;
```

## Reconcile status counts
```sql
SELECT status, COUNT(*) AS total
FROM tasks
GROUP BY status
ORDER BY status;
```

## Compare one test record
```sql
SELECT id, title, status, updated_at
FROM tasks
WHERE id = :task_id;
```

## Investigation discipline
- Record environment, query, parameters, timestamp, and expected rule.
- Use transactions/read-only sessions where practical; avoid unrestricted production queries.
- Consider soft deletes, tenant boundaries, eventual consistency, and replication lag before declaring a mismatch.
- Never include real personal data or credentials in the portfolio.
