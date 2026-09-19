def USD_to_EUR(usd):
    return usd * 0.87

while True:
    price = float(input("Enter the price of the product: "))
    print("In Euro, it is: €", round(USD_to_EUR(price), 2))
    
    choice = input("Do you wish to continue?: ")
    if choice == "NO" or choice == "no":
        break
