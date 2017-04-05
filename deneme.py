from stocktalk import streaming
from stocktalk import visualize
from bokeh.plotting import hplot, figure, show, output_server, Session
from numpy import arange, sin, cos


API_KEY = 'Xm5UMC76zmgBAqh32WECmvT4n'
API_SECRET = 'LJJFp2yIUhaoUp2CpviwhTWxGHLXhcUoOgjCjuBJCYbIlYq8uJ'
ACCESS_TOKEN = '2866268703-MZYoOB5dNXG20PbThX2aIlydEZBW8WDX5ui3t5q'
ACCESS_TOKEN_SECRET = 'R2oSZ5BPHuUi8qLE8gN6BuaWTeKOvODWJfQRUq1P037xl'
credentials = [API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]

path = "/home/diablo/Documents/Stocktalk/data/"
# python -m bokeh serve --show visualize.py
# First element must be ticker/name, proceeding elements are extra queries
TSLA = ['TSLA', 'Tesla']
SNAP = ['SNAP', 'Snapchat']
AAPL = ['AAPL', 'Apple']
AMZN = ['AMZN', 'Amazon']

# Variables
tickers = [TSLA, SNAP, AAPL, AMZN]  # Used for identification purposes
queries = TSLA + SNAP + AAPL + AMZN  # Filters tweets containing one or more query
refresh = 30  # Process and log data every 30 seconds

streaming(credentials, tickers, queries, refresh, path, \
          realtime=True, logTracker=True, logTweets=True, logSentiment=True, debug=True)

visualize(tickers, refresh, path)





