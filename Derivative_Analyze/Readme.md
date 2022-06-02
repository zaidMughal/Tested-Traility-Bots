 ## Strategy:
This strategy is extremely simple. Let me explain first conceptually. Then I'll dive into maths. 

Even in the longer term, market trend is either bullish(upward) or bearish(downward). This bot works in longer term. If it sees market is bullish in longer term, then it invests and when the trend changes to bearish, then it sells. Trading in longer term have lesser risk than trading in short term. And to further minimize the risk, this bot trades in multiple currencies so that in case one results in loss, there are others to balance the Portfolio.

### Maths
First we calculate the exponential moving average(EMA) of past candles (Consider it as average of past N candlles with a higher weight towards later candles). This EMA roughly tells us about the trend. To make analysing the trend easier, we calculate the derivative of it(Consider it EMA[latest] - EMA[latest-1] for this case).

This derivative value is positive if trend is upward and is negative if trend is downward. We only buy a currency if trend is upward for past TREND_RANGE candles for that currency. And we sell at the first negative value of derivative.

## Results
I have tested this bot on dates from 01.06.21 to 01.06.22 (1 Year). For this period, the specified currencies gave me 66% returns. 66% return in 1 year is not bad, but certainly can be improved. 
