#Buy/sell a stock on a condition
#Condition for buying
#1. The trend is up
#2. The price is near the lower band
#Condition for selling
#1. The trend is down OR
#2. The price is near the upper band
from levels import Trend, BUYSELL, Order
from helper_ks import HelperKS
import redis_util as r
import time

class technical: 
    def __init__(self, trend=Trend.sideways, price=0.0, lower_band=0.0, upper_band=0.0):
        self.trend = trend
        self.price = price
        self.lower_band = lower_band
        self.upper_band = upper_band

class position:
    def __init__(self, stock, price, qty):
        self.stock = stock
        self.price = price
        self.qty = qty
    def update(self, b_or_s:BUYSELL, qty:int, price:float):
        if b_or_s == BUYSELL.BUY:
            self.price = (self.price * self.qty + price * qty)/(self.qty + qty)
            self.qty += qty
        elif b_or_s == BUYSELL.SELL:
            self.qty -= qty
            if self.qty == 0:
                self.price = 0

class strategy:
    def __init__(self, broker, stock):
        self.stock=stock
        self.broker = broker
        self.position = position(stock, 0, 0)
    def buy(self, stock, qty, price):
        o = Order(stock, stock, BUYSELL.BUY, qty, price, 'Test buy', code=405)
        self.broker.placeOrder(o)
    def sell(self, stock, qty, price):
        o = Order(stock, stock, BUYSELL.SELL, qty, price, 'Test sell')
        self.broker.placeOrder(o)

    def execute(self, tech:technical):
        print ('Executing buy/sell')
        buy_flag = False
        if tech.trend == Trend.up:
            if tech.price < tech.lower_band + 1:
                if self.position.qty == 0:
                    buy_flag = True
        
        if buy_flag:
            qty = 25
            print (f'Buying @{tech.price}, qty: {qty}')
            self.buy(self.stock, qty, tech.price)
            self.position.update(BUYSELL.BUY, qty, tech.price)
        else:
            print('buy condition not met')
                
        if self.position.qty > 0:
            if tech.price > tech.upper_band - 1:
                print('Selling')
                self.sell(self.stock, self.position.qty, tech.price)
                self.position.update(BUYSELL.SELL, self.position.qty, tech.price)



        #Check the trend
        #Check the price
        #Check the position
        #Buy or sell
        pass

if __name__ == '__main__':
    broker = HelperKS(19)
    kitetoken = '14643970'
    bs = strategy(broker, kitetoken) #17892

    for counter in range(0, 10000):
        price =  float(r.get_dict('tickdata')[kitetoken])
        #Get the upper band and lower band
        mindata = r.getmindata(1, kitetoken)
        print (mindata)

        t = technical(Trend.up, price, float(mindata['lbb']), float(mindata['ubb']))
        print (f" Price: {price}, Lower band: {mindata['lbb']}, Upper band: {mindata['ubb']}")
        time.sleep(1)

        bs.execute(t)
