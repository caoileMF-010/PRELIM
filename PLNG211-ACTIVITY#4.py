cost1 = float(input("Enter the cost of product 1: "))
cost2 = float(input("Enter the cost of product 2: "))

totalCost = cost1 + cost2

payment = float(input(f"Your total cost is {totalCost}, please enter your payment: "))

if payment < totalCost:
    while totalCost > 0:
        totalCost -= payment
        if totalCost < 0:
            print("Your change is", abs(round(totalCost, 2)),".")
            break
        payment = float(input(f"You still owe {totalCost} please enter your payment: "))
    print("Thank you for your payment!")

elif payment > totalCost:
    print("Thank you for your payment! Your change is", abs(round(totalCost, 2)),".")

else:
    print("Thank you for your payment!")

