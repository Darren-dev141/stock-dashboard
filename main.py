import streamlit as st
from fpdf import FPDF
import pandas

import requests
from datetime import datetime
import time

def stocklookup():
    ticker = input("Input stock ticker")
    from_date = input('Enter Start date in YYYY/MM/DD Format:')
    to_date = input('Enter End date in YYYY/MM/DD    Format:')

    from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
    to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

    from_epoch = int(time.mktime(from_datetime.timetuple()))
    to_epoch = int(time.mktime(to_datetime.timetuple()))

    url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
    headers = headers = {'user-agent': 'my-app/0.0.1'}
    content = requests.get(url, headers=headers).content
    print(content)
    with open('data.csv', 'wb') as file:
        file.write(content)
        return file
    return
data = pandas.read_csv("data.csv")
df = pandas.DataFrame(data)
st.write("test")
st.write(data)
st.line_chart(data['Date'])
