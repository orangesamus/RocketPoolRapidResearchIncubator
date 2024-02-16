## Cohesive Proposal

Combine ideas from 4 categories of submissions:

1. Bond Reduction through sublinear bonding
1. Commission Cut Pot diverted to RPL stakers
1. Universal Variable Commission
1. Protect rETH from underperforming Node Operators

### 1. Bond Reduction

Defer to Valdorff’s recommendations here, using `Aggressive [alt]` from [bond_curves](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/bond_curves.md) (First two minipools are LEB4’s, thereafter allow LEB1.5s).

### 2. Commission Cut:

Mostly building off of [commission_cut](/initialProposalSubmission.md) and Valdorff's [direct_capture](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture.md) with some modifications:

- Change RPL Inflation revenue distribution to scale linearly with Node Operator Borrowed Eth, see **RPL Inflation** below
- Change ETH Commission Cut Pot revenue distribution to scale linearly with Staked RPL, see **ETH Commission Cut Pot** below

| RPL Inflation                                          | ETH Commission Cut Pot                                         |
| ------------------------------------------------------ | -------------------------------------------------------------- |
| ![RPLinflationRewards](/plots/RPLinflationRewards.png) | ![EthCommissionCutRewards](/plots/EthCommissionCutRewards.png) |

<br/>

- Introduce "Base Commission" and "Bonus Commission" for Node Operators. "Base Commission" is paid to all Node Operators, while "Bonus Commission" eligibility is determined by RPL staked on a Node, with max bonus being a Staked RPL value equivalent to 10% borrowed Eth. See Bonus Commission Eligibility below ("NO" is an abbreviation for "Node Operator"):

![BonusCommissionEligibility](/plots/BonusCommissionEligibility.png)

<br/>

Total Protocol Revenue Streams are visualized below:

![RevenueStreams](/plots/RevenueStreams.png)

<br/>

To understand the dynamics of the Eth Revenue Stream, take 4 example participants in order of most to least RPL bullishness.

1. Pure RPL Staker (Not Operating a Node)
1. Node Operator A, fully RPL collateralized, earning all of the potential bonus commission
1. Node Operator B, partially RPL collateralized, earning half of the potential bonus commission
1. Node Operator C, no RPL staked (Eth Only), earning no bonus commission

The Eth Revenue would be distributed as shown below:
![BorrowedEthRevenue](/plots/BorrowedEthRevenue.png)

<br/>

**Reason for the modifications:**

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

**Summary:**

- Individuals will be free to stake only ETH, only RPL, or any combination of the two.
- Staking RPL unlocks access to the commission cut pot of Eth
- Node Operation unlocks a base commission of Eth, and access to RPL inflation
- Node Operators who also stake RPL unlock a bonus commission of Eth
- Instead of 10% RPL Bond being the "minimum bond" requirement, it becomes the "max bonus". Examples:
  - Your RPL collateral falls to 9%? No problem, you just get base commission + 90% of your potential bonus commission
  - Don't like RPL and want to do Eth Only? No problem, you still get base commission

<br/>

### 3. Universal Variable Commission

All new minipools are UVC. There are 3 major commission cut knobs to control:

1. Total rETH Commission Fee
1. Node Operator Base Commission
1. Node Operator Max Bonus Commission

- In general, we can start by leaving the total rETH commission fee at **14%**
- All Node Operators receive a base commission. According to [calculationsAndConclusions](/calculationsAndConclusions.md) and [YieldComparisons](/YieldComparisons.xlsx), a base commission of **7%** would be ~1.5x more profitable than solo staking (from bonded ETH yield + base commission alone). For reference, Lido's CSM suggested a setup that provided 1.5x more profitability than solo staking.
- That leaves **7%** to be allocated between the Commission Cut Pot of ETH or Node Operator Bonus Commission. This means a fully RPL collateralized Node could earn 7% bonus commission, and an Eth Only Node Operator would earn 0% bonus commission.
  - For Eth Only Node Operators, or Nodes with RPL collateral values equivalent to less than 10% borrowed Eth, the remaining commission goes to the Commission Cut Pot to be distributed to RPL stakers.

If we started by applying this proposal to our existing set of Node Operators today, very little would change with commissions. Most Node Operators today are "fully RPL collateralized" since they all put up a 10% RPL bond as a minimum requirement when spinning up new minipools. This would mean they would mostly all earn the full bonus commission + the base commission, adding up to a total commission of 14% (the same as it is today).

