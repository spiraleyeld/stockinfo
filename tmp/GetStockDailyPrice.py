# -*- coding:utf-8 -*-
import requests as r
import pandas as pd
import dataframe as df
from bs4 import BeautifulSoup
import re
import json
import pyodbc



print('Let us to Get Data!!!')
### Get Data
json_data=r.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210201&stockNo=3481').json()

columns= ['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data=pd.DataFrame(json_data['data'],columns=columns)

print('Let us to Clear Data!!!')
### Clear Data
data['日期']=data['日期'].apply(lambda x: re.sub('(\d+)(/\d+/\d+)',lambda y: str(int(y.group(1))+1911)+y.group(2),x))
data[['成交股數','成交金額','成交筆數']]=data[['成交股數','成交金額','成交筆數']].applymap(lambda x:x.replace(',',''))
data.iloc[:,1:]=data.iloc[:,1:].applymap(float)
data[['成交股數','成交金額']]=data[['成交股數','成交金額']]/1000


### Assign Specific Column to Dataset



# Insert Dataframe into SQL Server:
server = 'USER-PC\AWEILIN' 
database = 'GSTOCK' 
username = 'GSa' 
password = '1234' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("INSERT INTO [StockDailyPrice] (YearID) values(?)", 2021)
cnxn.commit()
cursor.close()

print(data)