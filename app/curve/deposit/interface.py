from ...basic.contract.models import Contract

class CurveDepositInterface(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()

    def calc_withdraw_one_coin(self, token_amount, i):
        return self.contract.functions.calc_withdraw_one_coin(token_amount, i)

    def coins(self, index):
        return self.contract.functions.coins(index)

    def underlying_coins(index):
        return self.contract.functions.underlying_coins(index)
