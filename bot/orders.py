from bot.client import client
import datetime
import json 
import logging

def place_order(side,order_type,symbol,quantity,price=None) :
    print("\n---Order Summary---")
    print(f"Side       : {side}")
    print(f"Order type : {order_type}")
    print(f"Symbol     : {symbol}")
    print(f"Quantity   : {quantity}")
    if order_type == "LIMIT" :
        print(f"Price      : {price}")
    print("Fetching current market price...")
    try :
        price_data = client.get_symbol_ticker(symbol=symbol)
        current_price = float(price_data["price"])
    except :
        print("Invalid symbol or API")
        return 
    print(f"Current Price : {current_price}")
    #order logic
    status = ""
    message = ""
    if order_type == "MARKET" :
        status = "EXECUTED"
        message = f"Order executed at {current_price}"
    else :
        if side == "BUY" :
            if price >= current_price :
                status = "EXECUTED"
                message = f"Order executed at {current_price}"
            else :
                status = "PENDING"
                message = f"Order pending at {current_price}"
        elif side == "SELL" :
            if price <= current_price :
                status = "EXECUTED"
                message = f"Order executed at {current_price}"
            else :
                status = "PENDING"
                message = f"Order pending at {current_price}"
    print(f"Status : {status}")
    print(message)

    # Logging
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "time" : timestamp,
        "symbol" : symbol,
        "side" : side,
        "order_type" : order_type,
        "quantity" : quantity,
        "price" : price if price else "MARKET",
        "market_price" : current_price,
        "status" : status
    }
    with open("orders.log", "a") as file:
        json.dump(log_entry,file)
        file.write("\n")
        
    print("Order recorded successfully!")