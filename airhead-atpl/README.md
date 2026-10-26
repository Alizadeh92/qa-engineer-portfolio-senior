# Case Study: Airhead ATPL — Mobile, Web and Synchronization Testing

## Context

Airhead ATPL is a learning product used by aviation students to study ATPL material. The product experience spans mobile and web, and some study workflows need to remain useful when a connection is weak or unavailable.

My work on this product included manual testing across iOS, Android, web and desktop, checking content downloads and updates, investigating offline behaviour, and validating that data remained consistent after connectivity changed. I also helped coordinate testing work across a team of three QA engineers.

This document describes my testing approach without exposing internal architecture, private environments or customer data.

## Why this area needs careful testing

A screen can look correct while the underlying state is wrong. For example, a learner may see a downloaded subject but later find that some content is missing, or an action completed offline may not be reflected after reconnecting.

The main risks are:

- **Content integrity:** downloaded material is incomplete, duplicated or out of date.
- **State consistency:** progress or settings differ between local and server state.
- **Interrupted operations:** downloads or synchronization stop part-way through and do not recover cleanly.
- **Connectivity transitions:** the app does not recover correctly when switching between online, offline and unstable networks.
- **Platform differences:** the same workflow behaves differently on iOS, Android and web.
- **User feedback:** the interface shows success when an operation has not actually completed.

## Test approach

I start by mapping the key user journey, then identify state transitions and failure points. I pay particular attention to actions that can be repeated after a timeout or app restart.

1. Review requirements and clarify what should be available offline.
2. Identify the data that must persist locally and the events that require a server connection.
3. Cover normal, negative, boundary and recovery scenarios.
4. Test interruption and retry behaviour rather than only the happy path.
5. Compare visible behaviour across supported platforms and sessions.
6. Collect reproducible evidence and narrow down whether a failure appears to be UI-, network-, local-data- or server-related.
7. Retest the fix and run focused regression around adjacent workflows.

## Example risk-based coverage

| Area | Example risk | Test emphasis |
|---|---|---|
| Content download | Partial download is presented as complete | Interrupt download; inspect status and retry |
| Offline launch | Previously downloaded content is unavailable | Relaunch in airplane mode |
| Reconnection | Pending changes are lost or applied twice | Reconnect after offline actions; repeat sync |
| Content update | Old and new content are mixed | Update after an earlier download |
| App lifecycle | State is lost after backgrounding or restart | Repeat transitions at different operation stages |
| Cross-platform behaviour | Counts or progress differ by platform | Compare the same account and content state |

## What a useful defect report includes

A defect should make it possible for another person to reproduce the issue without a meeting. I include the build, platform, preconditions, exact steps, actual and expected results, reproducibility, and relevant screenshots, logs or network evidence. For synchronization defects, I also record the order of actions and connectivity changes.

## Collaboration and release thinking

When work is shared across QA engineers, I make the scope explicit, avoid duplicate coverage where possible, and review whether high-risk transitions are represented. Before release, I report what was tested, what remains unverified, the severity of open issues, and the impact on the learner. A test pass is evidence, not proof that a product has no defects.

## Scope note

This is a sanitised portfolio case study based on the product domain and responsibilities described in my professional experience. The detailed scenarios in this repository are demonstration artefacts; they are not claims that the example defects occurred in production.
