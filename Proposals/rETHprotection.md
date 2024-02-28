## rETH Protection:

Outlier underperforming NO's pay restitution to rETH to meet an adequate number (eg, overall rETH performance).

### Proposals:

#### 1. First take from NO ETH rewards, then mark any remaining unpaid restitution as NO debt

- Sources:
  - ArtDemocrat's [rETH Protection Proposal](https://dao.rocketpool.net/t/rapid-research-incubator-submission-reth-protection-through-rpl-rerouting-deflation/2599/3?u=samus)
  - Valdorff's [Cohesive Proposal](https://github.com/Valdorff/rp-thoughts/blob/2024-02_strategy/2024_02_strategy/with_voter_share/readme_tier3.md)
- Summary:
  - First restitution should be funded from ETH rewards flows
    - Per reward period: EL smoothie, RPL commission share -- both of these can be taken care of when making the merkl tree, so the underperformer never gains dominion over those funds
  - At this point, record any remaining unpaid restitution as debt, which can be repaid by:
    - EL fee distributor distribution -- anyone can do this
    - CL distribution -- anyone can do this
    - CL distribution during exit -- only owner can do this without a long wait.
      - Note that this exit can be a forced exit.
      - (Optional) Forced exit: if performing badly routinely -- kick.
        - Note that this optional point would require [Forced Exits](/Proposals/ForcedExits.md) to be implemented.
- Benefits:
  - Allow rETH to provide a more competitve APR
- Drawbacks: