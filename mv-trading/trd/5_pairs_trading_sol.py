from datetime import datetime

def calculate_price_change(price1, price2):
    return (price2 - price1) / price1 * 10000

def find_corresponding_b_data(timestamp, stock_b_data):
    for data in stock_b_data:
        if data[0] == timestamp:
            return data
    return None

def pairs_trading(market_data, x):
    stock_a_data, stock_b_data = market_data
    pnl = 0
    position = 0

    for i in range(1, len(stock_a_data)):
        timestamp_a1 = datetime.strptime(stock_a_data[i-1][0], '%d/%m/%Y %H:%M:%S')
        timestamp_a2 = datetime.strptime(stock_a_data[i][0], '%d/%m/%Y %H:%M:%S')
        ask_price_a1 = float(stock_a_data[i-1][2].replace(',', '.'))
        ask_price_a2 = float(stock_a_data[i][2].replace(',', '.'))

        price_change = calculate_price_change(ask_price_a1, ask_price_a2)
        corresponding_b_data = find_corresponding_b_data(timestamp_a2, stock_b_data)

        if corresponding_b_data is None:
            continue

        bid_price_b = float(corresponding_b_data[1].replace(',', '.'))
        ask_price_b = float(corresponding_b_data[2].replace(',', '.'))

        if price_change >= x:
            position += 1
            pnl -= ask_price_b
        elif price_change <= -x:
            position -= 1
            pnl += bid_price_b

    # Close remaining positions
    last_bid_price_b = float(stock_b_data[-1][1].replace(',', '.'))
    last_ask_price_b = float(stock_b_data[-1][2].replace(',', '.'))
    if position > 0:
        pnl += position * last_bid_price_b
    elif position < 0:
        pnl -= position * last_ask_price_b

    return pnl

# Test the function
stock_a_data = [
    ['13/09/2021 21:31:00', '3278,403', '3278,403'],
    ['13/09/2021 21:30:00', '3278,289', '3278,289'],
    ['13/09/2021 21:29:00', '3278,286', '3278,286'],
    ['13/09/2021 21:29:00', '3278,453', '3278,453'],
    ['13/09/2021 21:28:00', '3278,748', '3278,748'],
    ['13/09/2021 21:28:00', '3278,52', '3278,52']
]

stock_b_data = [
    ['13/09/2021 21:31:49', '45070,36', '45070,36'],
    ['13/09/2021 21:31:39', '45078,15', '45078,15'],
    ['13/09/2021 21:31:29', '45073,38', '45073,38'],
    ['13/09/2021 21:31:19', '45075,28', '45075,28'],
    ['13/09/2021 21:31:09', '45072,39', '45075,28']
]

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

import pandas as pd

def calculate_price_change(price1, price2):
    return (price2 - price1) / price1 * 10000

def find_corresponding_b_data(timestamp, stock_b_data):
    matching_rows = stock_b_data[stock_b_data['timestamp_gmt'] == timestamp]
    return matching_rows.iloc[0] if not matching_rows.empty else None

def pairs_trading(market_data, x):
    stock_a_data, stock_b_data = market_data
    pnl = 0
    position = 0

    for i in range(1, len(stock_a_data)):
        price_change = calculate_price_change(stock_a_data.loc[i-1, 'ask'], stock_a_data.loc[i, 'ask'])
        corresponding_b_data = find_corresponding_b_data(stock_a_data.loc[i, 'timestamp_gmt'], stock_b_data)

        if corresponding_b_data is None:
            continue

        if price_change >= x:
            position += 1
            pnl -= corresponding_b_data['ask']
        elif price_change <= -x:
            position -= 1
            pnl += corresponding_b_data['bid']

    # Close remaining positions
    if position > 0:
        pnl += position * stock_b_data.iloc[-1]['bid']
    elif position < 0:
        pnl -= position * stock_b_data.iloc[-1]['ask']

    return pnl

