## RPL Value Capture

Change rETH commission to be split between NOs and RPL, allowing RPL to Capture Value from protocol revenue.

### Proposals

#### 1. Buy and Burn

- Source: Valdorff's [Cohesive Proposal](https://github.com/Valdorff/rp-thoughts/blob/2024-02_strategy/2024_02_strategy/with_voter_share/readme_tier2.md#rpl-buyburn)
- Summary:
  - A share of ETH from commission goes to a smart contract 
  - Users may call a function to swap RPL for the ETH in the above contract
  - Swap price is based on on-chain TWAP oracle
  - Any RPL swapped this way is burned by sending it to `0x000000000000000000000000000000000000dEaD`