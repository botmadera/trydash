import pandas_datareader.data as web

symbol = 'WIKI/AAPL'  # or 'AAPL.US'

df = web.DataReader(symbol, 'quandl', '2015-01-01', '2015-01-05')

df.loc['2015-01-02']

print(df.head())