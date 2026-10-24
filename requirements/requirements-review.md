# Requirements Review — Example

## Sample requirement
“When a user edits a task offline, the change should synchronize after connectivity returns.”

## Questions to clarify before testing
1. Which fields can be edited offline?
2. How long must local changes persist?
3. What happens if the user signs out or reinstalls the app before syncing?
4. What is the conflict policy if the same task changes on another device?
5. Is synchronization automatic, manual, or both?
6. How are retry, timeout, partial failure, and server validation errors shown?
7. How can the user identify pending, successful, or failed synchronization?
8. Is synchronization expected to be idempotent?
9. What is the expected behavior on duplicate taps or rapid reconnect/disconnect?
10. Which platforms and minimum OS versions are in scope?

## Example acceptance criteria
- Given a valid offline edit, when connectivity returns, then the change is eventually reflected on the server and other authorized clients.
- Given a transient synchronization failure, when retry conditions are met, then the change is not silently lost.
- Given the same queued change is retried, then duplicate server records are not created.
- Given a conflict, then the documented conflict policy is applied and the user receives the expected feedback.

Acceptance criteria must be agreed with product/engineering; these are proposed examples.
