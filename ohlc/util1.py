def is_it_inside_candle(cur,prev):
    if cur['high'] < prev['high'] and cur['low'] > prev['low']:
        return True
    else:
        return False

def test_is_it_inside_candle(data1):
    #get the candle data for inside candle scenario
    #Extract prev and current
    cur = data1[-1]
    prev = data1[-2]
    flag = is_it_inside_candle(prev, cur)
    if flag is True:
        print ('its working correctly')
    else:
        print ('failed')

    #get the candle data for asending candle scenario
    #Extract prev and current
    flag = is_it_inside_candle(prev, cur)
    if flag is False :
        print ('its working correctly')
    else:
        print ('failed')

if __name__=="__main__":
    test_is_it_inside_candle([{'open': 101, 'high': 103, 'low': 99, 'close': 100, 'volume': 1000, 'date': '2022-09-01 09:15'},
         {'open': 100, 'high': 102, 'low': 98, 'close': 99, 'volume': 500, 'date': '2022-09-01 09:16'},
         {'open': 99, 'high': 101, 'low': 97, 'close': 98, 'volume': 1000, 'date': '2022-09-01 09:17'}, ])