# Test the function
stock_a_data = pd.DataFrame({
    'timestamp_gmt': pd.to_datetime(['13/09/2021 21:31:00', '13/09/2021 21:30:00', '13/09/2021 21:29:00', '13/09/2021 21:29:00', '13/09/2021 21:28:00', '13/09/2021 21:28:00']),
    'bid': [3278.403, 3278.289, 3278.286, 3278.453, 3278.748, 3278.52],
    'ask': [3278.403, 3278.289, 3278.286, 3278.453, 3278.748, 3278.52]
})

stock_b_data = pd.DataFrame({
    'timestamp_gmt': pd.to_datetime(['13/09/2021 21:31:49', '13/09/2021 21:31:39', '13/09/2021 21:31:29', '13/09/2021 21:31:19', '13/09/2021 21:31:09', '13/09/2021 21:30:59', '13/09/2021 21:30:49', '13/09/2021 21:30:39']),
    'bid': [45070.36, 45078.15, 45073.38, 45075.28, 45072.73, 45069.95, 45071.04, 45070.64],
    'ask': [45070.36, 45078.15, 45073]
    })

# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------



from datetime import datetime

def calculate_price_change(price1, price2):
    return (price2 - price1) / price1 * 10000

def find_corresponding_b_data(timestamp, stock_b_data):
    for data in stock_b_data:
        if data[0] == timestamp:
            return data
    return None

def pairs_trading(market_data, x):
    stock_a_data, stock_b_data = market_data[1], market_data[3]
    pnl = 0
    position = 0

    stock_a_data = [stock_a_data[i:i+3] for i in range(0, len(stock_a_data), 3)]
    stock_b_data = [stock_b_data[i:i+3] for i in range(0, len(stock_b_data), 3)]

    for i in range(1, len(stock_a_data)):
        timestamp_a1 = datetime.strptime(stock_a_data[i-1][0], '%d/%m/%Y %H:%M:%S')
        timestamp_a2 = datetime.strptime(stock_a_data[i][0], '%d/%m/%Y %H:%M:%S')
        ask_price_a1 = float(stock_a_data[i-1][2].replace(',', '.'))
        ask_price_a2 = float(stock_a_data[i][2].replace(',', '.'))

        print(timestamp_a1)
        print(timestamp_a2)

        price_change = calculate_price_change(ask_price_a1, ask_price_a2)
        corresponding_b_data = find_corresponding_b_data(timestamp_a2, stock_b_data)

        if corresponding_b_data is None:
            continue

        bid_price_b = float(corresponding_b_data[1].replace(',', '.'))
        ask_price_b = float(corresponding_b_data[2].replace(',', '.'))

        if price_change >= x:
            position += 1
            pnl -= ask_price_b
        elif price_change <= -x:
            position -= 1
            pnl += bid_price_b

    # Close remaining positions
    last_bid_price_b = float(stock_b_data[-1][1].replace(',', '.'))
    last_ask_price_b = float(stock_b_data[-1][2].replace(',', '.'))
    if position > 0:
        pnl += position * last_bid_price_b
    elif position < 0:
        pnl -= position * last_ask_price_b

    return pnl


if __name__ == '__main__':
    # Test the function
    market_data = [
        'Stock A',
        [
            '13/09/2021 21:31:00', '3278,403', '3278,403',
            '13/09/2021 21:31:00', '3278,289', '3278,289',
            '13/09/2021 21:31:00', '3278,286', '3278,286',
            '13/09/2021 21:29:00', '3278,286', '3270,286'
        ],
        'Stock B',
        [
            '13/09/2021 21:31:49', '45070,36', '45070,36',
            '13/09/2021 21:31:39', '45078,15', '45078,15',
            '13/09/2021 21:31:29', '45073,38', '45073,38'
        ]
    ]

    x = 10
    result = pairs_trading(market_data, x)
    print(result)



# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------
# market_data = [{
#     'Stock A': [
#         {'timestamp': '13/09/2021 21:31:00', 'bid': '3278,403', 'ask': '3278,403'},
#         {'timestamp': '13/09/2021 21:31:00', 'bid': '3278,289', 'ask': '3278,289'},
#         {'timestamp': '13/09/2021 21:31:00', 'bid': '3278,286', 'ask': '3278,286'},
#         {'timestamp': '13/09/2021 21:29:00', 'bid': '3278,286', 'ask': '3270,286'}
#     ],
#     'Stock B': [
#         {'timestamp': '13/09/2021 21:31:49', 'bid': '45070,36', 'ask': '45070,36'},
#         {'timestamp': '13/09/2021 21:31:39', 'bid': '45078,15', 'ask': '45078,15'},
#         {'timestamp': '13/09/2021 21:31:29', 'bid': '45073,38', 'ask': '45073,38'}
#     ]
# }]



