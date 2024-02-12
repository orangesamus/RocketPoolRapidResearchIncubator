## Cohesive Proposal

Combine ideas from 4 categories of submissions:

1. Bond Reduction through sublinear bonding
1. Commission Cut diverted to RPL stakers
1. Universal Variable Commission
1. Protect rETH from underperforming Node Operators

### 1. Bond Reduction

Defer to Valdorff’s recommendations here, using `Aggressive [alt]` from [bond_curves](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/bond_curves.md) (First two minipools are LEB4’s, thereafter allow LEB1.5s).

### 2. Commission Cut:

Mostly building off [direct_capture2](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture2.md) and [direct_capture](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture.md) proposals from Valdorff, with some modifications:

- Change RPL inflation rewards rewards to scale linearly with Node Operator borrowed Eth.
- Split “Staked RPL” into two categories:
  - “NO Staked RPL”: rewards curve suggested in Direct Capture 2 (scales with Borrowed Eth, therefore only accessible to Node Operators)
  - “All Staked RPL”: method described in original Direct Capture (weighted per staked token, scales linearly) – independent from Node Operation duties, opening the market to allow pure RPL staking.
    - Note: “All Staked RPL” still applies to RPL staked by Node Operators
  - Transition: Start with ~Direct Capture2. Over time, transition to ~Direct Capture:
    - Start with Staked RPL yield mostly going to “NO Staked RPL”, and proportionally increase “All Staked RPL” and decrease “NO Staked RPL” until all of this yield goes to “All Staked RPL”

Transition visualized below:

Start with the pie chart on the left, transition to the chart on the right:
![StakedRPLtransition](/plots/StakedRPLtransition.png)

Reason for the modification:

- Traditionally Rocket Pool has married RPL speculation with Node Operation, and has constrained target profitability to be a narrow window:
  - Requiring a minimum RPL bond of 10% borrowed ETH
  - Max effective RPL stake at 150% bonded ETH
  - Recently optimized even more narrowly for an RPL bond of 10-15% borrowed ETH with RPIP30.
- This proposal aims to smoothly transition toward decoupling RPL speculation from Node Operation and support the maximum number of participants in Rocket Pool
  - To start with we are opening the market to RPL skeptics (allowing Eth Only Node Operators, and linearly increasing rewards for “NO Staked RPL” from RPL bonds of 0-12% borrowed ETH).
  - We also open the market to a wider range of RPL speculators by allowing pure RPL staking, and over time transition to giving a larger commission cut to “All Staked RPL”

Summary:

- Individuals will be free to stake only ETH, only RPL, or any combination of the two.
- Staking RPL unlocks a commission cut of Eth
- Node Operation unlocks a base commission cut of Eth, and access to RPL inflation
- Node Operators who also stake RPL unlock a bonus commission cut of Eth

A simple way to visualize eligibility for the different commission cuts (RPL Staked NO also earn the commission cuts from "All Staked RPL" and "All NO's"):\
![RewardsCategories](/plots/RewardsCategories.png)

### 3. Universal Variable Commission

All new minipools are UVC. There are 3 major commission cut knobs to control:

1. “All NO’s”
1. “NO Staked RPL”
1. “All Staked RPL”

In general, we can start by leaving the rETH total commission cut fee (1+2+3) at **14%**:

- 1 (All NO’s) should have a fixed floor value to ensure base case profitability, even if you are an Eth Only Node Operator. For a simple example let’s call it **4%**.
- 3 (All Staked RPL) should have a fixed floor value to ensure base case profitability, even if you are a pure RPL staker. For a simple example let’s call it **1%**.
- 2 (NO Staked RPL) that leaves **9%** as the max amount that could go to NO Staked RPL.

If we start with the numbers above, we are not all that different from today. All NO’s today are RPL staked Node Operators, therefore they have access to all 3 categories of commission cuts, adding up to 14% commission. Most of the commission cut (9%) goes exclusively to NO Staked RPL.

Following the example numbers listed above: All Node Operators will earn 4% commisison, and the remaining 10% commission goes to a commission cut pot to be split among RPL stakers where each RPL staker can calculate their share with an example equation below:

```math
\displayLines{
StakedRPLCommissionCut = ax + by
StakedRPLCommissionCut = \frac{AllStakedRPLCommissionCut}{AllStakedRPLCommissionCut+NOStakedRPLCommissionCut}*{StakedRPLWeighting} + \frac{NOStakedRPLCommisisonCut}{AllStakedRPLCommissionCut+NOStakedRPLCommissionCut}*\frac{(DirectCapture2RewardsCurveWeighting)}{TotalWeightOfNOStakedRPL}
}
```

So in the equations above, if you are a pure RPL staker with x RPL to stake, you would earn:

```math
\displayLines{
\frac{1\%}{1\%+9\%} * \frac{x}{Total RPL Stake Supply} \\
0.1*\frac{x}{Total RPL Stake Supply}
}
```

In the equation above, as a pure RPL staker you would only earn from "AllStakedRPL" commission cut since "NOStakedRPL" commission cut depends on borrowed Eth and is therefore only eligble to NO's, (y variable = 0).

If you are a NO with x RPL at stake, leading to an RPL collateral equivalent to 12% borrowed ETH, you would earn:

