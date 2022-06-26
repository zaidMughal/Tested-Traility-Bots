WALLET = 100
LOWER = 0.48
HIGHER = 0.62
NUM = 10
def initialize(state):
   state.order_amt_q = WALLET/NUM
   state.grid = [0]*NUM
   print(state.grid)


@schedule(interval="1h", symbol="ADAUSDT")
def run(state, data):
    data.aroon(14)
        
