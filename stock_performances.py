import iexfinance
import numpy as np
import pandas as pd
import csv
import datetime
import datastruct

def get_stock_values(key):
    stocks = iexfinance.get_available_symbols(output_format="pandas")
    symbols = []
    for stock in stocks:
        symbol = stock[key]
        symbols.append(symbol)
    return symbols

def get_percent_of_years_performance(stock):
    current = stock.get_price()
    low = stock.get_years_low()
    high = stock.get_years_high()

    percentage = (current - low) / (high - low)
    return percentage

def get_num_stocks():
    return len(get_stock_values("symbol"))

def get_for_all_stocks(func):
    stocks_values = dict()
    applied_list = np.zeros((get_num_stocks()))
    for symbol in get_stock_values("symbol"):
        stock = iexfinance.Stock(symbol)
        try:
            stocks_values[symbol] = func(stock)
        except:
            stocks_values[symbol] = np.NaN
    return stocks_values

def get_performances_csv():
    performances_dict = get_for_all_stocks(get_percent_of_years_performance)
    datastruct.dict_to_csv(
        performances_dict,
        "stock_performances_" + str(datetime.datetime.now()),
        "Stock",
        "(price - low) / (high - low)")

def main():
    get_performances_csv()


if __name__ == "__main__":
    main()
