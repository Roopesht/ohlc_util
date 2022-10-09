from csvupload import csv1
def is_it_inside_candle(l1, nd):
    unsorted_list1=[]
    unsorted_list2=[]
    for i in range(nd,-1,-1):
        unsorted_list1.append(l1[i]['high'])
        unsorted_list2.append(l1[i]['low'])
    m=0
    n=1
    for i in range(0,len(unsorted_list1)-1):
        if unsorted_list1[m]<unsorted_list1[n] and unsorted_list2[m]>unsorted_list2[n]:
            m=m+1
            n=n+1
            continue
        return True

    return False

if __name__=="__main__":
    dic=csv1.csvfile()
    dic1=dic[::-1]
    is_it_inside_candle(dic, 221)
    flag = is_it_inside_candle(dic, 221)
    if flag is True:
        print('its working correctly')
    else:
        print('failed')

    flag = is_it_inside_candle(dic1, 3)
    if flag is False:
        print('its working correctly')
    else:
        print('failed')



