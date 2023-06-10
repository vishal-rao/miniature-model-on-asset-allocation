#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
from datetime import datetime, timedelta, date



# ### Downloading historical prices for 10 companies across 4 sectors

# In[10]:


# Function to download data and calculate the average of quarters
def histData(tickr,startyear,endyear):
    j = []
    k = []
    opend=[]
    highd=[]
    lowd=[]
    closed=[]
    acd=[]
    for i in range(4,14,3):
        if i == 13:
            j.append(i//10)
            k.append(i%10)
        else:
                j.append(i)
                k.append(i+2)
    years = list(np.arange(startyear,endyear))
    for z in years:
        for (sm,em) in zip(j,k):
            start = datetime.datetime(z,sm,1)
            end = datetime.datetime(z, em, 30)
            data = pdr.get_data_yahoo(tickr, start,end)
            o=data['Open'].mean()
            opend.append(o)
            h=data['High'].mean()
            highd.append(h)
            l=data['Low'].mean()
            lowd.append(l)
            c=data['Close'].mean()
            closed.append(c)
            ac=data['Adj Close'].mean()
            acd.append(ac)
    df_mod = pd.concat([pd.DataFrame(opend),pd.DataFrame(highd),pd.DataFrame(lowd),pd.DataFrame(closed),pd.DataFrame(acd)],axis=1)
    df_mod.columns=['Open','High','Low','Close','AdjClose']
    df_new2 = df_mod.copy()
    for i,j in zip(range(0,len(df_mod),4),range(0,len(df_mod)+1)):
         df_new2['Open'] = df_new2['Open'].replace(df_new2['Open'][j],df_mod.Open[i:i+4].mean())
         df_new2['High'] = df_new2['High'].replace(df_new2['High'][j],df_mod.High[i:i+4].mean())
         df_new2['Low'] = df_new2['Low'].replace(df_new2['Low'][j],df_mod.Low[i:i+4].mean())
         df_new2['Close'] = df_new2['Close'].replace(df_new2['Close'][j],df_mod.Close[i:i+4].mean())
         df_new2['AdjClose'] = df_new2['AdjClose'].replace(df_new2['AdjClose'][j],df_mod.AdjClose[i:i+4].mean())
#          year_range = list(range(startyear,endyear))
#          df_new2.insert(0, 'Year', year_range)
    return df_new2.drop(df_new2.index[int(len(df_new2)/4):int(len(df_new2))])


# In[7]:


# # # Downloading the data for IT sector
# histData('infy.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\infy.csv', index = False)
# # histData('wipro.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\wipro.csv', index = False)
# # histData('tcs.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\tcs.csv', index = False)
# # histData('hcltech.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\hcltech.csv', index = False)
# # histData('mphasis.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\mphasis.csv', index = False)
# # histData('lt.ns',2004,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\lt.csv', index = False)
# # histData('coforge.ns',2005,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\coforge.csv', index = False)
# # histData('techm.ns',2007,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\techm.csv', index = False)
# # histData('mindtree.ns',2007,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\mindtree.csv', index = False)
# # histData('ltts.ns',2017,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\IT Sector\ltts.csv', index = False)


# In[37]:


# # Downloading the data for banking sector
# histData('sbin.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\sbi.csv', index = False)
# histData('indianb.ns',2007,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\indianb.csv', index = False)
# histData('bankbaroda.ns',2006,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\bob.csv', index = False)
# histData('hdfcbank.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\hdfc.csv', index = False)
# histData('icicibank.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\icici.csv', index = False)
# histData('kotakbank.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\kotak.csv', index = False)
# histData('idfcfirstb.ns',2016,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\idfcfirst.csv', index = False)
# histData('canbk.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Banking Sector\canbk.csv', index = False)


# In[22]:


# # # Downloading the data for pharma sector
# # histData('sunpharma.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\sunpharma.csv', index = False)
# # histData('drreddy.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\drreddy.csv', index = False)
# # histData('cipla.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\cipla.csv', index = False)
# # histData('torntpharm.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\torrent.csv', index = False)
# # histData('zyduslife.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\zyduslife.csv', index = False)
# # histData('divislab.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\divis.csv', index = False)
# # histData('biocon.ns',2005,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\Pharma\biocon.csv', index = False)


# In[8]:


# # Downloading the data for fmcg sector
# histData('hindunilvr.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\FMCG\uni.csv', index = False)
# histData('itc.ns',2002,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\FMCG\itc.csv', index = False)
# histData('marico.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\FMCG\marico.csv', index = False)
# histData('britannia.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\FMCG\britannia.csv', index = False)
# histData('dabur.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\FMCG\dabur.csv', index = False)
# histData('godrejcp.ns',2003,2022).to_csv(r'C:\Users\triti\OneDrive\Documents\SET PROJECT 2022-23\FMCG\godrej.csv', index = False)


# ## Obtaining weights for investment amount per company

# In[91]:


# it = [infy, wipro, tcs, mphasis, coforge, hcltech, lt, ltts, techm, mindtree]
# pharma = [sunpharma, drreddy, cipla, torrent, zyduslife, divislab, biocon]
# fmcg = [unilvr,itc,marico,britannia,dabur,godrej]
# banking = [sbi,indian,bob, hdfc, icici, kotak, idfc, canb]

ticker_symbols={
    'Infosys':'infy.ns',
    'Wipro':'wipro.ns',
    'TCS':'tcs.ns',
    'Mphasis':'mphasis.ns',
    'Coforge':'coforge.ns',
    'HCL Tech': 'hcltech,ns',
    'Larsen & Toubro':'lt.ns',
    'L&T Technology Services': 'ltts.ns',
    'Tech Mahindra':'techm.ns',
    'Mindtree':'mindtree.ns',
    'Sunpharma':'sunpharma.ns',
    'Drreddy':'drreddy.ns',
    'Cipla':'cipla.ns',
    'Torrent':'torntpharm.ns',
    'Zyduslife':'zyduslife.ns',
    'Divis Lab':'divislab.ns',
    'Biocon':'biocon.ns',
    'Hindustan Unilever':'hindunilvr.ns',
    'ITC':'itc.ns',
    'Marico':'marico.ns',
    'Britannia':'britannia.ns',
    'Dabur':'dabur.ns',
    'Godrej':'godrejcp.ns',
    'SBI':'sbin.ns',
    'Indian Bank':'indianb.ns',
    'Bank of Baroda':'bankbaroda.ns',
    'HDFC':'hdfcbank.ns',
    'ICICI':'icicibank.ns',
    'Kotak Mahindra':'kotakbank.ns',
    'IDFC':'idfcfirstb.ns',
    'Canara Bank':'canbk.ns'  
}

# ticks = [ticker_symbols['Infosys','Mindtree']]
#noc = ['Canara Bank','ITC','Torrent','Wipro','Mindtree','TCS']
noc =['Cipla','Mindtree','ICICI','Bank of Baroda','Infosys']
ticks = [ticker_symbols.get(key) for key in noc]
ticks

def getweeklydata():
    cp = []
    curr = datetime.date(2021,2,8)
#     curr = datetime.datetime.today().date()


    prev = (curr - datetime.timedelta(weeks = len(noc)-1))
    for t in ticks:
        stock_d = yf.download(t,prev,curr,interval = "1wk")
        cp.append(stock_d['Close'])
    weekly_data = pd.DataFrame(cp)
#     weekly_data.columns = ['Week 1', 'Week 2']
    
    return weekly_data
getweeklydata().to_csv(r'D:\ML Datasets\weekly_data.csv', index = False)


# In[72]:


dataWeekly = pd.read_csv(r'D:\ML Datasets\weekly_data.csv')
dataWeekly.drop('2022-10-27',axis=1,inplace = True)
dataWeekly


# ## Hungarian on Weekly Closing Prices

# In[42]:


# Assignments using Hungarian Method
from scipy.optimize import linear_sum_assignment

cprices = dataWeekly.to_numpy()

row_ind, col_ind = linear_sum_assignment(cprices,True)

print("Closing prices from last ", len(ticks)," weeks: \n", cprices)
# print("\nCost Matrix: \n", cprices)
print("\nAssignments from Hungarian Method: \n", cprices[row_ind, col_ind], "\n")
for i in range(len(row_ind)):
    print("row_index: ", row_ind[i], "  col_index: " ,col_ind[i], "  value: ", cprices[i, col_ind[i]] )
total_assignment = cprices[row_ind, col_ind].sum()
print("\n Total cost on account of assignments made: ", total_assignment )


# In[47]:


cprices[row_ind, col_ind]
principal_amount = 10000
dfcp = pd.DataFrame(cprices[row_ind, col_ind], columns = ['Assignments'], index = ticks)
dfcp['Weights'] = (dfcp['Assignments']/total_assignment)*100
dfcp
index = [noc[i] for i in list(row_ind)]
# Obtaining current stock prices
csp = []
index = [noc[i] for i in list(row_ind)]
port_ticks = [ticker_symbols.get(key) for key in index]
for t in port_ticks:
    stock = yf.Ticker(t)
    price = stock.info['regularMarketPrice']
    csp.append(price)


# #### Checking standard deviation for evaluation of volatility

# In[52]:


# fetch the daily returns for a stock
principal_amount = int(input("Enter the principal amount: "))
# principal_amount = 100000
portfolio = pd.DataFrame(cprices[row_ind, col_ind], columns = ['Assignments'], index = index)
portfolio['Weights'] = (portfolio['Assignments']/cprices[row_ind, col_ind].sum())*100
portfolio['Current Stock Price'] = csp
# Getting units allocation for each stock
a = portfolio['Assignments'].sum()
norm_value = (principal_amount*portfolio['Assignments'])/a
units = norm_value/portfolio['Current Stock Price']
portfolio['Units'] = units
portfolio

