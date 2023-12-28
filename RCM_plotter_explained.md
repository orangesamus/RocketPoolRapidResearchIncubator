## Summary:

The python script [RCM_plotter.py](/RCM_plotter.py) allows you toggle various inputs and plot the resulting RCM's for comparison. The foundation for the calculations comes from this comparison done by Lido: [Lido Research bond and staking fee napkin math](https://research.lido.fi/t/bond-and-staking-fee-napkin-math/5999), where their complete calculations are found [here](https://docs.google.com/spreadsheets/d/1L-jtZkMF2ixQrkPlV58ONoteq1UtuCpj50RDJ5B3v6w/edit#gid=0). A similar excel sheet that shows various calculations for this commission cut proposal can be found in this repository ([YieldComparisons.xlsx](/YieldComparisons.xlsx)), or it can be viewed on google sheets [here](https://docs.google.com/spreadsheets/d/12Q7qeI4TS-vMcviZIDuIwXO0p1UF5GUh/edit#gid=1728151719).

A simple summary of the plot is that the Y axis is RCM (rewarded capital multiplier), it’s the multiplier of how much more rewards you earn vs solo staking (solo staking y = 1), if earning twice as much rewards then y = 2… etc

X-axis is the percentage of Eth Only Node operator bond out of total Node operator bond (For 1/3 Eth Only bond x=33.33%, so the the remaining 2/3 is Rpl-Staked Node Operator Bond)

The commission cut proposal explored here uses a simple distribution strategy of evenly dividing the total new ETH diverted from the commission cut by the total number of minipools (All minipools earn the same amount, so a lower LEB has higher RPL exposure but earns more ETH commissionn relative to the size of their bond).

Here's an example below that uses the default inputs:\
![DefaultInputs](/plots/defaultInputs.png)

The x-axis ranges from 0% to 70% because of 'unbounded' APR on the top end, (if only 1 pool was Rpl-staked, that pool would earn diverted commission from all the other pools). So after ~70% it really picks up vertically and makes it hard to understand what is going on from 0%-70%. See example below:\
![PlotTo100Percent](/plots/PlotTo100Percent.png)

