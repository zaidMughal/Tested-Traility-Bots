# Tested-Traility-Bots
## Prerequosite
1. You should have basic idea of what are cryptocurrencies and what is meant by cryptocurrency trading.
2. You should be familiar with python as trality bots are written in python.
3. 

## Overview
Crypto is certainly growing now a days and it is giving unthinkable profits to some while dumping savings of many. And one of the major cause of this loss is that many people invest in crypto without having any core strategies. And sad part is that strategies that does work like Portfolio balancing or dollar cost averiging etc, mostly require a lot of Capital, which common folks don't have.

So how to invest in crypto, with little capital and also have a fairly good chance of making profits?
1. One way is to keep updated with most of the information going around in crypto market. But that requires a lot of time.
2. Another way is to join groups that post crypto signals regularly. I tried this method, but didn't saw satisfactory gains. Reasons being that I cannot deduce among all the given signals, which one is a strong signal or which one is weak signal. For that you need a fair amount of information yourself. Another reason being that since market is unpredictable, a signal could go wrong anytime, but a person with no information cannot detect this reversal before his loss.
3. Another way is using crypto bots. But many of the profitable bots, again, implements capital intensive strategies, so bots that can work with low capital and can still turn in profits are rarity. Other than that there is a setup cost of bots that involves renting a server to run it as well as basic knowledge of how to run it. But what if you aren't sure if it will turn in profits? It all makes using a bot all the more hard. Indeed you can also use pre-built and pre-tested bots from cryptohopper etc, but they are costly and you can't test them before buying.

### What Trality offers
Most of our above mentioned problems related to bots are solved by trality.    
1. NO Initial fee: There is no need to rent hosting or make your laptop run 24/7. Trality itself runs all bots. Although buying a membership increases our options, the free version still gives us plenty.
2. Run only tested bots: Trality provides the backtesting interface. It means that you can test your bot on previous data of any cryptocurrency and make amends to your bot untill you are satisfied by its performance. Then deploy only the proven bots. More information on backtesting is below
3. Easy deployment: Out of all the websites/bots I tried, running a bot in trality is far easier and faster than any other option due to it being perticularly engineered to run bots.
4. Custom strategies: Since we ourselves are making it, we can tune some strategies to work with low capital or high capital or even capital neutral.

## What this Repository contain
The approach of this repository is that every folder is of the name of the bot it contains. And in that folder, there will be a pythone file that contains that bot as well as the Readme.md that explains in detail what strategy is implemented in that bot, what profit percentages are achieved in which conditions(upward, downward and sideways) and any further explanation needed by that bot.


## How to test/Deploy
### Making a bot
0. Prerequisite: An account on any crypto exchange listed by traility(e.g. Binance,...).
1. Go to https://app.trality.com/ and make your account
2. Then go to home page and click "Create"
3. In the popup, select
  a. "code" as bot type as we will bot using python code (Other option is rule bot, but it is not related to us).
  b. Type name of new  bot
  c. Select exchange on which you made account earlier
  d. Select USDT as base/quoted currency 
  e. Press "Create"
4. Copy the code of bot you want to run and paste it in code editor. It will be saved automatically. Then backtest it just in case(Button is in sidebar)
5. Goto to dashboard and activate the bot.
  
### Backtesting
Backtesting means applying a strategy to historical data to determine its accuracy. It can be used to test and compare the trading strategies so traders can employ successful strategies. More info on [Backtesting](https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/backtesting/).

While editing the code of your bot, there is a backtesting button in the right coloumn. That can be used to backtest for a limited time. The time range is adjustable. You can even test for specific scenarios like "downward", "upward" and "sideways".
(Note: Backtesting does not gurentee future results)




## Contribution guide