```math
\displayLines{
\frac{1\%}{1\%+9\%} * \frac{x}{Total RPL Stake Supply} + \frac{9\%}{1\%+9\%}*\frac{1*MiniPoolCount}{TotalWeightOfNOStakedRPL}\\
0.1*\frac{x}{Total RPL Stake Supply} + 0.9*\frac{1*MiniPoolCount}{TotalWeightOfNOStakedRPL}
}
```

If Rocket Pool desperately needs more node operators, category 1 can be increased at the expense of category 2 or 3 (this leads to a smaller total pot for "StakedRPLCommissionCut"). As Rocket Pool approaches maturity near self-limiting, RPL can capture more value by increasing category 2 and then 3 at the expense of 1 (increase total pot for "StakedRPLCommissionCut", and then also increase coefficient "a" at the expense of coefficient "b").

### 4. Protect rETH from underperforming Node Operators

As we increase leverage by allowing 1.5LEBs with sublinear bonding, it becomes more critical to protect rETH from NO issues. One way this can be accomplished is by allowing Node Operators to add ETH "credit" to their node balance in addition their ETH that is "staked" as bonds for minipools. The "credit" is not earning yield or commission since it isn't staked on the beacon chain or contributing to rETH supply, but it can act as a buffer of collateral to protect rETH from underperformance, and protect a Node Operator from being ejected by Rocket Pool for having too low of an Eth Bond.

One simple example is that this "credit" can be continuously added to from the Eth rewards and Commission from running minipools.

To calculate an example, pretend you were a solo staking Node Operator, and you approach Rocket Pool 32ETH. With sublinear bonding, you create 2 minipools. The total base case yield (ignoring RPL staking) you would earn in a year can be calculated with the equation belows

```math
MinipoolYield = SoloStakingAPR*EthBond + SoloStakingAPR*(32-EthBond)*(AllNOCommissionCut)
```

If we say SoloStakingAPR is 3%, and AllNOCommissionCut = 4%, your total yield comes out to:

```math
\displaylines{
LEB8 = 0.03*4 + 0.03*28*0.04 \\
LEB1.5 = 0.03*1.5 + 0.03*30.5*0.04 \\
Total = 2*LEB8 + 16*LEB1.5 = 1.61 Eth
}
```

This means if you start with 32 Eth, even as an Eth Only Node Operator, roughly once a year you can compound your stake by using your rewards to create an additional 1.5LEB minipool.

In this scenario, you could choose to "auto-credit" your rewards, where your rewards get sent to your "credit" balance, and once your "credit" balance exceeds 1.5ETH you can use your "credit" to create an additional LEB1.5 minipool.

Here is where rETH protection also comes in: Building off ArtDemocrat’s research with some modifications (some context found [here](https://dao.rocketpool.net/t/rapid-research-incubator-submission-reth-protection-through-rpl-rerouting-deflation/2599/4?u=samus)):

- No RPL burn

Ways to penalize underperforming NO’s and make rETH whole (in the order shown below):

1. Take from their ETH Credit
1. Take from their ETH Bond

With the description shown above, Node Operators can essentially "deleverage" some of their stake while retaining the commission cuts they earn from LEB1.5's. This "credit" balance could even be flexible to be used as shared security in other systems like EigenLayer (Shoutout to Jasper's [Rocket Layer Bounty](https://dao.rocketpool.net/t/round-8-gmc-call-for-bounty-applications-deadline-is-january-14/2558/2?u=samus) / [Hybrid Theory Article](https://mirror.xyz/jasperthefriendlyghost.eth/Xv7lLt8SVTfCaFnVie50IvvFrI4-TkQTgZcxb_omEnA)), and further buffer the already leveraged 1.5ETH Bond that is at stake for each minipool.

Rocket Pool has already implemented a simple version of a "credit" balance which was used in the most recent "Atlas" upgrade to assist Node Operators with converting their EB16's to LEB8's. This "credit" balance mechanism could be reused for LEB8 conversions to sublinear bonding, while also functioning as an additional layer of collateral should a Node Operator choose to somewhat deleverage their bonds at stake.

Optional variations:

- Eth rewards could be rerouted to make rETH whole before going to the underperforming Node Operator
- Node Operators could have Rocket Pool convert their "credit" balance to rETH, so that they still earn some staking yield on their credit balance (this would probably have tax implications though to swap ETH for rETH, then back to ETH to stake as a bond for an additional LEB1.5)
- Staked RPL could also be used as a form of collateral, penalizing underperfoming Node Operators could look like something below:

1. Take from their ETH Rewards
1. Take from their ETH (or rETH) Credit
1. Take from their RPL Rewards
1. Take from their RPL Bond
1. Take from their ETH Bond

An additional optional variation: To prevent market impacts to selling RPL for ETH to make rETH whole, the method below could be used:

![RerouteRpl](/plots/RerouteRpl.png)

In the above method, Staked RPL NO’s collectively lose ~some Eth, but gain ~some equivalent amount of RPL for that rewards period

With this method, RPL acts as a buffer of collateral before the ETH Bond is affected, but under extreme scenarios a validator is ejected for falling under the minimum required Eth Bond

### Acknowledgments

Discussions with Knoshua/Valdorff helped shaped some of the ideas under the Commission Cut section, Epineph has helpful additional thoughts on mechanics to implement changes in UVC [here](https://dao.rocketpool.net/t/options-forum-thread/2515/7).
