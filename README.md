## Rapid Research Incubator

This Repository contains my original "Commission Cut" proposal submitted for the [Rapid Research Incubator](https://dao.rocketpool.net/t/options-forum-thread/), and also my "Cohesive" proposal that pulls from several Rapid Research Incubator submission ideas with some modifications as a follow up to [Next Steps](https://dao.rocketpool.net/t/rapid-research-review-next-steps/2709).

### Cohesive Proposal Summary

Combine ideas from 4 categories of submissions:

1. Bond Reduction through sublinear bonding
1. Commission Cut diverted to RPL stakers
1. Universal Variable Commission
1. Protect rETH from underperforming Node Operators

The full proposal can be found here: [CohesiveProposal](/CohesiveProposal.md)

### Commission Cut Proposal Summary

The summary of this idea is to introduce Eth only minipools, where a portion of their
rewards are diverted to RPL staked minipools.

As a simple example, start by offering new node operators the same product as Lido’s CSM: (4E bond, and 7.5% commission on the other 28E). For an rETH holder, the commission could remain at 14%, leaving 6.5% on the 28E per minipool to be diverted to RPL staked minipools.

Start by reading the proposal submission here: [initialProposalSubmission.md](/initialProposalSubmission.md). The first distribution strategy (smoothie pool methodology) was explored more thoroughly with conclusions and calculations found here:
[calculationsAndConclusions.md](/calculationsAndConclusions.md)

### Files

- [CohesiveProposal](/CohesiveProposal.md) is my suggested proposal for next steps that pulls from several Rapid Research Incubator submission ideas with some modifications
- [initialProposalSubmission.md](/initialProposalSubmission.md) is the initial written proposal submission that summarizes and brainstorms the ideas from a high level. [DistributionStrategies.md](/DistributionStrategies.md) is a minor follow up to help visualize example distribution strategies for the diverted yield to RPL staked minipools.
- [YieldComparisons.xlsx](/YieldComparisons.xlsx) includes some initial calculations done to compare the yields and commissions of solutions under various scenarios. Google sheets version can also be found [here](https://docs.google.com/spreadsheets/d/12Q7qeI4TS-vMcviZIDuIwXO0p1UF5GUh/edit#gid=1728151719)
- [RCM_plotter.py](/RCM_plotter.py) is a script to plot out the scenarios for better visualization of the possibilities
- [calculationsAndConclusions.md](/calculationsAndConclusions.md) explains how the script is setup and provides examples with analysis/conclusions
- [plots](/plots/) includes example plots referenced in [calculationsAndConclusions.md](/calculationsAndConclusions.md)
