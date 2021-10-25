# import time
# import datetime

# with open("companies.txt") as file:
#     lines = file.readlines()
#     companyList = [line.rstrip() for line in lines][0]
# print(companyList)
# interval = '1d'
# period1 = int(time.mktime(datetime.datetime(2021, 1, 1, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2021, 6, 30, 23, 59).timetuple()))

# xlwriter = pd.ExcelWriter('historical prices.xlsx', engine='openpyxl')
# for ticker in companyList:
#     query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
#     df = pd.read_csv(query_string)
#     df.to_excel(xlwriter, sheet_name=ticker, index=False)

# xlwriter.save()

import yahoo_fin.stock_info as si
import pandas as pd
from io import BytesIO

with open("companies.txt") as file:
    lines = file.readlines()
    companyList = [line.rstrip() for line in lines]

stockData = {}

# writer = pd.ExcelWriter('/path_to_save/output.xlsx')
sum_df=pd.DataFrame()

for ticker in companyList:
    try:

        stockData[ticker] = si.get_data(ticker, start_date="01/01/2010", end_date="01/03/2020", interval="1mo")
        sum_df = sum_df.append(stockData[ticker])
    except:
        continue

sum_df.to_excel("output.xlsx") 






