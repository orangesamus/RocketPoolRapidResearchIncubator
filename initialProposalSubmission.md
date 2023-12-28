## Summary:
The summary of this idea is to introduce Eth-Only (EO) minipools (MPs), where a portion of their rewards are diverted to RPL-Staked (RS) MPs. As a simple example, start by offering new node operators (NOs) the same product as Lido’s CSM: (4E bond, and 7.5% commission on the other 28E). For an rETH holder, the commission could remain at 14%, leaving 6.5% on the 28E per MP to be diverted to RS MPs.

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

## Balancing mechanisms:
Answering Rapid Research Incubator topic #1, and #2:
- Balancing supply vs demand of rETH / NOs / RPL holders (#1), and additional value capture mechanisms for RPL (#2)
- This proposal also splits NOs into two parties where balancing should be considered (EO & RS)

### Fixed variables:
It may be difficult to quantify demands and create ways to automatically adjust the commission variables as described before in 1.4, but there is balancing to some degree even with fixed values. Starting by assessing the effects with fixed value commissions (A = 7.5%, B = 6.5%, C = 14%):
- rETH vs NO 
    - A new competitive market is opened for NO’s that want Eth only, which allows for additional supply to balance rETH demand. If rETH supply begins to outpace demand, there is a new release valve where value can flow from this new supply of EO NO’s to RS NO’s (who tend to be more RPL aligned). 
- RPL Value
    - The value in this new release valve could either go directly to RPL (see 3.5 under “variables to consider”) turning on a ‘fee switch’, or indirectly by improving the value proposition of RPL collateralized nodes. Over time this new yield could slowly reduce or replace RPL inflation.
    - Right now the only benefits to staking more RPL to a node is unlocking more RPL yield from RPL inflation. This becomes particularly unappealing if RPL/ETH ratio continues to decrease.  With this proposal, staking more RPL can now unlock more ETH yield. This should have a stabilizing effect on both the profitability of RS nodes, and the value of RPL in relation to ETH.
    - If eligibility 2.2 from variables section is chosen, RS NOs who don’t want or can’t afford to top up to 10% still have a new incentive to keep their RS MPs running, rather than the ‘all or nothing’ benefits mentality at 10% which often causes frustrated RS NOs to close their MPs and sell their RPL.
- EO vs RS:
    - As more EO MPs are created, the total ETH value of B will increase. If the number of RS MPs stays the same, or grows at a slower rate than EO MPs, RS MPs become increasingly more profitable. RS MPs could now have an “unbounded APR” as Jasper pointed out in the Options Draft discord channel. Over time, NOs are more rationally incentivized to open RS MPs compared to EO MPs (to receive B yield).
    - There doesn’t “need” to be a balance of having more EO MPs, but the less EO MPs there are, the less the total ETH value of B yield will be. This makes RS MPs neutral - less attractive than in the scenario from the previous bullet point (but the same attractiveness that they are today since B yield doesn’t exist today).

### Dynamic Variables:
Below are some examples of potential balancing effects of dynamic variable commissions:
- (Reminder C = A + B: A is EO commission, B is remaining commission diverted to RS NOs)
- ‘A’ could have some fixed floor value to provide prospective NOs an assurance of base case profitability.
- If rETH demand consistently outpaces supply, A could be increased, and B could be decreased (while C remains the same). This incentivizes additional NOs to join to create more rETH supply.
- If rETH supply outpaces demand (or meets it at equilibrium) and EO MPs demand outpaces RS MPs demand, A could be decreased, and B could be increased (while C remains the same).
- If rETH supply dramatically outpaces demand (too much Node Operator demand from both EO and RS MP creations), C could be reduced by lowering both A and B (could be done proportional to EO vs RS demand)
- The bullet points above would need methods or equations to quantify supply/demand. Some metrics are brainstormed below as inputs for equations, but would need further evaluation to ensure they aren’t gamed:
    1. rETH premium / discount
    2. Deposit Pool status/size
    3. rETH supply growth
    4. MP growth (can also consider RS vs EO pool growth)

## Potential drawbacks:
- RPL selling: RS NOs find EO staking more attractive, leading to mass selling/conversions of excess RPL to Eth for EO staking.
    - I think this is mitigated by the additional ETH yield earned from diverting EO yields to RS NOs. There will be similar products elsewhere that offer EO staking, so NOs will soon have more options outside of the protocol where they could sell RPL and migrate to EO staking if this is their desire. Rocket Pool can instead offer a similar competitive EO product, but capture value back from rETH holders to reward RPL collateralized NOs
    - As discussed previously – if more RS nodes convert to EO nodes, those who remain as RS nodes become proportionally more profitable, rewarding alignment to the protocol/RPL
- With more competition and a “race to the bottom” of fees, this proposal may present challenges. Rocket Pool charges 14% commission, but Lido only charges 10% presently – or 7.5% with CSM module. If every other protocol begins lowering commissions further (and do not route any additional commission to an equivalent “RS NO” in their protocol), the margins are compressed for Rocket Pool to compete and LST holders may avoid rETH in favor of cheaper commissions elsewhere.
    - This has always been a risk (Rocket Pool can never compete with Lido’s permissioned validator set on commission percentages for ex) and is unchanged with this proposal.
    - By offering NOs products of varying degrees of RPL speculation, Rocket Pool can capture more value and still provide outsized rewards for RS NOs
- Execution challenges: Implementation of distributing B yield would need further research. Val pointed this out/helped discuss in the options draft discord channel.
    - Ideally B yield would continuously distribute to RS NOs in a similar fashion to the smoothie pool. In practice it could be simpler to leave it to be routed when EO NOs choose to distribute their rewards. This should smooth out over time as more EO NOs join as they are incentivized to eventually claim their rewards, but gaming needs to be considered (ex: EO NO avoids distributing, then stakes large amounts of RPL as a RS NO, distributes from EO node/receiving a portion as RS NO, then sells RPL/exits RS NO)
    - Anyone can distribute so there’s a defense built in from that perspective, but maybe it is worth forcing all EO nodes to distribute every month. Or could it be possible to have the smart contract route the B yield automatically before going to the EO node?

## Follow up:
- This was a first draft, with the hopes of discussing ideas from an abstract level before diving deeper into implementations. I may also consolidate points down to a smaller document.
- I can come back and calculate some example scenarios for the amounts of additional Eth yield each RS MP could receive to make things more concrete.
- Research needed if this proposal is considered:
    - Establishing variables from “Variables to consider” section
    - Establishing ways to determining dynamic variables if they are made to be dynamic
    - Execution plan for distributing B yield
