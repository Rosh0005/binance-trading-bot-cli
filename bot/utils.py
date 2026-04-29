def get_quantity() :
    while True :
        try :
            quantity = float(input("Enter quantity : "))
            if quantity > 0 :
                return quantity
            else :
                print("Please enter a positive number")
        except Exception :
            print("Please enter a valid number for quantity")

def get_price() :
    while True :
        try :
            price = float(input("Enter price :"))
            if price > 0 :
                return price
            else :
                print("Please enter a positive number")
        except Exception :
            print("Please enter a valid number for price")

def get_side() :
    while True :
        side = input("Do you want to BUY or SELL : ").upper()
        if side in ["BUY","SELL"] :
            return side
        print("Invalid Input. Please enter BUY or SELL")

def get_order_type() :
    while True :
        order_type = input("Enter order type(MARKET/LIMIT) : ").upper()
        if order_type in ["MARKET","LIMIT"] :
            return order_type
        print("Please enter MARKET or LIMIT")
    