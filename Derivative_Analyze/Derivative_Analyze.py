STOCH_UPPER_THRESH = 75
STOCH_LOWER_THRESH = 25
STOCH_THRESH = 7

#working on 6h, -30
@schedule(interval="6h", symbol="ADAUSDT")
def run(state, data):
    ema21 = data.ema(period=50, select="close")

    buy= 1
    for i in range(-1,-30,-1):
        der = ema21[i]-ema21[i-1]
        if der < 0:
            buy = 0
            break
    if buy:
        order_market_value(symbol=data.symbol, value=query_balance_free("USDT"))
    
    if (ema21[-1]-ema21[-2]) < 0:       #sell
        order_market_amount(data.symbol, amount=-query_balance_free("ADA"))

    with PlotScope.group("my_group", data.symbol):
        plot_line("der",ema21[-1]-ema21[-2],data.symbol)
        plot_line("0",0,data.symbol)
   
