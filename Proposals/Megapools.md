## Megapools

Each Node can have all of their minipools under the same contract instead of requiring each minipool to have its own contract.

### Proposals

#### 1. One megapool contract per node which acts as the withdrawal credentials for one or many validators

- Source: Kane's [megapools research post](https://github.com/rocket-pool/rocketpool-research/blob/master/Megapools/megapools.md)<sup>\*</sup>
- Summary:
    - Each Node uses one megapool contract for all of their minipools.
    - The design must be trustless and not rely on the oDAO.
    - Beacon state data must be made available to the EVM (with EIP-4788) to distinguish between capital and rewards.
    - Capital and rewards must be split appropriately between the Node Operator and rETH users.
- Benefits:
    - Massive improvements to gas efficiency when running more than one minipool.
- Drawbacks:



#### Required Support

1. [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)<sup>\*</sup>

#### Notes

<sup>\*</sup>EIP-4788 is required for Megapools. EIP-4788 is included in the "Dencun" Ethereum Upgrade scheduled for March 13th, 2024
