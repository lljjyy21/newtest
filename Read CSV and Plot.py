# READ CSV FILE AND PLOT
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick2_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# enter stock code !!!!!!
stockName = 'TSLA'

# choose which data you want to see in the plot !!!!!!
dataTypes = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

# choose from 1 to 5 !!!!!!
numFroTypes = 4
theType = dataTypes[numFroTypes]

# read csv file
df = pd.read_csv(stockName + '.csv', parse_dates=True, index_col=0)

# show specifc data plot
df[theType].plot()

# df_ohlc = df['Close'].resample('10D').ohlc()
# df_volume = df['Volume'].resample('10D').sum()
# df_ohlc.reset_index(inplace=True)
# df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
# ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1)
# ax1.xaxis_date()



plt.show()
