
from config import ALCHEMY

from web3 import Web3


class Web3Interace():
    def __init__(self, provider=ALCHEMY):
        self.w3 = Web3(Web3.HTTPProvider(provider))
        self.contract = None

    def checksum_address(self, address):
        return Web3.toChecksumAddress(address)

    def eth_contract(self, address, abi):
        self.contract = self.w3.eth.contract(address=address, abi=abi)

W3 = Web3Interace()
