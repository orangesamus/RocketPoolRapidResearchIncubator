#%%
import numpy as np
import matplotlib.pyplot as plt

def pct(x):
    return x/100

def K_aprRatio(ethInflation,rplInflation,rplInflationToStakers,rplStakedPercent,ethAPR):
    C_parity = (1+ethInflation)/(1+rplInflation)
    rplStakingAPR = rplInflation*rplInflationToStakers/rplStakedPercent
    rplStakingAPRinETH = (1+rplStakingAPR)*C_parity - 1
    K = rplStakingAPRinETH/ethAPR
    return K

def ethRewardNoDivertedCommission(ethBond,rplBond,K,Fee,ethAPR):
    return ((ethBond+(32-ethBond)*Fee+rplBond*K)*ethAPR)

def newDivertedCommissionReward(x,a,b,c,d):
    return (32*(pct(x)/(1-pct(x)))*a*b*c)/(1+d)

def soloStakeReward(totalBond,APR):
    return totalBond*APR

# Variables that affect RCM of proposed LEB's that receive diverted commission
ratioEO_CB = 7                 # 'a' ratio: (Eth-Only Created Eth)/(Eth-Only Bonded Eth), LEB4's = 7, (4 Bond, 28 Created, 28/4=7)
ethAPR = pct(3)                # 'b'
commissionCutDiverted = pct(7) # 'c' diverted away from Eth-Only Nodes to Rpl-Staked Nodes
ratioRS_CB = 2                 # 'd' ratio: (Rpl-Staked Created Eth)/(Rpl-Staked Bonded Eth), can choose 5 (between LEB8 & LEB4)

# Variables that affect RCM of EthOnly LEB's
commissionEthOnlyNO = pct(7)
# ethAPR also affects EthOnly RCM

# Variables that affect RCM of all LEB's except EthOnly LEB's
ethInflation = pct(0)
rplInflation = pct(5)
rplInflationToStakers = pct(70)
rplStakedPercent = pct(46.19)
maxLSTFee = commissionCutDiverted + commissionEthOnlyNO

# xlist: create list for x values -> % Eth-Only Bond out of Total Node Operator Bond, start with 0% to 70%
xlist = np.linspace(0,70,num=100)

# Variables created based off of prior inputs
newDivertedCommissionPerMP = newDivertedCommissionReward(xlist,ratioEO_CB,ethAPR,commissionCutDiverted,ratioRS_CB)
APRratio_K = K_aprRatio(ethInflation,rplInflation,rplInflationToStakers,rplStakedPercent,ethAPR)


# current EB16 and proposed EB16
ethBond = 16
rplBond = 1.6
soloStakeRewardEB16 = soloStakeReward((ethBond+rplBond),ethAPR)
currEB16reward = ethRewardNoDivertedCommission(ethBond,rplBond,APRratio_K,maxLSTFee,ethAPR)
RCM_currEB16 = currEB16reward/soloStakeRewardEB16
yRCM_propEB16 = (currEB16reward + newDivertedCommissionPerMP)/soloStakeRewardEB16
yRCM_currEB16 = np.linspace(RCM_currEB16,RCM_currEB16,num=100)

# current LEB8 and proposed LEB8
ethBond = 8
rplBond = 2.4
soloStakeRewardLEB8 = soloStakeReward((ethBond+rplBond),ethAPR)
currLEB8reward = ethRewardNoDivertedCommission(ethBond,rplBond,APRratio_K,maxLSTFee,ethAPR)
RCM_currLEB8 = currLEB8reward/soloStakeRewardLEB8
yRCM_propLEB8 = (currLEB8reward + newDivertedCommissionPerMP)/soloStakeRewardLEB8
yRCM_currLEB8 = np.linspace(RCM_currLEB8,RCM_currLEB8,num=100)

# current LEB4 and proposed LEB4
ethBond = 4
rplBond = 2.8
soloStakeRewardLEB4 = soloStakeReward((ethBond+rplBond),ethAPR)
currLEB4reward = ethRewardNoDivertedCommission(ethBond,rplBond,APRratio_K,maxLSTFee,ethAPR)
RCM_currLEB4 = currLEB4reward/soloStakeRewardLEB4
yRCM_propLEB4 = (currLEB4reward + newDivertedCommissionPerMP)/soloStakeRewardLEB4
yRCM_currLEB4 = np.linspace(RCM_currLEB4,RCM_currLEB4,num=100)

# current LEB2 and proposed LEB2
ethBond = 2
rplBond = 3
soloStakeRewardLEB2 = soloStakeReward((ethBond+rplBond),ethAPR)
currLEB2reward = ethRewardNoDivertedCommission(ethBond,rplBond,APRratio_K,maxLSTFee,ethAPR)
RCM_currLEB2 = currLEB2reward/soloStakeRewardLEB2
yRCM_propLEB2 = (currLEB2reward + newDivertedCommissionPerMP)/soloStakeRewardLEB2
yRCM_currLEB2 = np.linspace(RCM_currLEB2,RCM_currLEB2,num=100)

# proposed Eth Only LEB4
ethBond = 4
rplBond = 0
soloStakeRewardEOLEB4 = soloStakeReward((ethBond+rplBond),ethAPR)
currEOLEB4reward = ethRewardNoDivertedCommission(ethBond,rplBond,APRratio_K,commissionEthOnlyNO,ethAPR)
RCM_propEOLEB4 = currEOLEB4reward/soloStakeRewardEOLEB4
yRCM_propEOLEB4 = np.linspace(RCM_propEOLEB4,RCM_propEOLEB4,num=100)

yRCM_LidoCSM4 = np.linspace(1.5,1.5,num=100)
yRCM_SoloStake = np.linspace(1,1,num=100)

plt.plot(xlist,yRCM_SoloStake,'black',label="SoloStaking")
plt.plot(xlist,yRCM_currEB16,'b',label="currEB16")
plt.plot(xlist,yRCM_currLEB8,'g',label="currLEB8")
#plt.plot(xlist,yRCM_currLEB4,'r',label="currLEB4")
#plt.plot(xlist,yRCM_currLEB2,'m',label="currLEB2")
plt.plot(xlist,yRCM_LidoCSM4,'y',label="Lido propCSM4")
plt.plot(xlist,yRCM_propEOLEB4,'--y',label="propEthOnlyLEB4")
plt.plot(xlist,yRCM_propEB16,'--b',label="propEB16")
plt.plot(xlist,yRCM_propLEB8,'--g',label="propLEB8")
plt.plot(xlist,yRCM_propLEB4,'--r',label="propLEB4")
#plt.plot(xlist,yRCM_propLEB2,'--m',label="propLEB2")
plt.xlabel("% Eth-Only Bond out of Total Node Operator Bond")
plt.ylabel("Rewarded Capital Multiplier")
plt.xticks(np.arange(0, max(xlist)+1, 10))
plt.yticks(np.arange(1, 4.25, 0.25))
# instead of arbitrary y tick range, you can autoscale yticks to 10 values with code below:
#     locs, labels = plt.yticks()
#     plt.yticks(np.arange(1,max(locs),(max(locs)-min(locs))/10))
plt.legend()
#%%