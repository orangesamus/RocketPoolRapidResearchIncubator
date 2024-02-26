## RPL Inflation Rework:

### Present Day State:

- Total RPL Inflation is at 5%
- 1.5% out of 5% (30%) goes to funding the pDAO and oDAO (we'll call this "DAO RPL Inflation")
- 3.5% out of 5% (70%) goes to NO's (we'll call this "NO RPL Inflation")
  - Distribution is calculated according to [RPIP30](https://rpips.rocketpool.net/RPIPs/RPIP-30) as described below:
    - If your staked RPL value in ETH is below 10% borrowed ETH, weight is 0
    - From 10%-15% borrowed ETH, weight is linear with the amount of borrowed ETH
      - 🧮 `weight = 100 * staked_rpl_value_in_eth`
    - Above 15%, weight follows a logarithmic curve, rising forever, but ever-more-slowly
      - 🧮 `weight = (13.6137 + 2 * ln(100 * (staked_rpl_value_in_eth / borrowed_eth) - 13)) * borrowed_eth`
    - The NO share of inflation gets split up to each node as `weight/total_summed_weight`

### Proposals:

#### 1. Change RPL Inflation to NO's to distribute by Borrowed ETH

- Source: Samus' [Cohesive Proposal](https://github.com/orangesamus/RocketPoolRapidResearchIncubator/blob/main/CohesiveProposal.md)
- Summary:
  - Change distribution of "NO RPL Inflation" to scale linearly with Node Operator Borrowed Eth. Rewards would be distributed to all NO's as calculated by `(your Borrowed ETH)/(total Protocol Borrowed ETH)`
  - Scale down "NO RPL Inflation" linearly from present value (3.5%) to 0% as rETH market share grows from present day to it's soft-limits goal (soft-limit described in [RPIP17: Self-Limiting Rocket Pool](https://rpips.rocketpool.net/RPIPs/RPIP-17)).
  - This gives Node Operators an additional source of revenue related to RPL price. Node Operators can benefit from RPL price appreciation even if they start out as ETH-Only.
  - This gives Node Operators a chance to "earn" access to governance over time without having to pay for it.

#### 2. Remove RPL Inflation to NO's

- Source: Valdorff's [Cohesive Proposal](https://github.com/Valdorff/rp-thoughts/blob/2024-02_strategy/2024_02_strategy/readme_tier3.md)
- Summary:
  - Set "NO RPL Inflation" to 0% ending all RPL rewards to NO's.
  - In this structure, we don't need to use RPL inflation to get more people staking RPL to meet rETH demand. Insofar as folks have unstaked, they're at least doing a service to RPL stakers by giving up their share. If they're doing something like LPing, then they're further serving RP.

#### 3. Remove RPL Inflation to oDAO & pDAO and replace with ETH commission

- Source: Samus' [Cohesive Proposal](https://github.com/orangesamus/RocketPoolRapidResearchIncubator/blob/main/CohesiveProposal.md)
- Summary:
  - Scale down "DAO RPL Inflation" linearly from present value (1.5%) to 0% as rETH market share grows from present day to it's soft-limits goal (soft-limit described in [RPIP17: Self-Limiting Rocket Pool](https://rpips.rocketpool.net/RPIPs/RPIP-17))
  - As rETH TVL grows, the amount of revenue generated from commission becomes large enough that a slice of commission could be used to fund the pDAO and oDAO.
  - During the transition period the pDAO and oDAO would have a blend of funding from both ETH commission and RPL inflation.
