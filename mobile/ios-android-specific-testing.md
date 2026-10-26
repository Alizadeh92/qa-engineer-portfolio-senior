# iOS and Android Platform-Specific Testing

## Scope and honesty

This is a sanitised portfolio guide showing how I design platform-specific checks. It is not a claim that every feature below exists in Airhead ATPL or was tested on every OS version. Before execution, confirm supported OS versions, app architecture, requirements and available test environment.

## Android-specific checks

| Area | Test scenario | Expected result | Initial priority |
|---|---|---|---|
| App Links / deep links | Open a valid supported link from a browser, email or another app; test an unknown route | Correct screen opens; invalid/unavailable routes fail safely | P1 |
| Intent filters | Launch with supported and malformed intent data; check whether another app can intercept the link | Only supported inputs are handled and sensitive data is not exposed | P1 |
| Back navigation | Use system Back from nested screens, forms, downloads and dialogs | Navigation follows product rules; unsaved or pending work is not silently lost | P1 |
| Permission: allow once | Grant a permission temporarily where the OS offers this choice, then retry after it expires | The app detects the changed permission state and explains what is needed | P2 |
| Permission denied | Deny a permission and repeat the relevant flow | App remains usable where possible and handles unavailable capability gracefully | P1 |
| Don't ask again / restricted permission | Deny repeatedly, then use the supported route to Settings | App does not loop permission prompts; guidance is accurate | P2 |
| Background limits | Background the app during a supported transfer, wait, then resume | Operation recovers or reports its state accurately | P1 |
| ANR / responsiveness | Exercise heavy or long-running operations on representative supported devices | Main interaction remains responsive; no reproducible ANR under agreed conditions | P1 |

Android permission wording and behaviour vary by OS version and permission type. Test the actual supported versions; do not assume every permission exposes the same choices.

## iOS-specific checks

| Area | Test scenario | Expected result | Initial priority |
|---|---|---|---|
| Universal Links | Open a valid associated domain link from Safari, Messages or another app | Correct destination opens; fallback behaviour is clear when the app cannot handle it | P1 |
| App background/resume | Background the app during a workflow, then resume after a short and longer interval | State is restored or refreshed according to requirements | P1 |
| Background App Refresh | Disable it in Settings and repeat a workflow that relies on background refresh | User-visible state remains accurate; the app does not promise an update that cannot run | P2 |
| Permission revoked | Change a granted permission in Settings and reopen the feature | App re-checks permission state and degrades gracefully | P1 |
| ATT, if applicable | On an app that performs tracking requiring ATT, test Allow, Ask App Not to Track and restricted states | Consent choice is respected; tracking does not begin contrary to the selected state | P1 if applicable |
| StoreKit / in-app purchase, if applicable | Test successful purchase, cancellation, pending transaction, restore and interrupted purchase | Entitlement follows verified transaction state; no duplicate entitlement or false success | P1 if applicable |
| Lifecycle interruption | Receive a call/notification or switch apps during a supported operation | The operation and user-entered data remain in a valid state | P2 |

ATT and StoreKit should only be included in actual product testing when the product uses those capabilities. They are included here as examples of platform knowledge, not as claims about Airhead ATPL.

## Cross-platform comparison

For equivalent user journeys on iOS and Android, compare:

- business outcome and persisted data;
- deep-link destination and fallback behaviour;
- offline status, retry and sync recovery;
- permission denial and recovery;
- background/foreground transitions;
- accessibility, text scaling and critical layout;
- error messaging and ability to recover.

A difference is a defect when it violates requirements, supported-platform expectations, data integrity or usability criteria—not merely because the OS conventions differ.

## Defect evidence

Record device model, OS version, app/build, permissions state, launch route, network state, exact steps, expected/actual result, reproduction rate and redacted diagnostics. Use only approved test accounts and synthetic data.
