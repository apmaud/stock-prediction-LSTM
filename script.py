from pandas_datareader import data # access financial data from sources
import matplotlib.pyplot as plt # collection of functions that make change to a figure
import pandas as pd # general analysis functions
import datetime as dt # datetime
import urllib.request, json # opens and reads URLs
import os # allows running of commands in the script
import numpy as np # used for array work
import tensorflow as tf # machine learning
from sklearn.preprocessing import MinMaxScaler # machine learning, data analysis library

data_source = 'kaggle'

if data_source == 'alphavantage':
    api_key = '57RJJOC80BF61120'
    ticker = "AAL"
    url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)
    file_to_save = 'stock_market_data-%s.csv'%ticker
    




