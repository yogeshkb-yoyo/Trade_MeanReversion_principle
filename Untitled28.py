import yfinance as yf
symbol = 'AAPL'  
quantity = 100  
profit_target = 0.50 
stop_loss = 0.25  
mean_threshold = 0.10  

# Fetch market data
stock_data = yf.download(symbol, period='1d', interval='1m')
bars = stock_data.iloc[-2:] 
price_diff = bars['Close'].diff().iloc[-1]

if price_diff > 0:
    entry_price = bars['Close'].iloc[-1]  
    exit_price = entry_price + profit_target  
    stop_price = entry_price - stop_loss  
    mean_price = bars['Close'].mean() 

    if entry_price > (1 + mean_threshold) * mean_price:
        print(f"Placing a buy order for {quantity} shares of {symbol} at a limit price of ₹{entry_price:.2f}")

        while True:
            latest_price = stock_data['Close'].iloc[-1]
            if latest_price <= mean_price or latest_price >= exit_price or latest_price <= stop_price:
                print(f"Placing a sell order for {quantity} shares of {symbol} at a limit price of ₹{latest_price:.2f}")
                break
            else:
                print(f"Latest price: ₹{latest_price:.2f}")
    else:
        print(f"Mean reversion trade not triggered for {symbol}.")
else:
    print(f"No trade opportunity detected for {symbol}.")


print(f"Price difference: ₹{price_diff:.2f} (Difference between the last two 1-minute bars' closing prices)")
print(f"Entry price: ₹{entry_price:.2f} (Price when the current bar opened)")
print(f"Mean price: ₹{mean_price:.2f} (Mean of the last two 1-minute bars' closing prices)")
print(f"Stop price: ₹{stop_price:.2f} (Price below which the trade will be stopped)")
print(f"Exit price: ₹{exit_price:.2f} (Profit target price)")