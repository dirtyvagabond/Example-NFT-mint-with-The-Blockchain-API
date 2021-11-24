#
# This is an example Python script that uses The Blockchain API to mint a
# single NFT piece into the specified wallet. It assumes you already have:
#
#   * The assets hosted somewhere, including the NFT metadata in the form of
#     a Metaplex compliant JSON. See METADATA_JSON_LINK
#
#   * A Solana wallet, preferably created by the Solana CLI, along with
#     its seed phrase. See SECRET_KEY
#
# You will need to install the official Python wrapper for The Blockchain API:
# https://github.com/BL0CK-X/the-blockchain-api-python-wrapper
#
# The following code was adapted from this official example...
# https://github.com/BL0CK-X/the-blockchain-api/blob/main/examples/solana-nft/create-an-nft/python_example.py
# ... and some much appreciated help from Josh Wolff
#
from theblockchainapi import TheBlockchainAPIResource, SolanaCurrencyUnit, SolanaNFTUploadMethod

# URL to your NFT metadata as Metaplex compliant JSON
# Change this to be yours (hosted on, e.g., Arweave or IPFS)
METADATA_JSON_LINK =  "https://arweave.net/rWZ1_TNBVjaa7SVDii8IDltQew737fDoV0Ac2kDP12U"

NFT_SYMBOL = "MYNFT"
NFT_NAME = "My Nft"

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = "TODO"
MY_API_SECRET_KEY = "TODO"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

# Your wallet (and the destination of the minted NFT)
# Read about security here:
#   https://docs.theblockchainapi.com/#section/Security
SECRET_KEY = 'TODO: change this to your minting wallet secret phrase'


def mint(json_link):
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # Initialize a Wallet using a known secret phrase, from
    # a wallet created using the Solana CLI
    # Read about security here:
    #   https://docs.theblockchainapi.com/#section/Security
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase=SECRET_KEY,
        derivation_path='' # blank, necessary for wallet created via Solana CLI
    )
    print("Wallet: " + public_key)

    # Mint an NFT
    nft = BLOCKCHAIN_API_RESOURCE.create_nft(
        secret_recovery_phrase=SECRET_KEY,
        derivation_path='', # blank, necessary for wallet created via Solana CLI
        nft_upload_method=SolanaNFTUploadMethod.LINK,
        nft_symbol=NFT_SYMBOL,
        nft_name=NFT_NAME,
        nft_url=json_link,
        is_mutable=False,
    )
    return nft


if __name__ == '__main__':
    nft = mint(METADATA_JSON_LINK) # you'd change this for each NFT
    print("NFT: ", nft)
    print(f"You can view the NFT here: {nft['explorer_url']}")
    print("The NFT should also be visible in your wallet")
