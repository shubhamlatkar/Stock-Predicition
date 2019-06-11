'''import pandas as pd
import numpy as np
#from Models.Regression import Regressor
import pandas_datareader.data as web
from datetime import datetime
#from Models.MyLSTM import LSTM
#from Models.FBProphet import FBProphet
import plotly as py
import plotly.graph_objs as go




df = web.DataReader('COKE', 'yahoo', datetime(2018,1,1),datetime.now() )
data = [go.Scatter( x=df.index, y=df['Close'] )]
print(py.offline.plot(data ,include_plotlyjs=False, output_type='div'))

#obj = FBProphet()
#obj.myProphet(df)


import bs4
from bs4 import BeautifulSoup 
from urllib.request import urlopen
import json

news_url="https://stocknewsapi.com/api/v1/category?section=alltickers&items=50&token=o8vaufrrmuoe07fcnyjjaom9xjavklrrp5pqpsju"
Client=urlopen(news_url)
content=Client.read()
Client.close()

soup = BeautifulSoup(content)

newDictionary=json.loads(str(soup))
print(newDictionary)

soup_page=soup(xml_page,"json")
news_list=soup_page.findAll("item")

for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)


import pickle
import requests
news_url="https://stocknewsapi.com/api/v1?tickers=TSLA&items=50&token=o8vaufrrmuoe07fcnyjjaom9xjavklrrp5pqpsju"
json_data = requests.get(news_url).json()
f = open("file.pkl","wb")
pickle.dump(dict,f)
f.close() 
'''


import json
import requests
news_url="https://stocknewsapi.com/api/v1?tickers=TSLA&items=50&token=o8vaufrrmuoe07fcnyjjaom9xjavklrrp5pqpsju"
json_data = requests.get(news_url).json()
json = json.dumps(json_data)
f = open("file.json","w")
f.write(json)
f.close()

