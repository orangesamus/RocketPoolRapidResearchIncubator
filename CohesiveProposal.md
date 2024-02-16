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

- Introduce "Base Commission" and "Bonus Commission" for Node Operators. "Base Commission" is paid to all Node Operators, while "Bonus Commission" eligibility is determined by RPL staked on a Node, with max bonus being a Staked RPL value equivalent to 10% borrowed Eth. See Bonus Commission Eligibility below:

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

1. “All NO’s”
1. “NO Staked RPL”
1. “All Staked RPL”

In general, we can start by leaving the rETH total commission cut fee (1+2+3) at **14%**:

- 1 (All NO’s) should have a fixed floor value to ensure base case profitability, even if you are an Eth Only Node Operator. For a simple example let’s call it **4%**.
- 3 (All Staked RPL) should have a fixed floor value to ensure base case profitability, even if you are a pure RPL staker. For a simple example let’s call it **1%**.
- 2 (NO Staked RPL) that leaves **9%** as the max amount that could go to NO Staked RPL.

If we start with the numbers above, we are not all that different from today. All NO’s today are RPL staked NO's, and all staked RPL today is staked by NO's. That means all existing NO's would have access to all 3 categories of commission cuts. We are opening two new markets with restricted commission cuts (RPL only staking, and ETH only staking), and providing RPL Staked NO's with exclusive access to most of the commission cut (9%).

Following the example numbers listed above: All Node Operators will earn 4% commisison, and the remaining 10% commission goes to a commission cut pot to be split among RPL stakers where each RPL staker can calculate their share with an example equation below:

```math
\displaylines{
StakedRPLCommissionCut = ax + by \\
a = \frac{AllStakedRPLCommissionCut}{AllStakedRPLCommissionCut+NOStakedRPLCommissionCut} \\
b = \frac{NOStakedRPLCommisisonCut}{AllStakedRPLCommissionCut+NOStakedRPLCommissionCut} \\
x = Individual \,\, AllStakedRPL \,\, Weighting \\
y = Individual \,\, NOStakedRPL \,\, Weighting
}
```

With the example of 1% commission cut to AllStakedRPL, and 9% commission cut to NOStakedRPL:

```math
\displaylines{
a = \frac{1\%}{1\%+9\%} = 0.1 \\
b = \frac{9\%}{1\%+9\%} = 0.9 \\
StakedRPLCommissionCut = 0.1x + 0.9y
}
```

To see some example calculations check the collapsable section below:

<details>
  <summary>Example Calculations</summary>
  
  If you are a pure RPL staker with x RPL to stake, you would only earn from "AllStakedRPL" commission cut since "NOStakedRPL" commission cut depends on borrowed Eth and is therefore only eligble to NO's, (y variable = 0). You would earn:
  
  ```math
  0.1*\frac{x}{Total RPL Stake Supply}
  ```
  
  If you are a NO with x RPL at stake, leading to an RPL collateral equivalent to 12% borrowed ETH, following the rewards curve from DirectCapture2 you would earn:
  
  ```math
  0.1* \frac{x}{Total RPL Stake Supply} + 0.9*\frac{1*MiniPoolCount}{TotalWeightOfNOStakedRPL}
  ```
  
  If you only had an RPL collateral equivalent of 6% borrowed Eth, you would earn:
  
  ```math
  0.1* \frac{x}{Total RPL Stake Supply} + 0.9*\frac{0.5*MiniPoolCount}{TotalWeightOfNOStakedRPL}
  ```
  
  If you are a NO with x RPL at stake, leading to an RPL collateral equivalent to 15% borrowed ETH, following the rewards curve from DirectCapture2 you would earn:
  
  ```math
  0.1* \frac{x}{Total RPL Stake Supply} + 0.9*\frac{1.2*MiniPoolCount}{TotalWeightOfNOStakedRPL}
  ```
  
  If you are a NO with x RPL at stake, leading to an RPL collateral equivalent to 100% borrowed ETH, following the rewards curve from DirectCapture2 you would earn:
  
  ```math
  0.1* \frac{x}{Total RPL Stake Supply} + 0.9*\frac{1.3*MiniPoolCount}{TotalWeightOfNOStakedRPL}
  ```
  
  "TotalWeightOfNOStakedRPL" is calculated by summing the weight of each individual NO, so that each NO earns their proportional weight of rewards.
  
</details>
<br/>

**UVC/Adjusting variables:**

If Rocket Pool desperately needs more node operators, category 1 can be increased at the expense of category 2 or 3 (this leads to a smaller total pot for "StakedRPLCommissionCut"). As Rocket Pool approaches maturity near self-limiting, RPL can capture more value by increasing category 2 and then 3 at the expense of 1 (increase total pot for "StakedRPLCommissionCut", and then also increase coefficient "a" at the expense of coefficient "b").

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
