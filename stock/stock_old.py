import tushare as ts
import datetime
import base
import sys

sort_key = 3
def sort_stock(elem):
    return elem[sort_key]


today = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().strftime("%Y-%m-%d")
# today = "2019-06-03"
stock = []
code = ('002119', '600352', '300099', '600093', '000159', '600290', '601860', '300265', '002847', '002930', '300519', '603259', '601138', '600929', '600549', '600581', '300505', '300644', '600128', '600606', '002905')
#print(ts.get_hist_data('sh000001'))
for i in code:
    stockInfo = base.getStockInfo(i)
    data = ts.get_hist_data(i, today, today)
    #print(data)
    #data = ts.get_k_data('sz002930', today)
    #print(data)
    daily = data.iloc[0]
    #print(daily)
    #gap_ma5 = (daily.loc['ma5']/daily.loc['close']-1)*100 if daily.loc['ma5']>=daily.loc['close'] else 'false'
    #gap_ma10 = (daily.loc['ma10']/daily.loc['close']-1)*100 if daily.loc['ma10']>=daily.loc['close'] else 'False'
    #gap_ma20 = (daily.loc['ma20']/daily.loc['close']-1)*100 if daily.loc['ma20']>=daily.loc['close'] else 'False'
    gap_ma5 = round((daily.loc['close']/daily.loc['ma5']-1)*100, 2)
    gap_ma10 = round((daily.loc['close']/daily.loc['ma10']-1)*100, 2)
    gap_ma20 = round((daily.loc['close']/daily.loc['ma20']-1)*100, 2)
    #print((stockInfo['name'], gap_ma5, gap_ma10, gap_ma20))
    stock.append((i, stockInfo['name'], gap_ma5, gap_ma10, gap_ma20))

stock.sort(key=sort_stock)
#print(stock)

file = today + '_stock.txt'
f = open(file, 'wt', encoding= 'utf-8')

for s in stock:
    for c in s:
        f.write(str(c))
        f.write('\t')
    f.write('\n')

f.close() 

#print(daily)
#print(type(daily))
#print(ts.realtime_boxoffice())
#data['new'] = data.apply(lambda x: ((1)?x.loc['ma20'] / x.loc['close'] - 1 : false), 1)
#data['gap_ma5']=data.apply(lambda x: (x.loc['ma5']/x.loc['close']-1)*100 if x.loc['ma5']>=x.loc['close'] else False, 1)
#data['gap_ma10']=data.apply(lambda x: (x.loc['ma10']/x.loc['close']-1)*100 if x.loc['ma10']>=x.loc['close'] else False, 1)
#data['gap_ma20']=data.apply(lambda x: (x.loc['ma20']/x.loc['close']-1)*100 if x.loc['ma20']>=x.loc['close'] else False, 1)
#print(data[['gap_ma5','gap_ma10','gap_ma20']])
