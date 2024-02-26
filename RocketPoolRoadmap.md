## Rocket Pool Roadmap

### Introduction

The goal of this page is to present an outline of the Rocket Pool Roadmap, including proposals being considered for inclusion.

### Table Of Contents

- [Rocket Pool Roadmap](#rocket-pool-roadmap)
  - [Introduction](#introduction)
  - [Table Of Contents](#table-of-contents)
  - [Summary](#summary)
  - [Planned for Integration](#planned-for-integration)
    - [1. Houston](#1-houston)
      - [Proposals](#proposals)
      - [Required Support](#required-support)
      - [Notes](#notes)
    - [2. Saturn](#2-saturn)
      - [Proposals](#proposals-1)
      - [Notes](#notes-1)
  - [Considering for Inclusion](#considering-for-inclusion)
    - [1. Megapools](#1-megapools)
      - [Proposals](#proposals-2)
      - [Required Support](#required-support-1)
      - [Notes](#notes-2)
    - [2. Sublinear Bonding](#2-sublinear-bonding)
      - [Proposals](#proposals-3)
      - [Required Support](#required-support-2)
      - [Recommended Support](#recommended-support)
      - [Notes](#notes-3)
    - [3. RPL Value Capture](#3-rpl-value-capture)
    - [4. Universal Variable Commission](#4-universal-variable-commission)
    - [5. rETH Protection](#5-reth-protection)
    - [6. Forced Exits](#6-forced-exits)
      - [Proposals](#proposals-4)
      - [Required Support](#required-support-3)
      - [Notes](#notes-4)
    - [7. RPL Inflation Rework](#7-rpl-inflation-rework)
      - [Proposals](#proposals-5)

### Summary

The outline includes two main sections:

1. [Planned for Integration](#planned-for-integration):
   1. These proposals have been voted and approved by the pDAO.
   2. These proposals are grouped by the Rocket Pool upgrade in which they plan to be integrated.
2. [Considering for Inclusion](#considering-for-inclusion):
   1. This section is categorized first by topic, with each topic listing the proposals being considered for inclusion.
   2. These proposals may not have an RPIP yet and it is uncertain which Rocket Pool upgrade they will be included in (if at all).
   3. This outline does not provide an exhaustive list of all proposals or research ideas, but instead prioritizes ideas being considered for inclusion.

### Planned for Integration

---

#### 1. Houston

##### Proposals

1. [RPIP-31: RPL Withdrawal Address](https://rpips.rocketpool.net/RPIPs/RPIP-32)
2. [RPIP-32: Stake ETH on behalf of node](https://rpips.rocketpool.net/RPIPs/RPIP-32)
3. [RPIP-33: On-Chain pDAO](https://rpips.rocketpool.net/RPIPs/RPIP-33)<sup>\*</sup>

##### Required Support

1. [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)<sup>\*</sup>

##### Notes

<sup>\*</sup>EIP-4788 is required for RPIP-33. EIP-4788 is included in the "Dencun" Ethereum Upgrade scheduled for March 13th, 2024

---

#### 2. Saturn

##### Proposals

1. [RPIP-28: Deposits Under the Minimum](https://rpips.rocketpool.net/RPIPs/RPIP-28)
2. [RPIP-30: RPL Staking Rework](https://rpips.rocketpool.net/RPIPs/RPIP-30)<sup>\*</sup>
3. [RPIP-35: Time-based Balance and RPL Price Submissions](https://rpips.rocketpool.net/RPIPs/RPIP-35)

##### Notes

<sup>\*</sup>Rewards rework has already implemented by the oDAO, but unstaking rework requires smart contract changes and has not been implemented yet

---

### Considering for Inclusion

---

#### 1. Megapools

##### Proposals

1. [One megapool contract per Node Operator which acts as the withdrawal credentials for one or many validators](https://github.com/rocket-pool/rocketpool-research/blob/master/Megapools/megapools.md)<sup>\*</sup>

##### Required Support

1. [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)<sup>\*</sup>

##### Notes

<sup>\*</sup>EIP-4788 is required for Megapools. EIP-4788 is included in the "Dencun" Ethereum Upgrade scheduled for March 13th, 2024

---

#### 2. Sublinear Bonding

##### Proposals

1. [First two minipools are LEB4’s, thereafter allow LEB1.5's](/Proposals/SublinearBonding.md#1-first-two-minipools-are-leb4s-thereafter-allow-leb15s)<sup>\*†‡</sup>

##### Required Support

1. [Forced Exits](#5-forced-exits)<sup>\*</sup>
2. [EIP7002: Execution Layer Triggerable Exits](https://eips.ethereum.org/EIPS/eip-7002)<sup>†</sup>

##### Recommended Support

1. [rETH Protection](#4-reth-protection)<sup>‡</sup>

##### Notes

<sup>\*</sup>With sublinear bonding, Forced Exits are critical to protect against loss scenarios associated with MEV theft and abandonment

<sup>†</sup>EIP-7002 is required for Forced Exits. EIP-7002 is tentatively planned for integration in the "Pectra" Ethereum Upgrade which is tentatively scheduled for ~Q4 2024

<sup>‡</sup>As we increase leverage by allowing sublinear bonding, it becomes more important to protect rETH from underperforming NO's

---

#### 3. RPL Value Capture

---

#### 4. Universal Variable Commission

---

#### 5. rETH Protection

---

#### 6. Forced Exits

##### Proposals

1. [Exit a validator when a NO's (total_leakage + debt) > 0.5 ETH](/Proposals/ForcedExits.md#1-exit-a-validator-when-a-nos-total_leakage--debt--05-eth)<sup>\*</sup>

##### Required Support

1. [EIP7002: Execution Layer Triggerable Exits](https://eips.ethereum.org/EIPS/eip-7002)<sup>\*</sup>

##### Notes

<sup>\*</sup>EIP-7002 is required for Forced Exits. EIP-7002 is tentatively planned for integration in the "Pectra" Ethereum Upgrade which is tentatively scheduled for ~Q4 2024

#### 7. RPL Inflation Rework

##### Proposals

1. [Change RPL Inflation to NO's to distribute by Borrowed ETH](/Proposals/RPLInflationRework.md#1-change-rpl-inflation-to-nos-to-distribute-by-borrowed-eth)
2. [Remove RPL Inflation to NO's](/Proposals/RPLInflationRework.md#2-remove-rpl-inflation-to-nos)
3. [Remove RPL Inflation to oDAO & pDAO and replace with ETH commission](/Proposals/RPLInflationRework.md#3-remove-rpl-inflation-to-odao--pdao-and-replace-with-eth-commission)

---