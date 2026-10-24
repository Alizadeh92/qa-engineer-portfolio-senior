# Release Readiness Criteria — Sample

## Minimum evidence to consider
- [ ] Critical user journeys have been tested on the target build
- [ ] Smoke suite passes in the intended release environment
- [ ] High-risk changes have targeted regression evidence
- [ ] Fixed P0/P1 defects have been retested
- [ ] No unresolved P0 defect; P1 defects have an explicit product/engineering decision
- [ ] Known issues, workarounds, and residual risks are documented
- [ ] API/client compatibility and data migration concerns have been reviewed
- [ ] Monitoring, rollback, or recovery arrangements are understood where applicable

## Do not use as a mechanical gate
A checklist cannot replace risk judgement. A single severe data-integrity issue may outweigh a high pass rate. Any exception should name the decision owner, accepted risk, workaround, and follow-up plan.
