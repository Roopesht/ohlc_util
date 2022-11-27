#from trade import PredData
#from trade import User
class closevalues:
    def closevaluesfn(self):
        import csv
        l1=[]
        close_values=[]
        m=1
        with open("ohlcdata.csv", newline='') as csvfile:
            filereader = csv.reader(csvfile)
            l = list(filereader)
            for n in range(1, len(l)):
                d = {}
                for m in range(1, 7):
                    d[l[0][m]] = l[n][m]
                l1.append(d)
        for i in range(0,len(l1)):
            close_values.append(l1[i]['close'])
        return close_values

    def getentryvalue(self):
        close_values=self.closevaluesfn()
        j=2
        while j != len(close_values):
            avg = sum(close_values[0:j]) / j

            if float(close_values[j]) > avg:
                return close_values[j]
            else:
                continue

    def getexitvalue(self):
        userdata=User(1, "Rahul", 20000, 0.02, 0.05)
        if cum_loss> userdata.balance*userdata.risk_perc:
            return close_value_at_that_point

    def getdirection(self):
        close_values=self.closevaluesfn()
        close_values_test=close_values[:]
        if sorted(close_values_test)==close_values:
            return 'up'
        elif sorted(close_values_test, reverse=True)==close_values:
            return 'down'
        else:
            return 'mixed'