from datetime import datetime

def calculate_price_change(old_price, new_price):
    return 10000 * (new_price - old_price) / old_price

def find_corresponding_b_data(timestamp_a, stock_b_data):
    for data in stock_b_data:
        if data['timestamp'] == timestamp_a:
            return data
    return None

def pairs_trading(market_data, x):
    stock_a_data = market_data[0]['Stock A']
    stock_b_data = market_data[0]['Stock B']
    pnl = 0
    position = 0

    stock_a_data.sort(key=lambda row: datetime.strptime(row['timestamp'], '%d/%m/%Y %H:%M:%S'))
    stock_b_data.sort(key=lambda row: datetime.strptime(row['timestamp'], '%d/%m/%Y %H:%M:%S'))

    for i in range(1, len(stock_a_data)):
        timestamp_a1 = datetime.strptime(stock_a_data[i-1]['timestamp'], '%d/%m/%Y %H:%M:%S')
        timestamp_a2 = datetime.strptime(stock_a_data[i]['timestamp'], '%d/%m/%Y %H:%M:%S')
        ask_price_a1 = float(stock_a_data[i-1]['ask'].replace(',', '.'))
        ask_price_a2 = float(stock_a_data[i]['ask'].replace(',', '.'))

        price_change = calculate_price_change(ask_price_a1, ask_price_a2)
        corresponding_b_data = find_corresponding_b_data(stock_a_data[i]['timestamp'], stock_b_data)

        if corresponding_b_data is None:
            continue

        bid_price_b = float(corresponding_b_data['bid'].replace(',', '.'))
        ask_price_b = float(corresponding_b_data['ask'].replace(',', '.'))

        if price_change >= x:
            position += 1
            pnl -= ask_price_b
        elif price_change <= -x:
            position -= 1
            pnl += bid_price_b

    # Close remaining positions
    last_bid_price_b = float(stock_b_data[-1]['bid'].replace(',', '.'))
    last_ask_price_b = float(stock_b_data[-1]['ask'].replace(',', '.'))
    if position > 0:
        pnl += position * last_bid_price_b
    elif position < 0:
        pnl -= position * last_ask_price_b

    return pnl

# Test the function
x = 10  # Change this value to test with different bps
result = pairs_trading(market_data, x)
print(result)




# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# market_data = [
#     ['Stock Name', 'Timestamp', 'Bid', 'Ask'],
#     ['Stock A', '13/09/2021 21:31:00', '3278,403', '3278,403'],
#     ['Stock A', '13/09/2021 21:31:00', '3278,289', '3278,289'],
#     ['Stock A', '13/09/2021 21:31:00', '3278,286', '3278,286'],
#     ['Stock A', '13/09/2021 21:29:00', '3278,286', '3270,286'],
#     ['Stock B', '13/09/2021 21:31:49', '45070,36', '45070,36'],
#     ['Stock B', '13/09/2021 21:31:39', '45078,15', '45078,15'],
#     ['Stock B', '13/09/2021 21:31:29', '45073,38', '45073,38']
# ]



from datetime import datetime

def calculate_price_change(old_price, new_price):
    return 10000 * (new_price - old_price) / old_price

def find_corresponding_b_data(timestamp_a, stock_b_data):
    for data in stock_b_data:
        if data['Timestamp'] == timestamp_a:
            return data
    return None

