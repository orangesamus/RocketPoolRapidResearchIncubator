In the Variables to consider section, there were multiple Distribution Strategy examples listed. Some plots are included here to help visualize rough examples of the distribution strategies originally discussed as 3.1 through 3.4. Valdorff’s “Direct Capture” proposal [linked here](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture2.md) (black line) would be analogous to 3.4: allowing yield for those under 10%. In practice the introduction of EthOnly pools can also allow Node Operators to spin up a combination of EthOnly pools and RPL staked pools to get a yield similar to the red dashed line.

![DistributionStrategiesVisualized](/plots/DistributionStrategiesVisualized.png)

## Variables to consider:
1. Commission variables:
    1. Commission A (Commission paid to EO MPs. Example: match Lido CSM to be 7.5%)
    1. Commission B (Remaining commission, to be diverted to RS MPs. Example: 6.5%)
    1. Total C = A + B, where C could stay the same as existing LEB8 commission of 14%
    1. Optional: Commissions variables above could be made flexible/dynamic
1. Eligibility to Receive B
    1. This could be left at RPL >10% borrowed Eth, same eligibility as RPL inflation yield
    1. Or it could apply to all RS who met >10% borrowed Eth when launching
1. Distribution strategy examples (how much of B is paid to each RS NO)
    1. Follow smoothie pool methodology, considering total attestations
    1. Follow RPL inflation rewards method from pre RPIP-30 which scales linearly, rewarding those with the most RPL (up to 150%)
    1. Follow RPL inflation rewards curve post RPIP-30 which depends on RPL collateral percentages but incentivizes being closer to 10%
    1. A new curve/equation could be used, especially if eligibility criteria is chosen from 2b above. RS MPs under 10% could still receive some B yield
    1. Optional: B could be converted to RPL before being paid to RS NO.
    1. Optional: Portions of B could also be diverted to the protocol, replacing RPL inflation
1. Governance eligibility of EO NOs
    1. Not a critical point to discuss here but could be decided to be 0 eligibility for example.
    1. In some ways they are passing governance to RS NO, as RS NO will likely convert portions of B yield to RPL, increasing their voting power
