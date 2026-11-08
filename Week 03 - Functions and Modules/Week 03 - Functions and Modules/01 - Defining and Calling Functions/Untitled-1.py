def add_tax(price):
    price = price * 1.2 
    return price  

total = 100 
total = add_tax(total)
print(total)  # 120.0