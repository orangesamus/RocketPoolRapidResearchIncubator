## Forced Exits:

### Proposals:

#### 1. Exit a validator when a NO's (total_leakage + debt) > 0.5 ETH

- Source: Valdorff's [cohesive proposal](https://github.com/Valdorff/rp-thoughts/blob/2024-02_strategy/2024_02_strategy/readme.md)
- Summary:
  - Exit a validator when a NO's (total_leakage + debt) >0.5 ETH; this is about enough for ~3 months covering leakage and debt to rETH at 4% apy: 32*.04*(6/12)\*1.645 = .526 ETH
    - The debt variable could be used for underperformance penalties from [rETH Protection](/Proposals/rETHprotection.md), as well as MEV penalties
    - Note that we can kick one minipool at a time here, which yields at least ~1.5 ETH credit.

### Required Support:

- [EIP7002: Execution Layer Triggerable Exits](https://eips.ethereum.org/EIPS/eip-7002)
  - This EIP allows the execution layer to request an exit from the Ethereum withdrawal address of a validator. For us that's the minipool/megapool contract.
  - The 1.5ETH bond must be recoverable by Rocket Pool in order to protect against loss scenarios associated with MEV theft and abandonment.
