import os
import json
from ... utility.api import etherscan_abi
from ... utility.local_storage import read_json, write_json
from ... utility.w3 import W3
from .. address.interface import AddressInterface


class ContractInterface(AddressInterface):
    def __init__(self, address, name, symbol):
        self.abi = None
        self.contract = None
        AddressInterface.__init__(self, address, name, symbol)

    def activate(self):
        self._get_abi()
        if self.abi:
            self.contract = W3.eth_contract(self.address, self.abi)
            return True
        else:
            return False

    def _get_abi(self):
        abi = read_json("/abis/"+self.address)
        if not abi:
            abi = etherscan_abi(self.address)
            if abi:
                write_json("/abis/"+self.address, abi)
            else:
                return False
        # else:
        #     abi = json.dumps(abi, indent=4)
        self.abi = abi
