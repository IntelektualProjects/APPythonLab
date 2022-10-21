import yfinance as yf
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr


class WishList:

    def __init__(self):
        self.wlist = []

    def add_wish_list(self, stock):
        self.wlist.append(stock)
        print(f"The stock {stock} has been added to your wish list")

    def delete_wish_list(self, wish_list):
        self.wlist.remove(wish_list)
        print(f"The stock {wish_list} has been removed from your wish list")

    def see_wish_list(self):
        for items in self.wlist:
            print(items)
        view = input("Would you like to view one of the stocks in your wishlist? y/n")
        if view.upper() == "Y":
            stock_name = input("Which stock would you like to see from this list? (ticker)").upper()
            while True:
                if stock_name not in self.wlist:
                    print("Sorry that is not in your wishlist. Please try again")
                    stock_name = input()
                else:
                    yf.pdr_override()
                    now = dt.datetime.now()
                    start = dt.datetime(2020, 1, 1)
                    df = pdr.get_data_yahoo(stock_name, start, now)
                    print(df)
                    break


# Connect to Google Sheets 
