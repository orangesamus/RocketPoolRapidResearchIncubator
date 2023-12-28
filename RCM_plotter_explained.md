## Summary:

The python script [RCM_plotter.py](/RCM_plotter.py) allows you toggle various inputs and plot the resulting RCM's for comparison. RCM means Rewarded Capital Multiplier, and the foundation for the calculations comes from this comparison done by Lido: [Lido Research bond and staking fee napkin math](https://research.lido.fi/t/bond-and-staking-fee-napkin-math/5999), where their complete calculations are found [here](https://docs.google.com/spreadsheets/d/1L-jtZkMF2ixQrkPlV58ONoteq1UtuCpj50RDJ5B3v6w/edit#gid=0). A similar excel sheet that shows various calculations for this commission cut proposal can be found in this repository ([YieldComparisons.xlsx](/YieldComparisons.xlsx)), or it can be viewed on google sheets [here](https://docs.google.com/spreadsheets/d/12Q7qeI4TS-vMcviZIDuIwXO0p1UF5GUh/edit#gid=1728151719).

A simple summary of the plot is that the Y axis is RCM (rewarded capital multiplier), it’s the multiplier of how much more rewards you earn vs solo staking (solo staking y = 1), if earning twice as much rewards then y = 2… etc

X-axis is the percentage of Eth Only Node operator bond out of total Node operator bond (For 1/3 Eth Only bond x=33.33%, so the the remaining 2/3 is Rpl-Staked Node Operator Bond)

Here's an example below that uses the default inputs:\
![Default Inputs](/plots/defaultInputs.png)

---

## Deriving the equation for calculating new diverted Eth reward per minipool

_Some abbreviations that will be used: Eth-Only = EO, RPL-Staked = RS, Minipools = MP, Node Operator = NO_

New diverted Eth reward per minipool ($Y$) is calculated by dividing the Total New Eth Diverted ($T_{NED}$) by the Total number of RS MPs ($T_{RS\_MP}$)

$$Y = \frac{T_{NED}}{T_{RS\_MP}}$$

The total amount of rETH created by EO MPs will be called $C_{EO}$, and the total amount of ETH bonded by EO MPs will be called $B_{EO}$ (Each LEB4 for example uses 4 bonded Eth to create 28 rETH, so 1 LEB4 contributes 4 to $B_{EO}$ and 28 to $C_{EO}$), similar variables are used for RS MPs ($C_{RS}$ and $B_{RS}$). Therefore,

$T_{NED}$ is calculated by:

$$T_{NED} = C_{EO}*EthSoloStakerAPR*\%CommissionDiverted*Time$$

and $T_{RS\_MP}$ is calculated by:

$$T_{RS\_MP} = \frac{B_{RS}+C_{RS}}{32}$$

The Ratio of RS Created rETh / Bonded Eth will be called $R_{RS\_CB}$ therefore:

$$R_{RS\_CB} = \frac{C_{RS}}{B_{RS}}$$
$$C_{RS} = R_{RS\_CB}*B_{RS}$$

Similarly, the Ratio of EO Created rETh / Bonded Eth will be called $R_{EO\_CB}$ therefore:

$$R_{EO\_CB} = \frac{C_{EO}}{B_{EO}}$$
$$C_{EO} = R_{EO\_CB}*B_{EO}$$

With some substitutions:
$$T_{RS\_MP} = \frac{B_{RS}+C_{RS}}{32}$$
$$T_{RS\_MP} = \frac{B_{RS}+R_{RS\_CB}*B_{RS}}{32}$$
$$T_{RS\_MP} = \frac{B_{RS}*(1+R_{RS\_CB})}{32}$$
$$Y = \frac{T_{NED}}{T_{RS\_MP}}$$
$$Y = \frac{C_{EO}*EthSoloStakerAPR*\%CommissionDiverted*Time}{\frac{B_{RS}*(1+R_{RS\_CB})}{32}}$$
$$Y = 32*\frac{C_{EO}}{B_{RS}}*\frac{EthSoloStakerAPR*\%CommissionDiverted*Time}{(1+R_{RS\_CB})}$$
$$Y = 32*\frac{R_{EO\_CB}*B_{EO}}{B_{RS}}*\frac{EthSoloStakerAPR*\%CommissionDiverted*Time}{(1+R_{RS\_CB})}$$

The ratio of total EO Node Operator Bond / total RS Node Operator Bond can be called $R_{EOB\_RSB}$ therefore:
$$R_{EOB\_RSB} = \frac{B_{EO}}{B_{RS}}$$

Now, $Y$ can be simplified as:
$$Y = \frac{32*R_{EO\_CB}*R_{EOB\_RSB}*EthSoloStakerAPR*\%CommissionDiverted*Time}{(1+R_{RS\_CB})}$$

$R_{EOB\_RSB}$ can also be calculated by taking input $x$ where $x$% is the % of EO Bond out of total NO Bond (For example 1/3 EO Bond will equate to a ratio of 0.5). Therefore:
$$R_{EOB\_RSB} = \frac{x}{1-x}$$

So the final equation for $Y$ for 1 year of time:
$$Y = \frac{32*\frac{x}{1-x}*R_{EO\_CB}*EthSoloStakerAPR*\%CommissionDiverted}{(1+R_{RS\_CB})}$$
