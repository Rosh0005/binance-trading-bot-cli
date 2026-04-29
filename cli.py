from bot.utils import *
from bot.orders import place_order

while True :
    print("\n---New Order---")
    price = None
    symbol = input("Enter symbol : ").upper()
    side = get_side()
    order_type = get_order_type()
    if order_type == "LIMIT" :
        price = get_price()
    quantity = get_quantity()

    place_order(side,order_type,symbol,quantity,price)

    again = input("Do you want to place another order(yes/no) : ").lower()
    if again != "yes" :
        print("Exiting trading bot...")
        break