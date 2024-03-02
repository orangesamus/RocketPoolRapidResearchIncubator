## Megapools

Each Node can have all of their minipools under the same contract instead of requiring each minipool to have its own contract.

### Proposals:

#### 1. One megapool contract per node which acts as the withdrawal credentials for one or many validators

- Source: Kane's [megapools research post](https://github.com/rocket-pool/rocketpool-research/blob/master/Megapools/megapools.md)
- Summary:
    - Each Node uses one megapool contract for all of their minipools.
    - Capital and rewards must be split appropriately between the Node Operator and rETH users.

### Required Support:

- [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)
  - The design must be trustless and not rely on the oDAO.
  - Beacon state data must be made available to the EVM for Megapools to work trustlessly
  - EIP-4788 is included in the "Dencun" Ethereum Upgrade scheduled for March 13th, 2024
