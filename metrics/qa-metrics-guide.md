# QA Metrics — How to Use Them Responsibly

Metrics should support decisions, not reward activity or conceal risk. Define each metric consistently before comparing teams or releases.

## Useful measures
- **Critical journey coverage:** critical user journeys with current test evidence / critical journeys identified.
- **Execution status:** passed, failed, blocked, and not-run counts for a defined test scope.
- **Defect aging:** time unresolved defects remain open, segmented by severity and ownership.
- **Escaped defects:** defects found after release, interpreted with severity and exposure.
- **Reopen rate:** reopened defects / defects closed in the same defined cohort.
- **Flaky test rate:** inconsistent outcomes under comparable conditions, with environment issues separated where possible.

## Caveats
- Test case count is not a reliable measure of quality by itself.
- Pass rate can hide untested critical paths and blocked tests.
- Defect counts depend on usage, reporting practices, and discovery effort.
- Avoid using individual defect counts to rank engineers.
- State the period, denominator, exclusions, and data source for every metric.

## Example dashboard definition
For each release, report the test scope and build, critical journey coverage, execution status, open P0/P1 defects, known limitations, and release recommendation with decision owner.
