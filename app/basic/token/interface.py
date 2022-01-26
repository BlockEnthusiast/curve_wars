

class TokenInterface(Contract):
    def __init__(self, address, name, symbol):
        Contract.__init__(self, address, name, symbol)

    def total_supply(self):
        return self.contract.functions.totalSupply().call()

    def allowance(self, owner, spender):
        return self.contract.functions.allowance(owner,spender).call()

    def name(self):
        return self.contract.functions.name().call()

    def symbol(self):
        return self.contract.functions.symbol().call()

    def decimals(self):
        return self.contract.functions.decimals().call()

    def balance_of(self, address):
        return self.contract.functions.balanceOf(address).call()
