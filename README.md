# Swap Wrapped Tokens

This repo contains scripts to swap wrapped tokens using brownie.

The [WETH contract](https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2) provides an interface that allows us to convert WETH to ETH
and vice versa.

This should work for other wrapped tokens too, like WMATIC.

## Setup

1. `touch .env`
2. add you private key `export PRIVATE_KEY=0x...`
3. add your [infura](https://infura.io/) key `export WEB3_INFURA_PROJECT_ID=...`
4. `source .env`

## Script

The conversion script is located at `scripts/wrapped-eth.py`

You only need to modify the const `AMOUNT` at the top of the file to your preference.

## Convert WETH to ETH

We are minting ETH from WETH.

Example

```
brownie run scripts/wrapped-eth.py --network kovan get_eth
```

## Convert ETH to WETH

We are minting WETH from ETH.

Example

```
brownie run scripts/wrapped-eth.py --network kovan get_weth
```
