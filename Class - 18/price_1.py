#Using For Loop If Condition Without Filter Method And Functions
prices=[199,99,75,65,1999,2001,4000,6000]

new_price = []

for price  in prices :
    if price > 2000:
        new_price.append(price)

print(prices)
print(new_price)