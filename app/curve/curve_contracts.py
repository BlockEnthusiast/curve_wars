
from ..address.address import Contract
from ..data.curve.curve_address_harvest_2022_01_22 import DATA

# Type 1 : https://etherscan.io/address/0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56#readContract
# Type 2 : https://etherscan.io/address/0xDeBF20617708857ebe4F679508E7b7863a8A8EeE#readContract
# Type 3: https://etherscan.io/address/0xA96A65c051bF88B4095Ee1f2451C2A9d43F53Ae2#readContract
class CurveSwapInterface(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()

    # type 1, 2
    def get_virtual_price(self):
        return self.contract.functions.get_virtual_price().call()

    # type 1, 2
    def calc_token_amount(self, amount, deposit):
        return self.contract.functions.calc_token_amount(amount, deposit).call()

    # type 1, 2
    def get_dy(self, i, j, dx):
        return self.contract.functions.get_dy(i, j, dx).call()

    # type 1
    def get_dx(self, i, j, dy):
        return self.contract.functions.get_dy(i, j, dy).call()

    # type 1, 2
    def get_dy_underlying(self, i, j, dy):
        return self.contract.functions.get_dy(i, j, dy).call()

    # type 1
    def get_dx_underlying(self, i, j, dy):
        return self.contract.functions.get_dy(i, j, dy).call()

    # type 1,
    # index = 0,1, etc for tokens in list
    # coins in strat
    def coins(self, index):
        return self.contract.functions.coins(index).call()

    # type 1, 2
    # index = 0,1, etc for tokens in list
    # coins raw
    def underlying_coins(self, index):
        return self.contract.functions.underlying_coins(index).call()

    # type 1, 2
    # index = 0,1, etc for tokens in list
    def balances(self, index):
        return self.contract.functions.balances(index).call()

    # type 1, 2
    def A(self):
        return self.contract.functions.A().call()

    # type 1, 2
    def fee(self):
        return self.contract.functions.fee().call()

    # type 1, 2
    def admin_fee(self):
        return self.contract.functions.admin_fee().call()

    # type 1, 2
    def admin_actions_deadline(self):
        return self.contract.functions.admin_actions_deadline().call()

    # type 1, 2
    def transfer_ownership_deadline(self):
        return self.contract.functions.transfer_ownership_deadline().call()

    # type 1
    def future_A(self):
        return self.contract.functions.future_A().call()

    # type 1, 2
    def future_fee(self):
        return self.contract.functions.future_fee().call()

    # type 1, 2
    def future_admin_fee(self):
        return self.contract.functions.future_admin_fee().call()

    # type 1, 2
    def owner(self):
        return self.contract.functions.owner().call()

    # type 1, 2
    def future_owner(self):
        return self.contract.functions.future_owner().call()

    # type 2
    def A_precise(self):
        return self.contract.functions.A_precise().call()

    # type 2
    # i, j are int
    def dynamic_fee(self, i, j):
        return self.contract.functions.dynamic_fee(i, j).call()

    # type 2
    # i is int, token_amount is uint
    def calc_withdraw_one_coin(self, token_amount, i):
        return self.contract.functions.calc_withdraw_one_coin(token_amount, i).call()

    # type 2
    # index is uint
    def admin_balances(self, index):
        return self.contract.functions.admin_balances(index).call()

    # type 2
    def offpeg_multiplier(self):
        return self.contract.functions.offpeg_multiplier().call()

    # type 2
    def future_offpeg_multiplier(self):
        return self.contract.functions.future_offpeg_multiplier().call()

    # type 2
    def lp_token(self):
        return self.contract.functions.lp_token().call()

    # type 2
    def initial_A(self):
        return self.contract.functions.initial_A().call()

    # type 2
    def future_A(self):
        return self.contract.functions.future_A().call()


class CurveDeposit(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()

class CurveGauge(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()

class CurveStaking(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()
        self.decimals = self.contract.functions.decimals().call()

class CurveAdapter(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()


class CurveRegistry():
    def __init__(self, api):
        self.contracts = {}
        self.swaps = {}
        self.tokens = {}
        self.deposits = {}
        self.gauges = {}
        self.stakings = {}
        self.adapters = {}
        self.keys = []


    def load_contracts(self):
        contracts = {}
        for k in DATA.keys():
            this = DATA[k]
            contracts[k] = {}
            keys = ['swap', 'token', 'deposit', 'gauge', 'adapter', 'staking']
            name = this['name']
            symbol = this['symbol']
            for subkey in keys:
                start = len("https://etherscan.io/address/")
                address = this[subkey][start:]
                if subkey == 'swap':
                    contract = CurveSwap(address, name + " "+subkey, symbol)
                    self.swaps[k] = contract
                elif subkey == 'token':
                    contract = CurveLPToken(address, name+ " "+subkey, symbol)
                    self.tokens[k] = contract
                elif subkey == 'deposit':
                    contract = CurveDeposit(address, name+ " "+subkey, symbol)
                    self.deposits[k] = contract
                elif subkey == 'gauge':
                    contract = CurveGauge(address, name+ " "+subkey, symbol)
                    self.gauges[k] = contract
                elif subkey == 'staking':
                    contract = CurveStaking(address, name+ " "+subkey, symbol)
                    self.stakings[k] = contract
                elif subkey == 'adapter':
                    contract = CurveAdapter(address, name+ " "+subkey, symbol)
                    self.adapters[k] = contract
                contracts[k][subkey] = contract
            self.keys.append(k)
        self.contracts = contracts
