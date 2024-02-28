# Rocket Pool Roadmap

The goal of this page is to present an outline of the Rocket Pool Roadmap, including proposals being considered for inclusion.

_Disclaimer: This is a work in progress and represents my own personal perspective_

## Introduction

This outline includes three main sections:

1. [Summary Table](#summary-table):
   1. Summarizes all of the proposals with the following categories:
      1. Priority
      2. Governance Stage
      3. Technical Stage
2. [Releases](#releases):
   1. These are the upgrades/releases on the horizon for Rocket Pool.
   2. Each release shows the proposals that are planned for inclusion.
   3. Proposals in this category have been voted on and approved by the pDAO.
3. [Considering for Inclusion](#considering-for-inclusion):
   1. This section is categorized first by topic, with each topic listing the proposals being considered for inclusion.
   2. The topics and proposals are listed in no particular order.
   3. Proposals in this section may not have an RPIP yet and it is uncertain which Rocket Pool upgrade they will be included in (if at all).
   4. This outline does not provide an exhaustive list of all proposals or research ideas, but instead prioritizes ideas being considered for inclusion.

## Summary Table

A Summary of the Proposals being considered for Inclusion, with the following categories:

- Priority (Author-subjective for now)
  - 1: High
  - 2: Medium
  - 3: Low
- Governance
  - 1: Early discussion
  - 2: Forum temp checking
  - 3: Voting
  - 4: Accepted
- Technical
  - 1: Early research
  - 2: Proof of concept
  - 3: Full spec
  - 4: Ready

| Name                                                               | Priority | Governance | Technical |
| ------------------------------------------------------------------ | :------: | :--------: | :-------: |
| [RPIP-31: RPL Withdrawal Address](#1-houston)                      |    1     |     4      |     4     |
| [RPIP-32: Stake ETH on behalf of node](#1-houston)                 |    1     |     4      |     4     |
| [RPIP-33: On-Chain pDAO](#1-houston)                               |    1     |     4      |     4     |
| [RPIP-28: Deposits Under the Minimum](#2-saturn)                   |    1     |     4      |     ?     |
| [RPIP-30: RPL Staking Rework](#2-saturn)                           |    2     |     4      |     ?     |
| [RPIP-35: Time-based Balance and RPL Price Submissions](#2-saturn) |    3     |     4      |     ?     |
| [Megapools](#1-megapools)                                          |    1     |     1      |    3?     |
| [Sublinear Bonding](#2-sublinear-bonding)                          |    1     |     1      |     1     |
| [RPL Value Capture](#3-rpl-value-capture)                          |    1     |     1      |     1     |
| [Universal Variable Commission](#4-universal-variable-commission)  |    2     |     1      |     1     |
| [rETH Protection](#5-reth-protection)                              |    3     |     1      |     1     |
| [Forced Exits](#6-forced-exits)                                    |    1     |     1      |    2?     |
| [RPL Inflation Rework](#7-rpl-inflation-rework)                    |    3     |     1      |     1     |

<br/>

## Releases

---

### 1. Houston

#### Proposals

1. [RPIP-31: RPL Withdrawal Address](https://rpips.rocketpool.net/RPIPs/RPIP-32)
2. [RPIP-32: Stake ETH on behalf of node](https://rpips.rocketpool.net/RPIPs/RPIP-32)
3. [RPIP-33: On-Chain pDAO](https://rpips.rocketpool.net/RPIPs/RPIP-33)<sup>\*</sup>

#### Required Support

1. [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)<sup>\*</sup>

#### Notes

<sup>\*</sup>EIP-4788 is required for RPIP-33. EIP-4788 is included in the "Dencun" Ethereum Upgrade scheduled for March 13th, 2024

---

### 2. Saturn

#### Proposals

1. [RPIP-28: Deposits Under the Minimum](https://rpips.rocketpool.net/RPIPs/RPIP-28)
2. [RPIP-30: RPL Staking Rework](https://rpips.rocketpool.net/RPIPs/RPIP-30)<sup>\*</sup>
3. [RPIP-35: Time-based Balance and RPL Price Submissions](https://rpips.rocketpool.net/RPIPs/RPIP-35)

#### Notes

<sup>\*</sup>Rewards rework has already been implemented by the oDAO, but unstaking rework requires smart contract changes and has not been implemented yet

---

<br/>

## Considering for Inclusion

---

### 1. Megapools

Each Node can have all minipools under the same contract instead of requiring each minipool to have its own contract.

#### Proposals

1. [One megapool contract per node which acts as the withdrawal credentials for one or many validators](/Proposals/Megapools.md)<sup>\*</sup>

#### Required Support

1. [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)<sup>\*</sup>

#### Notes

<sup>\*</sup>EIP-4788 is required for Megapools. EIP-4788 is included in the "Dencun" Ethereum Upgrade scheduled for March 13th, 2024

---

### 2. Sublinear Bonding

The first minipool(s) require a higher bond from a new Node Operator than subsequent minipools on the same Node.

#### Proposals

1. [First two minipools are LEB4’s, thereafter allow LEB1.5's](/Proposals/SublinearBonding.md#1-first-two-minipools-are-leb4s-thereafter-allow-leb15s)<sup>\*†‡§</sup>

#### Required Support

1. [Forced Exits](#5-forced-exits)<sup>\*</sup>
2. [EIP7002: Execution Layer Triggerable Exits](https://eips.ethereum.org/EIPS/eip-7002)<sup>†</sup>

#### Recommended Support

1. [rETH Protection](#4-reth-protection)<sup>‡</sup>
2. [Universal Variable Commission](#4-universal-variable-commission)<sup>§</sup>

#### Notes

<sup>\*</sup>With sublinear bonding, Forced Exits are critical to protect against loss scenarios associated with MEV theft and abandonment

<sup>†</sup>EIP-7002 is required for Forced Exits. EIP-7002 is tentatively planned for inclusion in the "Pectra" Ethereum Upgrade which is tentatively scheduled for ~Q4 2024

<sup>‡</sup>As we increase leverage by allowing sublinear bonding, it becomes more important to protect rETH from underperforming NO's

<sup>§</sup>Commission becomes a higher portion of Node Operator revenue with sublinear bonding. It becomes important then for Rocket Pool to have the ability to tweak commission variables over time since opt-in upgrades may not be enough to incentivize Node Operators to migrate away from their fixed commission into minipools with variable commission.

---

### 3. RPL Value Capture

#### Proposals

1. [Change rETH commission to be split between NO's and RPL](#3-rpl-value-capture)<sup>\*</sup>

#### Recommended Support

1. [Universal Variable Commission](#4-universal-variable-commission)<sup>\*</sup>

#### Notes

<sup>\*</sup>Ideally, UVC would be used to set the proportions of commission going to each group in RPL Value Capture

---

### 4. Universal Variable Commission

Commission variables can be universally changed by the protocol instead of each minipool having its own fixed commission.

#### Proposals

1. [Allow markets to find equilibrium for total rETH LST fee, NO commission, and RPL value capture](/Proposals/UniversalVariableCommission.md#1-allow-markets-to-find-equilibrium-for-total-reth-lst-fee-no-commission-and-rpl-value-capture)<sup>\*</sup>

#### Recommended Support

1. [RPL Value Capture](#3-rpl-value-capture)<sup>\*</sup>

#### Notes

<sup>\*</sup>Ideally, UVC would be used to set the proportions of commission going to each group in RPL Value Capture

---

### 5. rETH Protection

Outlier underperforming NO's pay restitution to rETH.

#### Proposals

1. [First take from NO ETH rewards, then mark any remaining unpaid restitution as NO debt](/Proposals/rETHprotection.md)

---

### 6. Forced Exits

Enable Rocket Pool to kick a NO and access the NO's bond as needed.

#### Proposals

1. [Exit a validator when a NO's (total_leakage + debt) > 0.5 ETH](/Proposals/ForcedExits.md#1-exit-a-validator-when-a-nos-total_leakage--debt--05-eth)<sup>\*</sup>

#### Required Support

1. [EIP7002: Execution Layer Triggerable Exits](https://eips.ethereum.org/EIPS/eip-7002)<sup>\*</sup>

#### Notes

<sup>\*</sup>EIP-7002 is required for Forced Exits. EIP-7002 is tentatively planned for inclusion in the "Pectra" Ethereum Upgrade which is tentatively scheduled for ~Q4 2024

---

### 7. RPL Inflation Rework

Change RPL Inflation (proposals range from changing distribution eligibility to removing inflation altogether)

#### Proposals

1. [Change RPL Inflation to NO's to distribute by Borrowed ETH](/Proposals/RPLInflationRework.md#1-change-rpl-inflation-to-nos-to-distribute-by-borrowed-eth)
2. [Scale Down RPL Inflation to NO's over time](/Proposals/RPLInflationRework.md#2-scale-down-rpl-inflation-to-nos-over-time)
3. [Remove RPL Inflation to NO's](/Proposals/RPLInflationRework.md#3-remove-rpl-inflation-to-nos)
4. [Remove RPL Inflation to oDAO & pDAO and replace with ETH commission](/Proposals/RPLInflationRework.md#4-remove-rpl-inflation-to-odao--pdao-and-replace-with-eth-commission)

---
