from getclosevalues import closevalues
class Strategy:
    symbol = None
    def is_buy(self, values):
        return True
    def is_sell(self, values):
        return True

class User:
    def __init__(self, id, username, balance, risk_perc, profit_perc):
        self.id = id
        self.username = username
        self.balance = balance
        self.risk_perc = risk_perc
        self.profit_perc = profit_perc

class Trend:
    up='u'
    down = 'd'
    sideways='s'

class Strength:
    weak=1
    normal=2
    strong = 3

class PredData:
    def __init__(self, symbol = 'Niftybank', entryat=0, direction = Trend.sideways, exit = 0, trend_strength=Strength.normal, stoploss=200):
        self.symbol = symbol
        self.entryat = entryat # we need will get after avg is calculated
        self.exit = exit # after the loss is greater than balance*risk_amt
        self.direction = Trend # requires the close data
        self.trend_strength= trend_strength # requires the close data
        self.stop_loss=stoploss #balance*risk_amt

    def getpredictiondata(self):
        gc=closevalues()
        close_values=gc.closevaluesfn()
        return close_values

class Prediction:
    def __init__(self, symbol='BANKNIFTY'):
        pass
    def get_prediction(self):
        return PredData()



class StrategyHelper:
    def __init__(self):
        pass
    def get_strategy(self, pred_data):
        if pred_data.direction == Trend.up:
            return Strategy()
        elif pred_data.direction == Trend.down:
            return Strategy()

class UserStrategy:
    def __init__(self, user, positions, strategy, pred_data=None):
        self.user = user
        self.positions = positions
        self.strategy = strategy
        if pred_data is not None:
            self.update(pred_data)

    def update(self, pred_data):
        #Based on the user's available amount, and strategyid, calculate the max qty that can be traded
        #Calculate the risk, reward for each qty

        #consider the user's risk level, and amount available
        #consider user's positions
        pass

class Impl:
    def __init__(self):
        self.broker = Broker()
    
    def execute(self, user_strategy):
        #Based on the user's available amount, and strategyid, calculate the max qty that can be traded
        #Calculate the risk, reward for each qty

        #consider the user's risk level, and amount available
        #consider user's positions
        self.broker.Buy()
    def run_continuosly(self):
        for i in range(2000):
            self.execute()

class Broker:
    def Buy(self, symbol, qty, price):
        #update the positions
        positions = {'symbol': 0, 'qty': 0, 'price': 0}
        pass
    def Sell(self, symbol, qty, price):
        pass
    def GetPositions(self):



user = User(1, "Rahul", 20000, 0.02, 0.05)
positions = Broker().GetPositions()
pred_data = Prediction().get_prediction()
strategy = StrategyHelper().get_strategy(pred_data)
user_strategy = UserStrategy(user, positions, strategy, pred_data)
Impl().execute(user_strategy)



# Depending on the strength, set the qty accordingly
# How to findout the strength: Based on the angle of the close values graph
