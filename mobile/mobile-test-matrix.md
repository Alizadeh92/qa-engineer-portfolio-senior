# Mobile Test Matrix — Offline, Sync, and Lifecycle

Illustrative matrix; choose devices/OS versions based on actual product support and usage data.

| Area | Setup / action | Expected behavior | Priority |
|---|---|---|---|
| Offline create | Disable network, create an item | Clear pending state; no silent data loss | High |
| Reconnect | Restore network with queued changes | Changes synchronize and reach a stable state | High |
| Retry | Simulate transient timeout and retry | No unintended duplicate; retry outcome is visible | High |
| Conflict | Edit same entity from two authorized clients | Documented conflict rule is applied | High |
| Background/foreground | Background app during sync, then resume | Operation recovers safely; state remains consistent | High |
| Force close | Terminate app with pending changes | Local queue persists according to specification | High |
| Session expiry | Expire token while changes are queued | Safe re-authentication and recoverable pending work | High |
| Network switch | Wi-Fi to cellular during transfer | Recovery follows contract; no corrupt state | Medium |
| Low storage | Approach device storage limit in test environment | Useful error/recovery; no silent corruption | Medium |
| Upgrade | Upgrade app with pending local changes | Data migration and sync remain consistent | High |
| Repeated action | Tap submit/retry rapidly | Duplicate prevention matches the contract | High |
| Cross-platform | Perform same scenario on iOS and Android | Behavior is functionally consistent with documented differences | Medium |

## Evidence to collect
App/build and OS version, device model, network transitions, exact timestamps, local state where available, redacted API/correlation IDs, final persisted state, and screen recording.
