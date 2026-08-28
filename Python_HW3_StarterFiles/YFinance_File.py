import numpy as np
import pandas as pd

def YahooData2returns(YahooData=None,symbol='AAPL'):
    # Input:
    # YahooData = data from Yahoo Finance
    # Output:
    # returns = array of returns
    # Steps:
    # Extract 'Close' and symbol (This is a 2d column. Demo below.)
    # Calculate and return the lagged returns
    prices = YahooData['Close'][symbol]
returns = prices.pct_change().dropna().values
    return returns
