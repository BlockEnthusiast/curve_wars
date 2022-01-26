

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
