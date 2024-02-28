## Sublinear Bonding

The first minipool(s) require a higher bond from a new Node Operator than subsequent minipools on the same Node.

### Proposals:

#### 1. First two minipools are LEB4’s, thereafter allow LEB1.5's

- Source: Valdorff's [bond_curves](https://github.com/Valdorff/rp-thoughts/blob/2024-02_strategy/2023_11_rapid_research_incubator/bond_curves.md)
- Summary:
  - First 2 minipools must be LEB4s
  - Thereafter allow LEB1.5s
  - Ends up with 0.5 ETH more of penalizable bond beyond grief slash budget
  - Allows for users to join with as little as 4 ETH
    - Note that a single LEB4 is around "13% value loss" with the worst case assumptions
    - Essentially we're saying "we value letting small players join and are willing to pay a cost for it." That said, the cost is pretty minimal. Large players _will not_ use single LEB4s to steal. The capital efficiency of more LEB1.5s will outweigh the theft advantage.i

### Required Support:

- [Forced Exits](/Proposals/ForcedExits.md)
  - The 1.5ETH bond must be recoverable by Rocket Pool in order to protect against loss scenarios associated with MEV theft and abandonment.

### Recommended Support:

- [rETH Protection](/Proposals/rETHprotection.md)
  - As we increase leverage by allowing 1.5LEBs with sublinear bonding, it becomes more critical to protect rETH from underperforming NO's.
- [Universal Variable Commission](/Proposals/UniversalVariableCommission.md)
  - Commission becomes a higher portion of Node Operator revenue with sublinear bonding. It becomes important then for Rocket Pool to have the ability to tweak commission variables over time since opt-in upgrades may not be enough to incentivize Node Operators to migrate away from their fixed commission into minipools with variable commission.
