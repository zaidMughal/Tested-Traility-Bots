 ## Strategy:
Let me put up a situation. Imagine you predicted ADA coin would start increasing in value and will keep on increasing for some days. You buy it, wait some reasonable time and then sell them at profit. But then you observe that ADA/USDT still keeps on increasing in value and you can't buy it again because you are uncertain of the situation.

In a similar case, lets assume you predicted the same things about ADA coins as in the previous paragraph, and you went to sleep imagining your ADA coins would continue to increase in value overnight. But then some unpredicted situation happens and you wake up with your ADA coins going in downtrend.

Both of these situation could be avoided if there could be a bot that would oversee your portfolio and would sell specified cryptocurrencies if it sees a shift from uptrend to downtrend. This is exactly what this bot does. 

The idea is that user would buy the specific coins that are showing rise in price and the user predicts would continue to show rise for some hours atleast. After buying those coins, the user would specify the coin in bot then activate/deploy it. The bot would continue to watch over the conversion rate of specified coins. Whenever it will detect a downtrend, it will make a market order to sell all(adjustable) coins.

As for how the bot deduce that market is declining and it is time to sell the coins, it uses three different indicators in series. These indicators are:
1. RSI
2. STOCHASTIC
3. MACD

The reason of using three different indicators is that we can be sure of market trend. The bot sells only if all of above indicators show a downtrend.
