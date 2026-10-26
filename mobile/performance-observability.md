# Mobile Performance and Observability

## Purpose

This document describes a practical QA approach to investigating stability and performance across supported mobile platforms. Tool names are examples of available diagnostic options, not a claim that each was used on every project. Performance thresholds must be agreed with the product team and measured against a documented baseline.

## Stability and crash diagnostics

| Signal | What I look for | Possible evidence / tools | Priority example |
|---|---|---|---|
| Crash rate and crash-free sessions | New crash clusters after a build, affected versions/devices and reproducibility | Firebase Crashlytics, Sentry, OS crash reports | P1 |
| Android ANR | App stops responding, slow main-thread work, repeated hangs | Android vitals where available, Logcat, Android Studio diagnostics | P1 |
| Failed background work | Sync/download silently stops or never reaches a terminal state | App logs, timestamps, sanitised network traces, backend correlation IDs | P1 |
| Error spikes after release | Regression concentrated in a build, OS version or workflow | Crash/error dashboards and release comparison | P1 |
| Memory growth | Memory increases over a long session or repeated navigation without returning to a stable range | LeakCanary on Android; Xcode Instruments on iOS | P2, raised to P1 if it causes crashes |
| Slow or unstable network | Excessive retries, duplicate requests or a long-running loading state | Charles Proxy or approved network diagnostics | P1/P2 by user impact |

## Performance measurements

| Metric | Measurement approach | Notes |
|---|---|---|
| Cold start | Measure from process launch to a defined usable screen with app process not already running | Record device, OS, build, cache/data conditions and repeated samples |
| Warm start | Measure returning to an existing process from background to the same defined usable state | Keep the comparison conditions consistent |
| Screen / workflow response | Time a named action until meaningful content or completion feedback is visible | Do not use animation completion alone if data is still unavailable |
| Memory | Observe baseline, peak and post-workflow memory during repeated navigation and longer sessions | Look for sustained growth and user-visible impact |
| Battery | Compare a fixed workload over a controlled duration with the same device and settings | Account for screen brightness, radio conditions and background activity |
| Network traffic | Record request count and bytes for a defined action or sync cycle | Look for repeated downloads, unnecessary polling and oversized payloads |

## Practical investigation workflow

1. Define the user-visible symptom and the exact workflow.
2. Record app build, OS, device class, network conditions and test data state.
3. Capture a baseline and repeat the same steps on the candidate build.
4. Correlate timestamps across app logs, crash reports and sanitised network evidence where available.
5. Compare affected and unaffected platform/build combinations.
6. Report the measured result, sample count, variability and impact; avoid asserting a root cause until evidence supports it.
7. Re-test the fix and run focused regression on adjacent workflows.

## Example release gate

The following is a **proposed template**, not a measured product SLA:

- No newly introduced reproducible crash or ANR in a critical supported journey.
- No data loss or corrupt state when a workflow is interrupted.
- Startup and key actions remain within agreed product thresholds on representative devices.
- No sustained memory growth that causes instability during the agreed test session.
- Network and battery usage show no unexplained regression for the same workload.

Set numeric thresholds with product, engineering and performance owners based on the baseline and user expectations. Do not invent a universal launch-time target and present it as an industry requirement.

## Confidentiality

Share only approved and redacted evidence. Remove tokens, personal data, private endpoints and sensitive request/response payloads from logs and screenshots before attaching them to a defect or portfolio.