def pairs_trading(market_data, x):
    stock_a_data = [row for row in market_data if row[0] == 'Stock A'][1:]
    stock_b_data = [row for row in market_data if row[0] == 'Stock B'][1:]
    pnl = 0
    position = 0

    stock_a_data.sort(key=lambda row: datetime.strptime(row[1], '%d/%m/%Y %H:%M:%S'))
    stock_b_data.sort(key=lambda row: datetime.strptime(row[1], '%d/%m/%Y %H:%M:%S'))

    for i in range(1, len(stock_a_data)):
        timestamp_a1 = datetime.strptime(stock_a_data[i-1][1], '%d/%m/%Y %H:%M:%S')
        timestamp_a2 = datetime.strptime(stock_a_data[i][1], '%d/%m/%Y %H:%M:%S')
        ask_price_a1 = float(stock_a_data[i-1][3].replace(',', '.'))
        ask_price_a2 = float(stock_a_data[i][3].replace(',', '.'))

        price_change = calculate_price_change(ask_price_a1, ask_price_a2)
        corresponding_b_data = find_corresponding_b_data(stock_a_data[i][1], stock_b_data)

        if corresponding_b_data is None:
            continue

        bid_price_b = float(corresponding_b_data[2].replace(',', '.'))
        ask_price_b = float(corresponding_b_data[3].replace(',', '.'))

        if price_change >= x:
            position += 1
            pnl -= ask_price_b
        elif price_change <= -x:
            position -= 1
            pnl += bid_price_b

    # Close remaining positions
    last_bid_price_b = float(stock_b_data[-1][2].replace(',', '.'))
    last_ask_price_b = float(stock_b_data[-1][3].replace(',', '.'))
    if position > 0:
        pnl += position * last_bid_price_b
    elif position < 0:
        pnl -= position * last_ask_price_b

    return pnl

# Test the function
x = 10  # Change this value to test with different bps
result = pairs_trading(market_data, x)
print(result)


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# market_data = [
#     ('Stock A', [
#         ('13/09/2021 21:31:00', '3278,403', '3278,403'),
#         ('13/09/2021 21:31:00', '3278,289', '3278,289'),
#         ('13/09/2021 21:31:00', '3278,286', '3278,286'),
#         ('13/09/2021 21:29:00', '3278,286', '3270,286')
#     ]),
#     ('Stock B', [
#         ('13/09/2021 21:31:49', '45070,36', '45070,36'),
#         ('13/09/2021 21:31:39', '45078,15', '45078,15'),
#         ('13/09/2021 21:31:29', '45073,38', '45073,38')


from datetime import datetime

def calculate_price_change(old_price, new_price):
    return 10000 * (new_price - old_price) / old_price

def find_corresponding_b_data(timestamp_a, stock_b_data):
    for data in stock_b_data:
        if data[0] == timestamp_a:
            return data
    return None

def pairs_trading(market_data, x):
    stock_a_data = market_data[0][1]
    stock_b_data = market_data[1][1]
    pnl = 0
    position = 0

    stock_a_data.sort(key=lambda row: datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S'))
    stock_b_data.sort(key=lambda row: datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S'))

    for i in range(1, len(stock_a_data)):
        timestamp_a1 = datetime.strptime(stock_a_data[i-1][0], '%d/%m/%Y %H:%M:%S')
        timestamp_a2 = datetime.strptime(stock_a_data[i][0], '%d/%m/%Y %H:%M:%S')
        ask_price_a1 = float(stock_a_data[i-1][2].replace(',', '.'))
        ask_price_a2 = float(stock_a_data[i][2].replace(',', '.'))

        price_change = calculate_price_change(ask_price_a1, ask_price_a2)
        corresponding_b_data = find_corresponding_b_data(stock_a_data[i][0], stock_b_data)

        if corresponding_b_data is None:
            continue

        bid_price_b = float(corresponding_b_data[1].replace(',', '.'))
        ask_price_b = float(corresponding_b_data[2].replace(',', '.'))

        if price_change >= x:
            position += 1
            pnl -= ask_price_b
        elif price_change <= -x:
            position -= 1
            pnl += bid_price_b

    # Close remaining positions
    last_bid_price_b = float(stock_b_data[-1][1].replace(',', '.'))
    last_ask_price_b = float(stock_b_data[-1][2].replace(',', '.'))
    if position > 0:
        pnl += position * last_bid_price_b
    elif position < 0:
        pnl -= position * last_ask_price_b

    return pnl

# Test the function
x = 10  # Change this value to test with different bps
result = pairs_trading(market_data, x)
print(result)
