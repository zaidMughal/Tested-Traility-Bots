# BUY_IN_ITERATION_1 constant tells if we need to buy said currency in first iteration or is it already bought. For the case of backtesting, it should be 1 as backtesting starts with no currency other than USDT
BUY_IN_ITERATION_1 = 0          # 0 for not buying
FIRST_ORDER_USDT = 50           # Amount in USDT to make first order

def initialize(state):
    state.sold = 0
    state.first_iteration = 1

@schedule(interval="1h", symbol=["ADAUSDT","BTCUSDT"])
def run(state, data):
    if isinstance(data,dict):                   # Case: If there are multiple currencies
        for currency in data:
            crypto = data[currency]
            sell_if_decline(state,crypto,currency)
    else:                                       # Case: If there is single currency
        sell_if_decline(state,data,data.symbol)

    state.first_iteration = 0                   # First iteration ended

def sell_if_decline(state,crypto,currency):
    sto = crypto.stoch(14,7,7) 
    rsi = crypto.rsi(10).last
    macd = crypto.macd(12,26,9)

    stoch_d = sto['stoch_d'].last
    stoch_k = sto['stoch_k'].last
    momentum_neg = (stoch_k < stoch_d)          # Downward momentum

    # 3 different indicators indicating downtrend in future
    if(momentum_neg and (rsi<70) and (macd["macd"].last < macd["macd_signal"].last)):
        order_market_value(currency, value=-query_balance_free("ADA"))
        state.sold = 1


    #with PlotScope.root(currency):
        #plot_line("sold",state.sold)
    
    if BUY_IN_ITERATION_1 & state.first_iteration:
        order_market_value(currency, FIRST_ORDER_USDT)
