## Universal Variable Commission

Commission variables can be universally changed by the protocol instead of each minipool having its own fixed commission.

### Proposals:

#### 1. Allow markets to find equilibrium for total rETH LST fee, NO commission, and RPL value capture.
- Sources:
  - Samus' [Cohesive Proposal](https://github.com/orangesamus/RocketPoolRapidResearchIncubator/blob/main/CohesiveProposal.md)
- Summary:
  - Find an equilibrium for:
    - The ideal total fee that rETH charges such that people are still willing to hold rETH
    - The ideal commission a Node Operator will take at our "soft limit" market share (soft-limit described in [RPIP17: Self-Limiting Rocket Pool](https://rpips.rocketpool.net/RPIPs/RPIP-17)).
    - And the rest (Total Fee - Node Operator Commission) can be captured by RPL (this includes "voter share" in [RPL Value Capture](/Proposals/RPLValueCapture.md))
  - Starting point:
    - Start by keeping total rETH fee at 14%
    - Set a competitive NO commission (Sublinear Bonding example could be 5%)
    - The remainder (9%) as an example is captured by RPL
  - Expected changes:
    - As rETH approaches maturity (TVL grows to reach soft-limit goals), scale back NO commission (example could be 3%)
    - RPL captures whatever is left while rETH maintains a competitive fee
    - If rETH exceeds it's self-limits the total rETH commission fee can be increased to make rETH less attractive and bring it back down to the self-limit
  - Stagnation/intervention:
    - If there is excess rETH demand we should not increase total rETH Commission Fee, but instead increase Base Commission to NO's to meet rETH demand (effectively squeezing the RPL Value Capture share, and instead incentivizing Node Operators to meet the demand)
    - If rETH demand dries up, we can decrease the total rETH Commission Fee to make rETH more attractive, and leave Base Commission alone (effectively squeezing the RPL Value Capture knob, and instead giving it to rETH holders)