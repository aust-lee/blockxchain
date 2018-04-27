
# coding: utf-8

# ## This notebook pulls pricing information from Coinmarketcap $$$ 

# ### Data will consist of information from ranks, coins, stats, new coins, trends, and events

# In[42]:


from pymarketcap import Pymarketcap
import re
import json
import pprint
import pandas as pd
import requests
from datetime import datetime, timedelta 
from bs4 import BeautifulSoup
import urllib3
import time
import logging
import numpy as np
from apscheduler.schedulers.blocking import BlockingScheduler
import re
import urllib.request
import numpy as np
pd.options.display.float_format = '{:20,.2f}'.format


# ##### Defines a function that allows for replacement for new coin date added

# In[43]:


def setdate(x):
    if len(x) == 5 or len(x) == 7:
        return datetime.today().strftime("%m/%d/%Y")
    elif len(x) == 8:
        newDate = datetime.today() - timedelta(days=int(x[:1]))
        return newDate.strftime("%m/%d/%Y")
    else:
        newDate = datetime.today() - timedelta(days=int(x[:2]))
        return newDate.strftime("%m/%d/%Y")


# ###### Sets variable coinmarketcap with Pymarketcap API/Scraper 

# In[44]:

def coinMarketCapData():
    from pymarketcap import Pymarketcap
    coinmarketcap = Pymarketcap()
    symbols = coinmarketcap.symbols


    # ###### Set initial Date/Time.. Will be setting throughout 

    # In[45]:


    #Pulls date and time information
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    today = pd.Timestamp("today").strftime("%m/%d/%Y")
    hh = pd.Timestamp("today").strftime("%H")
    mm = pd.Timestamp("today").strftime("%M")


    # ###### Coinmarketcap statistics - up to date 1/14/2018

    # In[47]:


    try:
        stats = coinmarketcap.stats()
        stats = pd.DataFrame(stats, index=[0])
        
        stats['Date'] = today
        stats['Hour'] = hh
        stats['Minute'] = mm
        stats['Now'] = pd.Timestamp("today")
        
        stats.to_csv('Coinmarketcap/boom/stats/stats_'+moment+'.csv', sep=',') 
        print("Look at all those stats 0.o")
    except:
        print("*NO STATS GATHERED*")


    # ###### Coin Data - Updated 1/14/2018

    # In[49]:


    try:
        from pymarketcap import Pymarketcap
        coinmarketcap = Pymarketcap()
        ticker = coinmarketcap.ticker(limit=1500, convert="BTC")
        ticker = pd.DataFrame(ticker)

        ticker['Date'] = today
        ticker['Hour'] = hh
        ticker['Minute'] = mm
        ticker['Now'] = pd.Timestamp("today")

        ticker.to_csv('Coinmarketcap/boom/coins/coins_'+moment+'.csv', sep=',')  
        print("Chaaaa-CHING! The coin data is in")
    except:
        print("*NO COINS GATHERED* *YOU ARE LOSING OUT ON BAGS*")


    # ###### Coin exchange info for each token - Updated 1/14/2018

    # In[ ]:


    for coin2 in symbols:
        try:
            from pymarketcap import Pymarketcap
            coinmarketcap = Pymarketcap()
            markets = coinmarketcap.markets(coin2)
            markets = pd.DataFrame(markets['markets'])

            markets['Date'] = today
            markets['Hour'] = hh
            markets['Minute'] = mm
            markets['Now'] = pd.Timestamp("today")
            
            markets.to_csv('Coinmarketcap/boom/markets/markets_'+coin2+'_'+moment+'.csv', sep=',') 
        except:
            print("No market data was captured for ", coin2)
            pass
    print("I hear the exchange trades from here.. exchange data collected :)")


    # ###### Gainers and Losers (1h, 24h, 7d) - Updated 1/14/2018

    # ###### ******Currently no 7d Gainers being captured******

    # ###### New coins - Updated 1/14/2018

    # In[102]:


    #Set date and time
    today = pd.Timestamp("today").strftime("%m/%d/%Y")
    hh = pd.Timestamp("today").strftime("%H")
    mm = pd.Timestamp("today").strftime("%M")
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())

    data = coinmarketcap.recently()
    data = pd.DataFrame(data)

    data.head()

    data['Date'] = today
    data['Hour'] = hh
    data['Minute'] = mm 
    data['days_ago']= data['added'].str.extract('(\d.)', expand=True)
    data['Now'] = pd.Timestamp("today")
    data['days_ago'] = data['days_ago'].apply(pd.to_numeric)
    data['Date_Added'] = data['Now'] - pd.to_timedelta(data['days_ago'], unit='d')
    data['Date_Added'] = data['Date_Added'].dt.date

    #Reimport due to naming issues
    from pymarketcap import Pymarketcap
    coinmarketcap = Pymarketcap()


    #Get Market date for new coins
    for coin2 in data["symbol"]:
        try:
            markets = coinmarketcap.markets(coin2)
            markets = pd.DataFrame(markets['markets'])


            #add 'Today' 'Hour' and 'minutes' column
            markets['Date'] = today
            markets['Hour'] = hh
            markets['Minute'] = mm
            markets['Now'] = pd.Timestamp("today")

            #Save CSV
            markets.to_csv('Coinmarketcap/boom/markets/new/markerts_'+coin2+'_'+moment+'.csv', sep=',') 
            print("Market info for new coin", coin2," captured!")
        except:
            print("************ERROR COIN", coin2, "DATA NOT CAPUTRED*************")
            pass
            
            
        ###Upload datafile

        
    data.to_csv('Coinmarketcap/boom/new/new_'+moment+'.csv', sep=',') 
    print("Gotta catch all the new coins!")


coinMarketCapData()

scheduler = BlockingScheduler()
scheduler.add_job(coinMarketCapData, 'interval', minutes=30, id="cal")
scheduler.start()

