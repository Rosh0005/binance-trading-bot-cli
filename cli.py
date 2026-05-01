import json
from bot.utils import *
from bot.orders import place_order

while True :
    print("\n===== Trading Bot =====")
    print("1. Place Order")
    print("2. View Order History")
    print("3. Exit")
    choice = input("Enter your choice : ")
    if choice == "1" :
        print("\n---New Order---")
        price = None
        symbol = input("Enter symbol : ").upper()
        side = get_side()
        order_type = get_order_type()
        if order_type == "LIMIT" :
            price = get_price()
        quantity = get_quantity()
        place_order(side,order_type,symbol,quantity,price)
        print("\n------------------------------------------")

    elif choice == "2" :
        print("\n---Order History---")
        try :
            with open("orders.log","r") as file :
                for line in file :
                    if line.strip() == "" :
                        continue
                    try :
                        order = json.loads(line)
                        print(f"\nTime       : {order.get('time', 'N/A')}")
                        print(f"Symbol       : {order.get('symbol', 'N/A')}")
                        print(f"Side         : {order.get('side', 'N/A')}")
                        print(f"Order Type   : {order.get('order_type', 'N/A')}")
                        print(f"Quantity     : {order.get('quantity', 'N/A')}")
                        print(f"Price        : {order.get('price', 'N/A')}")
                        print(f"Market Price : {order.get('market_price', 'N/A')}")
                        print(f"Status       : {order.get('status', 'N/A')}")
                    except json.JSONDecodeError :
                        print("Skipping invalid log entry...")
                        continue
        except FileNotFoundError :
            print("No orders found yet.")

    elif choice == "3" :
        print("Exiting Trade Bot...")
        break

    else :
        print("Invalid Input. Please enter 1, 2 or 3")