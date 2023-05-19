import sys
import pandas as pd
import numpy as np
from io import StringIO

# Read input from STDIN
input_data = sys.stdin.read()

# Split input into trades and bid_ask
trades_csv, bid_ask_csv = input_data.strip().split('\n\n')

# Read input into dataframes
trades = pd.read_csv(StringIO(trades_csv))
bid_ask = pd.read_csv(StringIO(bid_ask_csv))

# Convert timestamp_gmt to datetime
trades['timestamp_gmt'] = pd.to_datetime(trades['timestamp_gmt'])
bid_ask['timestamp_gmt'] = pd.to_datetime(bid_ask['timestamp_gmt'])

# Define the function to calculate delta quality
def delta_quality(trades, bid_ask, x):
    dq_numerator = 0
    dq_denominator = 0

    for index, trade in trades.iterrows():
        trade_time = trade['timestamp_gmt']
        trade_volume = trade['volume']
        trade_price = trade['price']
        trade_side = 1 if trade['side'] == 'BOT' else -1

        future_time = trade_time + pd.Timedelta(seconds=x)
        future_bid_ask = bid_ask.loc[bid_ask['timestamp_gmt'] == future_time].iloc[0]

        volume_bid = future_bid_ask['bid_size']
        volume_ask = future_bid_ask['ask_size']
        price_bid = future_bid_ask['bid']
        price_ask = future_bid_ask['ask']

        future_price = (volume_bid * price_ask + volume_ask * price_bid) / (volume_bid + volume_ask)

        dq_numerator += ((future_price - trade_price) / trade_price) * trade_side * trade_volume
        dq_denominator += trade_volume

    dq = dq_numerator / dq_denominator
    return dq * 10000  # Convert to basis points

# Calculate delta quality for 10 seconds and 60 seconds
dq_10 = delta_quality(trades, bid_ask, 10)
dq_60 = delta_quality(trades, bid_ask, 60)

# Print output to STDOUT
print(f'Delta quality (DQ) for 10 seconds: {dq_10} bps')
print(f'Delta quality (DQ) for 60 seconds: {dq_60} bps')