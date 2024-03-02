## Forced Exits:

Enable Rocket Pool to kick a NO and access the NO's bond as needed.

### Proposals:

#### 1. Exit a validator when a NO's (total_leakage + debt) > 0.5 ETH

- Source: Valdorff's [Cohesive Proposal](https://github.com/Valdorff/rp-thoughts/blob/2024-02_strategy/2024_02_strategy/readme.md)
- Summary:
  - Exit a validator when a NO's (total_leakage + debt) >0.5 ETH; this is about enough for ~3 months covering leakage and debt to rETH at 4% apy: 32*.04*(6/12)\*1.645 = .526 ETH
    - The debt variable could be used for underperformance penalties from [rETH Protection](/Proposals/rETHprotection.md), as well as MEV penalties
    - Note that we can kick one minipool at a time here, which yields at least ~1.5 ETH credit.
    - Further notes on MEV penalties:
      - No vanilla blocks allowed
      - oDAO-applied penalty based on size of theft (largest bid across relays) plus a little bit (eg, 10%)
        - Note: no penalty for missing, just for using vanilla block or a non-allowed relay
      - Some trickiness around relay API timeliness - don't expect them to be quite realtime
        - If APIs are bad, we may need to remove them from allowlist
      - Security council should be able to remove penalties -- note they can be replaced by oDAO, so this is insufficient
      - pDAO guardian must remain in place to limit total penalties

### Required Support:

- [EIP7002: Execution Layer Triggerable Exits](https://eips.ethereum.org/EIPS/eip-7002)
  - This EIP allows the execution layer to request an exit from the Ethereum withdrawal address of a validator. For us that's the minipool/megapool contract.
  - The 1.5ETH bond must be recoverable by Rocket Pool in order to protect against loss scenarios associated with MEV theft and abandonment.