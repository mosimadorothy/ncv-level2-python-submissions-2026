def order(item):
   
    print("Your order is: ", item)

def get_order():
    print("preparing order")
    return ("Order is ready")

def calcullate_total(item):
    base_price = 25.5
    vat = 1.15
    total_price = (base_price + len(item)) * vat
    return (f'Order Amount: R{round(total_price,2)}')





place_order =input("Enter the order ")





print("====================")
print(get_order())
order(place_order)
order_total = calcullate_total(place_order)
print(calcullate_total(order_total))
print("====================")
print("collect your", place_order)

