# Example-NFT-mint-with-The-Blockchain-API

This is a simple working demonstration of using [The Blockchain API's](https://theblockchainapi.com/) Python wrapper to script the creation of an NFT to an existing Solana wallet.

To run:
```
$ python3 example.py
```

See code comments for details and prereqs.

The code assumes the wallet already exists and was created using the Solana CLI. (This is a variation from the [official example code](https://github.com/BL0CK-X/the-blockchain-api/blob/main/examples/solana-wallet/derive-public-key/python_example.py) that existed at the time I needed to do this.)

The example code uses JSON metadata already uploaded to Arweave for the NFT's assets. For your own NFT you should already have your NFT's assets already uploaded to a service such as Arweave or IPFS and change the link to that.

The example JSON metadata is also in this repo as a convenient reference/example, see `example.nft.json`.

Many thanks to [Josh Wolf](https://github.com/joshwolff1) over at [The Blockchain API](https://theblockchainapi.com/) for all the help!
