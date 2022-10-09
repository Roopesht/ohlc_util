class csv1:
    def csvfile():
        import csv
        d={}
        l1=[]
        m=1
        with open("ohlcdata.csv",newline='') as csvfile:
            filereader=csv.reader(csvfile)
            l=list(filereader)
            for n in range(1,len(l)):
                d={}
                for m in range(1,7):
                    d[l[0][m]]=l[n][m]
                l1.append(d)
            return l1

if __name__ == "__main__":
    c=csv1()
