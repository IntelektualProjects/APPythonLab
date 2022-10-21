import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import pandas as pd


class StockInfo:

    def stock_info(self, usrname):
        pd.set_option('display.max_columns', 6)
        yf.pdr_override()
        stock = input(f" What stock would you like to search today {usrname}? (Ticker)")
        stock_name = yf.Ticker(stock)

        date = input("From what date do you wish to get stock data?  Ex. month/day/year ")
        month, day, year = date.split("/")
        start = dt.datetime(int(year), int(month), int(day))
        now = dt.datetime.now()
        df = pdr.get_data_yahoo(stock, start, now)
        print(df)

        stock_information = dict(stock_name.info)
        if "sector" in stock_information:
            print(f"{stock_information['sector']} sector")
        if "previousClose" in stock_information:
            print(f"Previous Close Price is {stock_information['previousClose']}")
        if "marketCap" in stock_information:
            print(f"Market Cap: {stock_information['marketCap']}")
        if "fiftyTwoWeekHigh" in stock_information:
            print(f"52-week High: {stock_information['fiftyTwoWeekHigh']}")
        if "fiftyTwoWeekLow" in stock_information:
            print(f"52-week Low: {stock_information['fiftyTwoWeekLow']}")

        wish_list = input("Would you like to add this to your wish list? (y/n) ")
        if wish_list.upper() == "Y":
            stock = stock.upper()
            return stock
        return 0
