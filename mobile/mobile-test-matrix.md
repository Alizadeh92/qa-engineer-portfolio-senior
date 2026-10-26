# Mobile Test Matrix — Offline, Sync, Lifecycle and Platform Differences

Illustrative matrix; select devices and OS versions using the actual product support policy and usage data. Priorities are starting points and must be re-evaluated against release scope and risk.

| Area | Setup / action | Expected behaviour | Priority |
|---|---|---|---|
| Offline create | Disable network and create/change supported data | Clear pending state; no silent data loss | P1 |
| Reconnect | Restore network with queued changes | Changes synchronise and reach a stable state | P0 |
| Retry | Simulate transient timeout and retry | No unintended duplicate; retry outcome is visible | P1 |
| Conflict | Edit the same entity from two authorised clients | Documented conflict rule is applied | P1 |
| Background/foreground | Background app during sync, then resume | Operation recovers safely; state remains consistent | P1 |
| Force close | Terminate app with pending changes | Local queue persists according to specification | P1 |
| Session expiry | Expire session while changes are queued | Safe re-authentication and recoverable pending work | P1 |
| Network switch | Switch Wi-Fi to cellular during transfer | Recovery follows contract; no corrupt state | P1 |
| Low storage | Approach device storage limit in test environment | Useful error/recovery; no silent corruption | P1 |
| Upgrade | Upgrade with pending local changes | Migration and sync remain consistent | P1 |
| Repeated action | Tap submit/retry rapidly | Duplicate prevention matches contract | P1 |
| Cross-platform | Run equivalent scenario on iOS and Android | Business behaviour is consistent; documented OS differences are respected | P1 |
| Android Back | Navigate back from nested screen or active form | Correct navigation; no unintended loss of pending input | P2 |
| Android permissions | Deny, revoke or restrict a permission | App handles capability loss without looping prompts | P2 |
| iOS Universal Links | Open supported link from another app/browser | Correct destination or safe fallback | P2 |
| iOS background refresh | Change Background App Refresh setting where relevant | UI does not misrepresent stale data or promise unsupported refresh | P2 |

## Evidence to collect

App/build and OS version, device model, network transitions, permission state, timestamps, local state where available, redacted API/correlation IDs, final persisted state, reproduction rate and screen recording.
