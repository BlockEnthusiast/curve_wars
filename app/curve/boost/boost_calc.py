# min(1000 * 0.4 + 3095238 * 10000/346740720 * 0.6, 1000) ,


class Boost():
    def __init__(self):
      self.dollar_provided = 0
      self.total_liquidity = 0
      self.voting_balance = 0
      self.voting_total = 0

    def calc(self):
        temp = self.dollar_provided * (0.4/100) + self.total_liquidity * self.voting_balance / self.voting_total * ((100-40)/100)
        if temp > self.dollar_provided:
            return temp
        else
            return self.dollar_provided

    def set(self, lp, tl, vb, vt):
        self.dollar_provided = lp
        self.total_liquidity = tl
        self.voting_balance = vb
        self.voting_total = vl

class Address():
    def __init__():

# 
# class AddressRegistry():
#     def __init__():
#         self.reg = {}
#
#     def get():
#
#

class LiquitityProvision():
    def __init__(self):
      self.dollar_provided = 0

class LiquidityRegistry():
    def __init__(self):
        pass

class Gauge():
    def __init__(self):
        self.lps = []

class GaugeRegistry():
    def __init__(self):
        self.gauges = {}

class veCRV():
    def __init__(self):
        pass
