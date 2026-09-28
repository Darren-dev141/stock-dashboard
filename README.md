# Stock Dashboard

Downloads historical stock data from Yahoo Finance and visualizes it with a small Streamlit dashboard.

## How it works

- `main.py` prompts for a ticker and date range, pulls daily OHLC data from Yahoo Finance's download endpoint into `data.csv`, then renders it in Streamlit with a line chart.

## Run

```bash
pip install -r requirements.txt
streamlit run main.py
```

## Stack

Python, Streamlit, pandas, requests
