## Summary:

The python script [RCM_plotter.py](/RCM_plotter.py) allows you toggle various inputs and plot the resulting RCM's for comparison. RCM means Rewarded Capital Multiplier, and the foundation for the calculations comes from this comparison done by Lido: [Lido Research bond and staking fee napkin math](https://research.lido.fi/t/bond-and-staking-fee-napkin-math/5999), where their complete calculations are found [here](https://docs.google.com/spreadsheets/d/1L-jtZkMF2ixQrkPlV58ONoteq1UtuCpj50RDJ5B3v6w/edit#gid=0). A similar excel sheet that shows various calculations for this commission cut proposal can be found in this repository ([YieldComparisons.xlsx](/YieldComparisons.xlsx)), or it can be viewed on google sheets [here](https://docs.google.com/spreadsheets/d/12Q7qeI4TS-vMcviZIDuIwXO0p1UF5GUh/edit#gid=1728151719).

A simple summary of the plot is that the Y axis is RCM (rewarded capital multiplier), it’s the multiplier of how much more rewards you earn vs solo staking (solo staking y = 1), if earning twice as much rewards then y = 2… etc

X-axis is the percentage of Eth Only Node operator bond out of total Node operator bond (For 1/3 Eth Only bond x=33.33%, so the the remaining 2/3 is Rpl-Staked Node Operator Bond)

Here's an example below that uses the default inputs:\
![Default Inputs](/plots/defaultInputs.png)

---

## Deriving the equation for calculating new diverted Eth reward per minipool

New diverted Eth reward per minipool will be **Y** and it is calculated by dividing the Total New Eth Diverted (**Tned**) by the Total number of Rpl-Staked (RS) Minipools (MP) (**Trs_mp**)

```math
Y = \frac{T_{NED}}{T_{RS_MP}}
```
