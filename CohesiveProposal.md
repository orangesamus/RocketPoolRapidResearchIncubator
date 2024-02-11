## Cohesive Proposal

Combine ideas from 4 categories of submissions: \
1. Bond Reduction through sublinear bonding
1.	Commission Cut diverted to RPL stakers
1.	Universal Variable Commission
1.	Protect rETH from underperforming Node Operators

### 1. Bond Reduction
Defer to Valdorff’s recommendations here, using `Aggressive [alt]` from [bond_curves](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/bond_curves.md) (First two minipools are LEB4’s, thereafter allow LEB1.5s).

### 2. Commission Cut:
Mostly building off [direct_capture2](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture2.md) and [direct_capture](https://github.com/Valdorff/rp-thoughts/blob/main/2023_11_rapid_research_incubator/direct_capture.md) proposals from Valdorff, with some modifications:
- Keep the RPL Inflation rewards curve independent from Direct Capture rewards curve, it can continue with the RPIP30 model for now.
- Split “Staked RPL” into two categories:
    - “NO Staked RPL”: rewards curve suggested in Direct Capture 2 (scales with Borrowed Eth, therefore only accessible to Node Operators)
    - “All Staked RPL”: method described in original Direct Capture (weighted per staked token, scales linearly) – independent from Node Operation duties, opening the market to allow pure RPL staking.
        - Note: “All Staked RPL” still applies to RPL staked by Node Operators
    - Transition: Start with ~Direct Capture2. Over time, transition to ~Direct Capture:
        - Start with Staked RPL yield mostly going to “NO Staked RPL”, and proportionally increase “All Staked RPL” and decrease “NO Staked RPL” until all of this yield goes to “All Staked RPL”  
        - Simultaneously, increase the rewards curve linear range of “NO Staked RPL”, (Direct Capture2 proposes a linear range of 0% -> x% borrowed Eth. Here we would increase x, starting from 12%)

Transition visualized below:

Start with the pie chart on the left, transition to the chart on the right:
![StakedRPLtransition](/plots/StakedRPLtransition.png)

Reason for the modification:
- Traditionally Rocket Pool has married RPL speculation with Node Operation, and has constrained target profitability to be a narrow window:
    - Requiring a minimum RPL bond of 10% borrowed ETH
    - Max effective RPL stake at 150% bonded ETH
    - Recently optimized even more narrowly for 10-15% borrowed ETH with RPIP30.
- This proposal aims to smoothly transition toward decoupling RPL speculation from Node Operation and support the maximum number of participants in Rocket Pool
    - To start with we are opening the market to RPL skeptics (allowing Eth Only Node Operators, and linearly increasing rewards for “NO Staked RPL” from 0-12% borrowed ETH).
    - Over time we also transition to opening the market to the heaviest RPL speculators (those who wish to stake purely RPL, no Node Operation/Eth staked), by increasing “All Staked RPL”, and increasing the linear rewards curve range for “NO Staked RPL”

Summary:
- Individuals will be free to stake only ETH, only RPL, or any combination of the two.
- Staking RPL unlocks a commission cut of Eth
- Node Operation unlocks boosted commission cut of Eth, and access to RPL inflation

### 3. Universal Variable Commission
All new minipools are UVC. There are 3 major commission cut knobs to control:
1.	“All NO’s”
1.	“NO Staked RPL”
1.	“All Staked RPL” 

In general, we can start by leaving the rETH total commission cut fee (1+2+3) at 14%:
- 1 (All NO’s) should have a fixed floor value to ensure base case profitability, even if you are an Eth Only Node Operator. For a simple example let’s call it 3%. 
- 3 (All Staked RPL) should have a fixed floor value to ensure base case profitability, even if you are a pure RPL staker. For a simple example let’s call it 1%.
- 2 (NO Staked RPL) that leaves 10% as the max amount that could go to NO Staked RPL.

If we start with the numbers above, we are not all that different from today. All NO’s today are RPL staked Node Operators, therefore they have access to all 3 categories of commission cuts, adding up to 14% commission. Most of the commission cut (10%) goes to NO Staked RPL.

If Rocket Pool desperately needs more node operators, category 1 can be increased at the expense of category 2 or 3. As Rocket Pool approaches maturity near self-limiting, RPL can capture more value by increasing category 2 and then 3 at the expense of 1.

### 4. Protect rETH from underperforming Node Operators
As we increase leverage by allowing 1.5LEBs with sublinear bonding, it becomes more critical to protect rETH from NO issues. Build off ArtDemocrat’s research with some modifications (some conetext found [here](https://dao.rocketpool.net/t/rapid-research-incubator-submission-reth-protection-through-rpl-rerouting-deflation/2599/4?u=samus)):
- No RPL burn

Ways to penalize underperforming NO’s and make rETH whole (in the order shown below):
1.	Take from their ETH Rewards
1.	Take from their RPL Rewards
1.	Take from their RPL Bond
1.	Take from their ETH Bond

Optional: To prevent market impacts to selling RPL for ETH to make rETH whole, the method below could be used:

![RerouteRpl](/plots/RerouteRpl.png)

In the above method, Staked RPL NO’s collectively lose ~some Eth, but gain ~some equivalent amount of RPL for that rewards period

With this method, RPL acts as a buffer of collateral before the ETH Bond is affected, but under extreme scenarios a validator is ejected for falling under the minimum required Eth Bond


### Acknowledgments
Discussions with Knoshua/Valdorff helped shaped some of the ideas under the Commission Cut section, Epineph has helpful additional thoughts on mechanics to implement changes in UVC [here](https://dao.rocketpool.net/t/options-forum-thread/2515/7).