### Example Scenarios and Conclusions
Start with the default inputs (explanation of inputs can be found [here](#input-variables)):
|x|a|b|c|d|e|f|g|h|i|j|
|-|-|-|-|-|-|-|-|-|-|-|
|\[0%...70%\]|7|3%|7%|2|7%|0%|5%|70%|46.19%|14%|

![DefaultInputs](/plots/defaultInputs.png)

Example 1: The effects of adjusting the commission paid to Eth-Only Node Operators, vs diverted to Rpl-Staked Node Operators (keep all input variables the same but change 'c' and 'e'):
|scenario 1|scenario 2|scenario 3|
|:-:|:-:|:-:|
|c=3%, e=11%, more to Eth-Only|c=7%, e=7%, default inputs|c=11%, e=3%, more to Rpl-Staked|
|![EOEarnMore](/plots/EthOnlyEarnMoreCommission.png)|![Default](/plots/defaultInputs.png)|![RSEarnMore](/plots/divertMoreCommissionToRPLStakedNO.png)|
Conclusion: propEthOnlyLEB4's RCM moves up and down based off it's commission 'e' (7% makes it competitive to Lido propCSM4), propLEB's RCMs scale higher based off commission diverted 'c'.

## Calculations Explained
### Input Variables
Input variables that affect RCM of proposed LEB's that receive diverted Eth Commission per Minipool:

| Variable | Ranges For Input Values | Notes |
| -------- | ----------------------- | ----- |
|$`\frac{x}{1-x} = R_{EOB\_RSB}`$| 0% <= x < 100%|Ratio of Eth-Only bond over Rpl-staked bond; can be input as x% Eth-Only bond and ratio can be calculated with equation: x/(1-x). Example: 1/3 Eth-Only Node Operator Bond = $`\frac{33.33\%}{(1-33.33\%)} = 0.5`$|
|a = $`R_{EO\_CB}`$| 1 <= a <= 15 |Ratio of Eth-Only created Eth over Eth-Only bonded Eth. If Eth-Only minipools were all LEB4, a = 7 since LEB4 is 4 bonded Eth, 28 created Eth, 28/4 = 7. Range of 1 (EB16) to 15 (LEB2)|
|b = $EthSoloStakerAPR$|2.5% <= b <= 5%| ultrasound.money website shows APR range from 2.5% to 5%, currently this value is close to 3%|
|c = $`\%CommissionDiverted`$|0% <= c <= MaxLSTFee%|Commission cut % diverted from Eth-Only Node Operators to Rpl-staked Node Operators, where MaxLSTFee is the commission Fee charged to LST holders. Target 7% to be competitive with Lido CSM with 4Eth bond. If c = MaxLSTFee% Eth-Only Node Operators have no incentive to join since their RCM would be the same as a solo staker|
|d = $`R_{RS\_CB}`$|1 <= d <= 15|Ratio of Rpl-staked created Eth over Rpl-staked bonded Eth. If all RPL-staked was LEB8 this would be: 3. Since some RPL-staked are still EB16, this number is between 1 and 3: currently close to 2 on rocketscan|

\
\
Input variables that affect RCM of Eth-Only LEB's
| Variable | Ranges For Input Values | Notes |
| -------- | ----------------------- | ----- |
| e = $`CommissionEthOnlyNO`$|0% <= e <= MaxLSTFee%|Commission paid to Eth-Only Node Operators. Target 7% to be competitive with Lido CSM with 4Eth bond. If c = 0% Eth-Only Node Operators have no incentive to join since their RCM would be the same as a solo staker.|
|b = $EthSoloStakerAPR$|2.5% <= b <= 5%| Eth-Only LEB's are also impacted by this variable since it is the source of the yield|

\
\
Input Variables that affect RCM of all LEB's except Eth-Only LEB's
| Variable | Ranges For Input Values | Notes |
| -------- | ----------------------- | ----- |
|f = $`ethInflation`$|f = 0%|Eth is slightly deflationary but this could be rounded to 0% for simplification|
|g = $`rplInflation`$|0% <= rplInflation <= 5%|Current RPL inflation rate is 5% but could be lowered to 0%|
|h = $`rplInflationToStakers`$|0<= h = 100%|This is the % of RPL inflation that is being paid to RPL-Staked Node Operators. This number is currently 70% but could be changed in the future|
|i = $`rplStakedPercent`$|0% <= i <= 100% |This number is currently ~46.19% but is growing steadily over time|
|j = $`maxLSTFee`$|j = commissionCutDiverted + commissionEthOnlyNO|This is the fee/commission charged to LST holders on the Eth-Only created Eth. A cut of this commission could also be diverted to fund the protocol instead of relying on RPL inflation|

### Equations
Equations from Lido's napkin math:
```
RC_generic = Bond + (32 - Bond) * MaxFee
RC_csm = Bond * (1 - LidoStakingFee) + 32 * MaxFee
RC_alt = BondETH + (32 - BondETH) * MaxFee + BondALT * K
RPL_StakingAPR_in_ETH = (1 + RPL_StakingAPR) * C_parity - 1
C_parity = (1 + ETH_inflation) / (1 + RPL_inflation)
RPL_StakingAPR = RPL_inflation * RPL_inflation_allocation_to_stakers / RPL_staked_percent
K = RPL_StakingAPR_in_ETH / ETH_StakingAPR
```

The Equations above can be used to calculate the current LEB RCM (no new diverted Eth commission). The total Eth value of the rewards is calculated by multiplying the total Eth value of the Bond by the solo staking Eth APR, and then multiplying that by the corresponding RCM as shown below:

```math
EthRewardsBeforeDivertedCommission = (EthBond+RplBond)*ethAPR*currLEB\_RCM
```

Next, the diverted Eth commission reward per minipool is calculated using the equation below (explanation of the equation can be found [here](#deriving-the-equation-for-calculating--per-minipool)):

```math
\displaylines{
    NewDivertedCommissionReward = \frac{32*\frac{x}{1-x}*R_{EO\_CB}*EthSoloStakerAPR*\%CommissionDiverted}{(1+R_{RS\_CB})} \\
    or \\
    Y = \frac{32*\frac{x}{1-x}*a*b*c}{(1+d)}
}
```

Finally, the proposed new RCM can be calculated by adding the original Eth rewards with the new diverted Eth commission rewards, and dividing that sum by the solo staking Eth rewards

```math
propLEB\_RCM = (EthRewardsBeforeDivertedCommission+NewDivertedCommissionReward)/soloStakeEthRewards
```

### Deriving the equation for calculating $`NewDivertedCommissionReward`$ per minipool

_Some abbreviations that will be used: Eth-Only = EO, RPL-Staked = RS, Minipools = MP, Node Operator = NO_

New diverted Eth reward per minipool ($Y$) is calculated by dividing Total New Eth Diverted ($T_{NED}$) by Total number of RS MPs ($`T_{RS\_MP}`$)

```math
Y = \frac{T_{NED}}{T_{RS\_MP}}
```

The total amount of ETH created by EO MPs will be called $C_{EO}$, and the total amount of ETH bonded by EO MPs will be called $B_{EO}$ (Each LEB4 for example uses 4 bonded Eth to create 28 ETH, so 1 LEB4 contributes 4 to $B_{EO}$ and 28 to $C_{EO}$), similar variables are used for RS MPs ($C_{RS}$ and $B_{RS}$). Therefore,

$T_{NED}$ is calculated by:

```math
T_{NED} = C_{EO}*EthSoloStakerAPR*\%CommissionDiverted*Time
```

and $`T_{RS\_MP}`$ is calculated by:

```math
T_{RS\_MP} = \frac{B_{RS}+C_{RS}}{32}
```

The Ratio of RS Created ETH / Bonded Eth will be called $`R_{RS\_CB}`$ therefore:

```math
\displaylines{
    R_{RS\_CB} = \frac{C_{RS}}{B_{RS}} \\
    C_{RS} = R_{RS\_CB}*B_{RS}
}
```

Similarly, the Ratio of EO Created ETH / Bonded Eth will be called $`R_{EO\_CB}`$ therefore:

```math
\displaylines{
    R_{EO\_CB} = \frac{C_{EO}}{B_{EO}} \\
    C_{EO} = R_{EO\_CB}*B_{EO}
}
```

With some substitutions:

```math
\displaylines{
    T_{RS\_MP} = \frac{B_{RS}+C_{RS}}{32} \\
    T_{RS\_MP} = \frac{B_{RS}+R_{RS\_CB}*B_{RS}}{32} \\
    T_{RS\_MP} = \frac{B_{RS}*(1+R_{RS\_CB})}{32} \\
    Y = \frac{T_{NED}}{T_{RS\_MP}} \\
    Y = \frac{C_{EO}*EthSoloStakerAPR*\%CommissionDiverted*Time}{\frac{B_{RS}*(1+R_{RS\_CB})}{32}} \\
    Y = 32*\frac{C_{EO}}{B_{RS}}*\frac{EthSoloStakerAPR*\%CommissionDiverted*Time}{(1+R_{RS\_CB})} \\
    Y = 32*\frac{R_{EO\_CB}*B_{EO}}{B_{RS}}*\frac{EthSoloStakerAPR*\%CommissionDiverted*Time}{(1+R_{RS\_CB})}
}
```

The ratio of total EO Node Operator Bond / total RS Node Operator Bond can be called $`R_{EOB\_RSB}`$ therefore:

```math
R_{EOB\_RSB} = \frac{B_{EO}}{B_{RS}}
```

Now, $Y$ can be simplified as:

```math
Y = \frac{32*R_{EO\_CB}*R_{EOB\_RSB}*EthSoloStakerAPR*\%CommissionDiverted*Time}{(1+R_{RS\_CB})}
```

$`R_{EOB\_RSB}`$ can also be calculated by taking input $x$ where $x$% is the % of EO Bond out of total NO Bond (For example 1/3 EO Bond will equate to a ratio of 0.5). Therefore:

```math
R_{EOB\_RSB} = \frac{x}{1-x}
```

So the final equation for $Y$ for 1 year of time:

```math
Y = \frac{32*\frac{x}{1-x}*R_{EO\_CB}*EthSoloStakerAPR*\%CommissionDiverted}{(1+R_{RS\_CB})}
```

With simplified variable names:
```math
Y = \frac{32*\frac{x}{1-x}*a*b*c}{(1+d)}
```