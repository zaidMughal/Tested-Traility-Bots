INTERVAL = "6h"
SYMBOL = ["BTCUSDT","BNBUSDT", "SOLUSDT", "XRPUSDT","NEARUSDT","ROSEUSDT"]      #All currencies this bot will trade upon
EMA_PERIOD = 60         #How many past candles will we see while calculating EMA
TREND_RANGE = -30       #Past EMA of how many periods will we see to decide future trend

'''
INTERVAL = "12h"     #For testing
SYMBOL = ["BTCUSDT","BNBUSDT", "SOLUSDT", "XRPUSDT","NEARUSDT","ROSEUSDT"]
TREND_RANGE = -15'''

#working on 6h, 60, -30
#bnb PEAK AT 70
#ADA peak at 60 (70 also works)
#ETH peak at 50
#BTC peak at 60

def initialize(state):
    state.num_curr = len(SYMBOL)    #Num of currencies
    state.buy = dict()
    for currency in SYMBOL:
        state.buy[currency] = 0     #Have we bought this currency or not

@schedule(interval=INTERVAL, symbol=SYMBOL)
def run(state, data):
        
    for currency in data:
        crypto_data = data[currency]

        ema = crypto_data.ema(period=EMA_PERIOD , select="close")
        buy= 1
        for i in range(-1,TREND_RANGE,-1):      #-1,-2,-3,...TREND_RANGE
            der = ema[i]-ema[i-1]   #Since time period is constant, we don't need to divide by interval
            if der < 0:             #Make sure ema is increasing from past TREND_RANGE candles
                buy = 0
                break

        if (ema[-1] < ema[-2]) and (state.buy[crypto_data.symbol] == 1):       #sell
            order_market_amount(crypto_data.symbol, amount=-query_balance_free(crypto_data.base))
            state.buy[crypto_data.symbol] = 0

        if buy and (state.buy[crypto_data.symbol] == 0):    #Buy if signaled and not already bought
            value=query_balance_free("USDT")/state.num_curr
            value = value if value >15 else 15
            order_market_value(symbol=crypto_data.symbol, value=value)
            state.buy[crypto_data.symbol] = 1
        

        with PlotScope.group("my_group", crypto_data.symbol):
            plot_line("derivative_div",(ema[-1]-ema[-2])*100/crypto_data.close_last,crypto_data.symbol)
            #Comparatively normalized graph for derivative
