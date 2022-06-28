#Step 1: Make grid bot with defined limits
#Step 2: Make grid bot with limits calculated automatically
#Step 3: Add a trend detecting mechanism that only turns on trading when market is moving sideways


WALLET = 100
LOWER = 0.48
HIGHER = 0.62
NUM = 10

def initialize(state):
   state.order_amt_quoted = WALLET/NUM

   state.grid = [0] * NUM
   margin_price = LOWER
   grid_step_base_currency = (HIGHER - LOWER)/NUM
   for margin in state.grid:
       print(state.grid)
       #margin.order = 0
       #margin.price = margin_price
       #margin_price = margin_price - grid_step_base_currency

    


@schedule(interval="1h", symbol="ADAUSDT")
def run(state, data):
    curr_price = data.close_last
