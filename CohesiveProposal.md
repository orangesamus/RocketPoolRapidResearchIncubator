## Cohesive Proposal

Combine ideas from 4 categories of submissions:

1. Bond Reduction through sublinear bonding
1. RPL Value Capture
1. Universal Variable Commission
1. rETH Protection from underperforming Node Operators

Where 1 and 2 are the top priorities, but 1 should be accompanied with 4, and 2 should be accompanied with 3.

### 1. Bond Reduction

#### Summary:

Defer to Valdorff’s recommendations here, using `Aggressive [alt]` from [bond_curves](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/bond_curves.md) (First two minipools are LEB4’s, thereafter allow LEB1.5s).

### 2. RPL Value Capture:

#### Summary:

Rocket Pool will remove the minimum RPL Bond requirement to allow Eth Only Node Operators. The Node Operators who desire less RPL speculation can still join, they just give up some of their commission to those who do stake RPL (this is how RPL captures value). All Node Operators earn a base commission, and Node Operators who also stake RPL can earn a bonus commission. Some remaining commission will also be deposited to a "Commission Pot" to be distributed to all RPL Stakers (including pure RPL Stakers who do not run a node).

A simple example would be keep the total rETH Commission Fee at 14%, give 6% as Base Commission to all Node Operators, give up to 7% as Bonus Commission to Node Operators who stake RPL, and guarantee 1% to the Commission Pot to distribute to all RPL Stakers.

In Summary:

- Individuals will be free to stake only ETH, only RPL, or any combination of the two.
- Staking RPL unlocks access to the Commission Pot of ETH revenue
  - The Commission Pot grows with rETH TVL, this means as rETH TVL grows, the value of RPL should grow along with it.
- Node Operation unlocks a base commission of ETH, and access to RPL inflation
- Node Operators who also stake RPL unlock a bonus commission of Eth
- **Instead of 10% RPL Bond being the "minimum bond" requirement, it becomes the "max bonus"**. See examples below:
  - Don't like RPL and want to do Eth Only? No problem, you still get base commission
  - Your RPL bond falls to 9%? No problem, you still get base commission + 90% of your potential bonus commission

#### Implementation:

Mostly building off of [commission_cut](/initialProposalSubmission.md) and Valdorff's [direct_capture](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture.md) with 4 main modifications:

1. Change distribution of RPL from RPL Inflation to scale linearly with Node Operator Borrowed Eth, see **"RPL Inflation Distribution"** below
1. Change distribution of ETH from Commission Pot to scale linearly with Staked RPL, see **"Commission Pot Distribution"** below

| RPL Inflation Distribution                             | Commission Pot Distribution                                    |
| ------------------------------------------------------ | -------------------------------------------------------------- |
| ![RPLinflationRewards](/plots/RPLinflationRewards.png) | ![EthCommissionCutRewards](/plots/EthCommissionCutRewards.png) |

<br/>

3. Introduce "Base Commission" and "Bonus Commission" for Node Operators. "Base Commission" is paid to all Node Operators, while "Bonus Commission" eligibility is determined by RPL staked on a Node, with max bonus eligibility being a Staked RPL value equivalent to 10% borrowed Eth. See Bonus Commission Eligibility below ("NO" is an abbreviation for "Node Operator"):

![BonusCommissionEligibility](/plots/BonusCommissionEligibility.png)

<br/>

