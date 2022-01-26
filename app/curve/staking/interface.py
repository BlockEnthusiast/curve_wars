

class CurveStaking(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)
        self.activate()
        # self.decimals = self.contract.functions.decimals().call()
