# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:11:35 2020

@author: Aetienne
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime 

"""
df = pd.read_csv('tether prices.csv', sep=';', parse_dates=["Date"], decimal=",")
df.set_index('Date', inplace=True)

fig=plt.figure()
plt.title('Historical Tether Prices and Market Cap.')

ax1 = df['Close'].plot(color='blue', grid=True)
ax2 = (df['Market Cap']/10**6).plot(color='red', secondary_y=True, grid=True)

handles,labels = [],[]
for ax in fig.axes:
    for h,l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)

plt.legend(handles,labels)

ax2.set_ylim([0,350])
ax2.set_ylabel('Market Cap. (in million USD)')

ax1.set_ylim([0.9,1.1])
ax1.set_xlabel("Date")
ax1.set_ylabel("Price (USD)")
ax1.set_xlim([datetime.date(2017, 4, 1), datetime.date(2017, 8, 31)])

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %y'))
plt.savefig('tether prices.png', bbox_inches='tight')
"""



df = pd.read_csv('google trends.csv', sep=';', parse_dates=["Date"])
df = df[(df['Date'] > '2008-1-1')]
ax = df.plot(x='Date', y=['Mastercoin', 'Stablecoin'], lw=1.0, linestyle="-", title='Mastercoin vs. Stablecoin Google Searches')
ax.set_xlim([datetime.date(2008, 1, 1), datetime.date(2019, 11, 30)])
ax.set_xlabel("Date")
ax.set_ylabel("Google Search Activity")
plt.grid(True)
plt.savefig('google search activity.png', bbox_inches='tight')