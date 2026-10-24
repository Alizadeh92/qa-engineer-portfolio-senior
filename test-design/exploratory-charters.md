# Exploratory Testing Charters

Use time-boxed sessions. Record build/environment, mission, actions, observations, questions, and follow-up tests.

## Charter A — Offline-to-online synchronization
**Timebox:** 45 minutes  
**Mission:** Explore whether offline edits survive connectivity changes and repeated retries.

**Ideas to investigate**
- Toggle airplane mode before, during, and after editing
- Force-close and relaunch with pending changes
- Reconnect on a different network
- Retry repeatedly and rapidly
- Edit the same entity on a second authorized client
- Inspect user feedback and final server state

**Stop conditions:** Data loss, cross-user data exposure, or repeatable corruption; capture evidence and escalate.

## Charter B — Search, filters, and counts
**Timebox:** 30 minutes  
**Mission:** Look for inconsistent result sets when search, filters, sorting, and pagination interact.

**Ideas to investigate**
- Apply filters individually and in combination
- Search with case, whitespace, special characters, and no matches
- Change sorting while on a later page
- Reset filters after a search
- Compare visible rows, pagination, and displayed counts

## Charter C — API resilience and retries
**Timebox:** 30 minutes  
**Mission:** Investigate validation, retry, timeout, and duplicate-submission behavior.

**Ideas to investigate**
- Missing and invalid fields
- Unexpected enum values and boundary lengths
- Simulated timeout followed by retry in a safe test environment
- Repeated create requests
- Missing/expired credentials and insufficient permissions

Do not perform destructive or high-volume experiments against production systems.
