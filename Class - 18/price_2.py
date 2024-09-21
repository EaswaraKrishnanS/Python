#Using Filter Method And Function
prices=[199,99,75,65,1999,2001,4000,6000]

def get_price (price):
    return price > 2000


new_price = list(filter(get_price,prices))
print(prices)
print(new_price)