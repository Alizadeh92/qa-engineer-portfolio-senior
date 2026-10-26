# Example Bug Reports

The reports below are **illustrative examples** created to demonstrate defect-reporting style. They are not presented as confirmed incidents from the production product.

## BUG-01 — Interrupted download is displayed as completed

**Severity:** Major (proposed; confirm impact during triage)  
**Priority:** High (proposed)  
**Area:** Mobile / Content download  
**Environment:** iOS or Android test build; exact build and OS to be recorded during execution  
**Reproducibility:** To be measured during execution

### Preconditions
- The user is signed in.
- A subject is available for download.
- The device has a controllable network connection.

### Steps to reproduce
1. Open the subject download screen.
2. Start downloading the subject.
3. Disable the network before the download finishes.
4. Wait for the app to settle and inspect the download status.
5. Open the subject or attempt to use the downloaded content.

### Actual result
*Example observation to verify:* the UI shows a completed state even though some content is unavailable.

### Expected result
The app should not report a successful download until the required content is available. If the operation is interrupted, the status should reflect the incomplete state and provide a clear recovery action.

### Impact
A learner may rely on content being available offline and discover the missing material only when internet access is unavailable.

### Evidence to attach
Screen recording, timestamps, app build, OS version, network transition details, and relevant logs or requests where accessible.

### Triage notes
Confirm whether the UI status and content manifest disagree. Check whether the issue is reproducible after app restart and whether retry resolves it.

---

## BUG-02 — Progress differs after reconnecting from offline use

**Severity:** Major (proposed; depends on data-loss scope)  
**Priority:** High (proposed)  
**Area:** Mobile / Offline state / Synchronization  
**Environment:** Record exact app build, OS and backend environment during execution

### Preconditions
- The user has a valid account and downloaded content.
- The tested progress action is supported offline.
- The account can be checked again after connectivity is restored.

### Steps to reproduce
1. Open downloaded content while online and confirm the starting progress.
2. Enable airplane mode.
3. Perform a progress-changing action supported by the product.
4. Close and reopen the app while still offline.
5. Restore connectivity and wait for synchronization.
6. Inspect progress on the original device and, if supported, another platform.

### Actual result
*Example observation to verify:* the offline action is visible locally but is missing or different after synchronization.

### Expected result
The action should follow the documented offline/sync rules and result in a consistent state. If synchronization fails, the user should receive a clear indication rather than silent data loss.

### Impact
The learner may lose confidence in progress tracking or repeat work unnecessarily.

### Evidence to attach
Initial and final state, exact action sequence, timestamps, connectivity changes, screenshots, relevant request/response data, and reproduction rate.

### Triage notes
Check whether the action was persisted locally, whether a sync request was sent, and whether the server accepted or rejected it. Avoid assuming the root cause before evidence is available.

---

## Reporting standard

- Separate **observed behaviour** from assumptions about root cause.
- Keep actual and expected results specific.
- Use severity to describe impact and priority to describe urgency.
- Record reproducibility rather than writing “always” without repeated checks.
- Remove credentials, personal data and private endpoint details from screenshots and logs.
