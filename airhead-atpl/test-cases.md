# Test Cases — Offline Mode, Downloads and Synchronization

These are executable-style portfolio examples. Replace the illustrative subject/account data with approved test-environment data when running them.

## Test setup

- **Platforms:** iOS and Android; compare with web where the workflow is supported.
- **Network controls:** stable Wi-Fi, airplane mode, network disabled during an operation, and restored connectivity.
- **Test data:** a test account with one downloaded subject and one subject available for download.
- **Evidence:** app build, OS version, timestamps, screenshots/video, and relevant logs or request/response details where available.

| ID | Priority | Scenario | Steps | Expected result |
|---|---|---|---|---|
| ATPL-SYNC-01 | P1 | Open previously downloaded content offline | Download a subject; confirm completion; enable airplane mode; force-close and reopen the app; open the subject | Downloaded content opens without a network request being required for the stored material |
| ATPL-SYNC-02 | P1 | Interrupt a content download | Start downloading a subject; disable the network before completion; inspect the download state | The operation is not shown as successfully completed; the user receives a clear state and can retry |
| ATPL-SYNC-03 | P1 | Retry an interrupted download | Complete ATPL-SYNC-02; restore connectivity; retry the download | The download resumes or restarts according to product design; content is usable after confirmed completion |
| ATPL-SYNC-04 | P1 | Reconnect after offline use | Open downloaded content offline; perform a supported progress-changing action; restore connectivity; wait for sync | The action is retained and synchronization reaches a clear completed or actionable error state |
| ATPL-SYNC-05 | P1 | Avoid duplicate state after repeated sync | Complete a sync; trigger sync again without changing data | Repeating sync does not create duplicate content or duplicate progress records |
| ATPL-SYNC-06 | P1 | Restart during synchronization | Start sync; background or force-close the app during the operation; reopen after reconnecting | The app recovers to a consistent state and communicates whether pending work remains |
| ATPL-SYNC-07 | P2 | Update already downloaded content | Download a subject; make a newer content version available in the test environment; run the update flow | The app clearly indicates the version/state and does not mix incompatible old and new content |
| ATPL-SYNC-08 | P2 | Switch between Wi-Fi and mobile data | Start a supported download on Wi-Fi; switch network type during the operation | The operation completes or fails gracefully without a false success state or corrupted content |
| ATPL-SYNC-09 | P2 | Compare the same account across platforms | Complete a defined progress action on one supported platform; sync; inspect the same account on another platform | Shared state matches the product's documented synchronization rules |
| ATPL-SYNC-10 | P2 | Session expires during a server operation | In a controlled test environment, expire the session during sync; attempt the operation | The app handles authentication failure clearly and does not silently discard pending state |
| ATPL-SYNC-11 | P2 | Low storage during download | Use a test device with limited free storage; start a download that needs more space | The app reports the problem clearly, avoids claiming completion, and remains usable |
| ATPL-SYNC-12 | P2 | Offline search or filtering | Open downloaded material offline; apply supported search and filters | Available local functionality behaves as specified; unavailable functionality gives useful feedback |

## Additional exploratory charters

### Charter A — “Break the connection”
Explore the download and synchronization journey while switching the network off and on at different moments. Look for false completion states, stuck spinners, repeated actions and unclear recovery paths.

### Charter B — “Interrupt the app”
Background, force-close and reopen the app during download, sync and content viewing. Check persistence, recovery and the clarity of operation status.

### Charter C — “Compare state”
Use the same test account on supported platforms. Compare downloaded content, progress and counts after a defined sequence of actions. Record differences before deciding whether they are defects or expected platform limitations.

## Execution notes

For every failure, record the exact build and OS, initial state, network state, timing, reproduction rate, and evidence. Do not report a cross-platform difference as a defect until expected product behaviour and any documented platform limitations have been checked.
