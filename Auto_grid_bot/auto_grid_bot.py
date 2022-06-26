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
