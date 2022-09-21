from csvupload import csv1


'''
This function takes 2 parameters
l1 - the list of candles in dict format, 
nd - the number of candles to verify

Returns boolean if they are in ascending order
'''

def is_it_ascending(l1, nd):
    #Filter only the last number of rows required
    l1_filtered = l1[len(l1)-nd: len(l1)-1]
    high_list = [a['high'] for a in l1_filtered]
    low_list = [a['low'] for a in l1_filtered]

    high_sorted = sorted( high_list.copy())
    low_sorted = sorted( low_list.copy())

    if high_list == high_sorted and low_list == low_sorted:
        return True
    else:
        return False


if __name__ == "__main__":

    dic = csv1.csvfile()
    dic1=dic[::-1]
    is_it_ascending(dic, 3)
    flag = is_it_ascending(dic, 3)
    if flag is True:
        print('its working correctly')
    else:
        print('failed')

    flag = is_it_ascending(dic1, 3)
    if flag is False:
        print('its working correctly')
    else:
        print('failed')