The effects of the changes would begin to materialize as many Node Operators might not "top up" their RPL collateral, and instead opt to give up some commission to the Commission Cut Pot. We would also expect a wave of new Node Operators to join who vary on the spectrum of desire for RPL speculation, ranging from zero RPL (Eth-Only) to somewhere inbetween RPL bond values of 0-10% borrowed ETH. These new Node Operators would be providing substantial amounts of ETH to the Commission Cut Pot to then be distributed to RPL stakers (both pure RPL stakers and Node Operators with RPL collateral).

**Market Based Variable Adjustment:**

Rocket Pool has established itself as an Ethereum Aligned Protocol (See [RPIP17](https://github.com/rocket-pool/RPIPs/blob/main/RPIPs/RPIP-17.md), which the pDAO voted for with a passing vote of ~99.55% - see [results](https://snapshot.org/#/rocketpool-dao.eth/proposal/0x9e093dea49dee9d1b3e43dbb6e0d8735149c5fde6ef703620970129b81d0f7f8)), and here is where we can put our money where our mouth is. RPIP17 laid out a vision to soft limit at 22% market share, and hard limit at 33% market share in order to act in the best interest of Ethereum Health.

UVC can be used to assist with implementation of these limits by enabling market based controls for the commission cut knobs. Focusing on knobs 2 and 3:

1. Total rETH Commission Fee
1. Node Operator Base Commission
1. Node Operator Max Bonus Commission

First, knob 3 (Node Operator Max Bonus Commission) can be determined by an inversely propotional linear scale from 0% market share to 22% market share. This can be demonstrated with examples below:

- If Rocket Pool had a market share of 0%, then the Max Bonus Commission would equal 7% based on the previous example numbers. This is determined by:

```math
\displaylines{
  PotentialMaxBonus = Total rETH Commission Fee - Node Operator Base Commission \\
  ActualMaxBonus = PotentialMaxBonus - \frac{MarketShare}{22%}*PotentialMaxBonus \\
  ActualMaxBonus = (14%-7%) - \frac{0%}{22%}*(14-7%) = 7%
}
```

- If Rocket Pool reaches 22% market share (or more), then Max Bonus Commission would equal 0%.

```math
\displaylines{
  ActualMaxBonus = (14%-7%) - \frac{22%}{22%}*(14-7%) = 0%
}
```

Second, knob 2 (Node Operator Base Commission) can be determined by an inversely propotional linear scale from 0% market share to 33% market share. The math here would be similar:

- If Rocket Pool had a market share of 0%, then the Base Commission would equal 7% based on the previous example numbers. This is determined by:

```math
\displaylines{
  Actual Base = PotentialBase - \frac{MarketShare}{33%}*PotentialBase \\
  Actual Base = 7% - \frac{0%}{33%}*(7%) = 7%
}
```

- If Rocket Pool reaches a market share of 33%, then Base Commission would equal 0% based on the previous example numbers

```math
\displaylines{
  Actual Base = 7% - \frac{33%}{33%}*(7%) = 0%
}
```

### 4. Protect rETH from underperforming Node Operators

**Introducing Credit Collateral:**

As we increase leverage by allowing 1.5LEBs with sublinear bonding, it becomes more critical to protect rETH from NO issues. One way this can be accomplished is by allowing Node Operators to add ETH "credit" to their node balance in addition their ETH that is "staked" as bonds for minipools. The "credit" is not earning yield or commission since it isn't staked on the beacon chain or contributing to rETH supply, but it can act as a buffer of collateral to protect rETH from underperformance, and protect a Node Operator from being ejected by Rocket Pool for having too low of an Eth Bond.

One simple example is that this "credit" can be continuously added to from the Eth rewards and Commission from running minipools.

To calculate an example, pretend you were a solo staking Node Operator, and you approach Rocket Pool 32ETH. With sublinear bonding, you create 2 LEB4 minipools and 16 LEB1.5 minipools. The total base case yield (ignoring RPL staking) you would earn in a year can be calculated with the equation belows

```math
MinipoolYield = SoloStakingAPR*EthBond + SoloStakingAPR*(32-EthBond)*(AllNOCommissionCut)
```

If we say SoloStakingAPR is 3%, and AllNOCommissionCut = 4%, your total yield comes out to:

```math
\displaylines{
LEB4 = 0.03*4 + 0.03*28*0.04 \\
LEB1.5 = 0.03*1.5 + 0.03*30.5*0.04 \\
Total = 2*LEB4 + 16*LEB1.5 = 1.61 Eth
}
```

This means if you start with 32 Eth, even as an Eth Only Node Operator, roughly once a year you can compound your stake by using your rewards to create an additional 1.5LEB minipool.

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

Discussions with Knoshua/Valdorff helped shaped some of the ideas under the Commission Cut section, Epineph has helpful additional thoughts on mechanics to implement changes in UVC [here](https://dao.rocketpool.net/t/options-forum-thread/2515/7).