4. Actual commission variables can be set as determined by [Universal Variable Commission](#3-universal-variable-commission) section

#### Visualizing the Implementation:

Total Protocol Revenue Streams are visualized below:

![RevenueStreams](/plots/RevenueStreams.png)

<br/>

To understand the dynamics of the Eth Revenue Stream, take 4 example participants in order of most to least RPL bullishness.

1. Pure RPL Staker (Not Operating a Node)
2. Node Operator A, fully RPL collateralized, earning all of the potential bonus commission
3. Node Operator B, partially RPL collateralized, earning half of the potential bonus commission
4. Node Operator C, no RPL staked (Eth Only), earning no bonus commission

The Eth Revenue would be distributed as shown below:
![BorrowedEthRevenue](/plots/BorrowedEthRevenue.png)

#### Reason for the modifications:

- Traditionally Rocket Pool has married RPL speculation with Node Operation, and has constrained target profitability to be a narrow window:
  - Requiring a minimum RPL bond of 10% borrowed ETH
  - Max effective RPL stake at 150% bonded ETH
  - Recently optimized even more narrowly for an RPL bond of 10-15% borrowed ETH with RPIP30.
- This proposal provides a path to decoupling RPL speculation from Node Operation and support the maximum number of participants in Rocket Pool. This is accomplished by:
  - Opening the market to RPL skeptics (allowing Eth Only Node Operators, and linearly increasing bonus commission for Node Operators with Staked RPL collaterals values equivalent to 0-10% borrowed ETH).
  - We also open the market to a wider range of RPL speculators by allowing pure RPL staking
- The changes to the RPL Inflation Revenue Distribution introduces the "Rocket Pool Node Operator Flywheel" shown below:

![RocketPoolNOflywheel](/plots/RocketPoolNOflywheel.png)

<br/>

### 3. Universal Variable Commission

#### Summary:

All new minipools require Universal Variable Commission, meaning the commission variables can be universally changed by the protocol (instead of historically where each minipool had its own fixed commission).

Rocket Pool has established itself as an Ethereum Aligned Protocol (See [RPIP17](https://github.com/rocket-pool/RPIPs/blob/main/RPIPs/RPIP-17.md), which the pDAO voted for with a passing vote of ~99.55% - see [results](https://snapshot.org/#/rocketpool-dao.eth/proposal/0x9e093dea49dee9d1b3e43dbb6e0d8735149c5fde6ef703620970129b81d0f7f8)). RPIP17 laid out a vision to soft limit at 16% market share, and hard limit at 22% market share in order to act in the best interest of Ethereum Health. Here is where we can put our money where our mouth is.

With the implementation presented in the [RPL Value Capture](#2-rpl-value-capture) section, we have 3 major commission knobs to control to achieve our end goal:

1. Total rETH Commission Fee
2. Node Operator Base Commission
3. RPL Value Capture (distribution depends on staked RPL)
   - 3a. Node Operator Bonus Commission
   - 3b. RPL Commission Pot

_Our end goal is that eventually there should be an equilbrium established by the market for:_

1. _The ideal total fee that rETH charges such that people are still willing to hold rETH_
2. _The ideal commission a Node Operator will take at our "soft limit" market share_
3. _And the rest (Total Fee - Node Operator Commission) can be captured by RPL_

With that in mind, we explore how these commission variables will be set.

#### Starting Point

There are 2 primary "manual inputs" to play with. The first manual input would be knob 1 (Total rETH Commission Fee). The second primary manual input would be knob 2 (Node Operator Base Commission). Knob 3 (RPL Value Capture) can capture whatever commission is left ("knob 1 - knob 2").

1. We can start by leaving total rETH commission fee at **14%** as the market has shown ample demand for this fee, and it is still relatively competitive to other LST's.
2. For Node Operator Base Commission, we can start by choosing **7%**. According to [calculationsAndConclusions](/calculationsAndConclusions.md) and [YieldComparisons](/YieldComparisons.xlsx), a base commission of 7% would be ~1.5x more profitable than solo staking for LEB4's (from bonded ETH yield + base commission alone). For reference, Lido's CSM suggested a setup that provided 1.5x more profitability than solo staking.
   - Note that this does not account for sublinear bonding, which could allow the number 7% listed above to be smaller and still more profitable due to increased commission
3. That leaves **7%** to be allocated between the Node Operator Bonus Commission or the RPL Commission Pot. This means a fully RPL collateralized Node could earn 7% bonus commission, and an Eth Only Node Operator would earn 0% bonus commission.
   - For Eth Only Node Operators, or Nodes with RPL collateral values equivalent to less than 10% borrowed Eth, the remaining commission goes to the Commission Pot to be distributed to RPL stakers.

#### Market Share Based Variable Adjustment:

UVC can now be used to enable market share based controls for the commission knobs. You can play with the numbers yourself with your own copy of [MarketShareBasedVariableCommissions.xlsx](/MarketShareBasedVariableCommissions.xlsx)

**Node Operator Commissions to enforce Hard Limit:**

Knobs 2 and 3a (Node Operator Base and Bonus Commissions) can be determined by decreasing linearly from 0% market share to 22% (our "hard-limit" market share). This can be demonstrated with examples below:

- If Rocket Pool had a market share of 0%, then the Commissions would look like:
  - Base Commission = **7%**
  - Bonus Commission = **7%**
  - RPL Commission Pot is guaranteed **0%**
  - Total rETH Commission Fee = **14%** = 7% + 7% + 0%
- If Rocket Pool reaches its soft limit market share (16%) then the Commissions would look like:
  - Base Commission = **1.9%**
  - Bonus Commission = **3.3%**
  - RPL Commission Pot is guaranteed **8.8%**
  - Total rETH Commission Fee = **14%** = 1.9% + 3.3% + 8.8%
- If Rocket Pool reaches it's hard limit market share of 22%, then the Base and Bonus Commissions would each equal 0%
  - Base Commission = **0%**
  - Bonus Commission = **0%**
  - RPL Commission Pot is guaranteed **14%**
  - Total rETH Commission Fee = **14%** = 0% + 0% + 14%

See math below for example calculations with market share at soft limit (16%):

<details>
  <summary>Example Calculations</summary>
  Base Commission:
  
  ```math
  \displaylines{
    Actual Base = PotentialBase - \frac{MarketShare}{HardLimit\%}*PotentialBase \\
    Actual Base = 7\% - \frac{16\%}{22\%}*(7\%) = 1.9\%
  }
  ```
  
  <br/>
  
  Bonus Commission:
  
  ```math
  \displaylines{
    PotentialBonus = Total \,\, rETH Commission Fee - Node Operator Base Commission \\
    ActualBonus = PotentialBonus - \frac{MarketShare}{HardLimit\%}*PotentialBonus \\
    ActualBonus = (14\%-1.9\%) - \frac{16\%}{22\%}*(14-1.9\%) = 3.3\%
  }
  ```
  
  <br/>
  
  This means with Rocket Pool at its soft limit of 16% market share, the Total Potential Node Operator Commission would be 5.2%, and 8.8% of all rETH commission would be guaranteed to the RPLCommissionPot as shown by the math below:
  
  ```math
  \displaylines{
    TotalPotentialNOCommission = NO Base Commission + NO Bonus Commission \\
    TotalPotentialNOCommission = 1.9\% + 3.3\% = 5.2\% \\
    GuaranteedRPLCommissionPot = Total \,\, rETHCommissionFee - TotalPotentialNOCommission \\
    GuaranteedRPLCommissionPot = 14\% - 5.2\% = 8.8\%
  }
  ```
</details>

<br/>

**Total rETH Commission Fee to enforce Soft Limit:**

To enforce the "soft limit" market share, knob 1 (total rETH Commission Fee) can be set to linearly increase from the soft-limit to the hard-limit market share values to make rETH increasingly less attractive. This can be demonstrated with examples below:

- If Rocket Pool has not reached its soft limit market share and is still in "growth mode" (market share ranging from 0-16%). The total rETH Commission Fee will remain at it's manual input target (say 14%).
- If Rocket Pool is at "maturity" (market share ranging from 16% to 22%), the total rETH Commission Fee will be somewhere between it's manual input target (say 14%) and 100%. As an example, if Rocket Pool reached a market share of 20%, it would then charge rETH holders a 71.33% commission fee. That would leave only 28.67% of the ETH revenue to go to rETH holders. This should make rETH less attractive relative to other LST's and allow rETH to balance back to its target market share at the soft limit.
- If Rocket Pool reaches its hard limit market share of 22%, the total rETH Commission Fee will be 100% (meaning no ETH revenue goes to rETH holders, which removes incentives to hold rETH).

See math below for example calculations with market share above soft limit (at 20%):

<details>
  <summary>Example Calculations</summary>
  
  <br/>

```math
\displaylines{
  TotalrETHFee = TargetFee + (100\%-TargetFee)*\frac{MarketShare - SoftLimit}{HardLimit - SoftLimit} \\
  TotalrETHFee = 14\% + (100\%-14\%)*\frac{20\% - 16\%}{22\% - 16\%} \\
  TotalrETHFee = 71.33\%
}
```

</details>

**Stagnation and Intervention:**

If Rocket Pool is in growth mode (market share 0% to 16%), and growth stagnates due to improper "manual input" starting values, "manual intervention" could be done to incentivize growth:

1. If there is excess rETH demand we should not increase Target total rETH Commission Fee, but instead increase Base Commission to NO's to meet rETH demand (effectively squeezing the RPL Value Capture knob, and instead incentivizing Node Operators to meet the demand)
2. If rETH demand dries up, we can decrease the total rETH Commission Fee to make rETH more attractive, and leave Base Commission alone (effectively squeezing the RPL Value Capture knob, and instead giving it to rETH holders)

The two adjustments described above could be done with a manual vote, or growth could be quantified and automated based on market share/time, or deposit pool status, etc. Similar intervention could be done at "maturity", but at that stage we are targeting the Soft Limit instead of growth.

#### RPL Inflation:

Lastly, RPL inflation could be treated in a similar same way:

- Scale down linearly from 5% to 0%, based off market share from 0% to Soft Limit (say 16%) in a similar manner described previously.
- At maturity, as Rocket Pool approaches its Soft Limit (say 16%) for market share, the oDAO and pDAO treasury could be paid with a very small percentage of ETH revenue from the Commission Pot. This could also be scaled up linearly to the necessary amount to smoothly transition away from RPL Inflation.

<br/>

### 4. rETH Protection from underperforming Node Operators

**Introducing Credit Collateral:**

As we increase leverage by allowing 1.5LEBs with sublinear bonding, it becomes more critical to protect rETH from NO issues. One way this can be accomplished is by allowing Node Operators to add ETH "credit" to their node balance in addition their ETH that is "staked" as bonds for minipools. The "credit" is not earning yield or commission since it isn't staked on the beacon chain or contributing to rETH supply, but it can act as a buffer of collateral to protect rETH from underperformance, and protect a Node Operator from being ejected by Rocket Pool for having too low of an Eth Bond.

One simple example is that this "credit" can be continuously added to from the Eth rewards and Commission from running minipools.

To calculate an example, pretend you were a solo staking Node Operator, and you approach Rocket Pool 32ETH. With sublinear bonding, you create 2 LEB4 minipools and 16 LEB1.5 minipools. The total base case yield (ignoring RPL staking and Bonus Commission) you would earn in a year can be calculated with the equation belows

```math
MinipoolYield = SoloStakingAPR*EthBond + SoloStakingAPR*(32-EthBond)*(BaseCommission)
```

If we say SoloStakingAPR is 3%, and BaseCommission = 7%, your total yield comes out to:

```math
\displaylines{
LEB4 = 0.03*4 + 0.03*28*0.07 \\
LEB1.5 = 0.03*1.5 + 0.03*30.5*0.07 \\
Total = 2*LEB4 + 16*LEB1.5 = 2.1 Eth
}
```

This means if you start with 32 Eth, even as an Eth Only Node Operator, roughly once every 9 months you can compound your stake by using your rewards to create an additional 1.5LEB minipool.

In this scenario, you could choose to "auto-credit" your rewards, where your rewards get sent to your "credit" balance, and once your "credit" balance exceeds 1.5ETH you can use your "credit" to create an additional LEB1.5 minipool.

<br/>

**Protecting rETH:**

Here is where rETH protection also comes in: Building off ArtDemocrat’s research with some modifications (some context found [here](https://dao.rocketpool.net/t/rapid-research-incubator-submission-reth-protection-through-rpl-rerouting-deflation/2599/4?u=samus)):

- No RPL burn

Ways to penalize underperforming NO’s and make rETH whole (in the order shown below):

1. Take from their ETH Credit
1. Take from their ETH Bond

With the description shown above, Node Operators can essentially "deleverage" some of their stake while retaining the commission cuts they earn from LEB1.5's. This "credit" balance could even be flexible to be used as shared security in other systems like EigenLayer (Shoutout to Jasper's [Rocket Layer Bounty](https://dao.rocketpool.net/t/round-8-gmc-call-for-bounty-applications-deadline-is-january-14/2558/2?u=samus) / [Hybrid Theory Article](https://mirror.xyz/jasperthefriendlyghost.eth/Xv7lLt8SVTfCaFnVie50IvvFrI4-TkQTgZcxb_omEnA)), and further buffer the already leveraged 1.5ETH Bond that is at stake for each minipool.

Rocket Pool has already implemented a simple version of a "credit" balance which was used in the most recent "Atlas" upgrade to assist Node Operators with converting their EB16's to LEB8's. This "credit" balance mechanism could be reused for LEB8 conversions to sublinear bonding, while also functioning as an additional layer of collateral should a Node Operator choose to somewhat deleverage their bonds at stake.

### Acknowledgments

Discussions with Knoshua/Valdorff helped shaped some of the ideas under the Commission Pot section, Epineph has helpful additional thoughts on mechanics to implement changes in UVC [here](https://dao.rocketpool.net/t/options-forum-thread/2515/7).
