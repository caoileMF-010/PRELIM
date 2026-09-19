while True:
    print("ARITHMETIC CALCULATOR")
    print("1. Addition\t2. Subtraction\t3. Multiplication")
    print("4. Division\t5. Modulus\t6. Increment\n7. Decrement")
    
    choice = int(input("Select an arithmetic operation: "))

    match (choice):
        case 1:
            x = float(input("Enter the value of x: "))
            y = float(input("Enter the value of y: "))
            sum = x + y
        
            print(f"Variable Values : x = {x}, y = {y}")
            print(f"Addition: x + y = {sum}")
        
        case 2:
            x = float(input("Enter the value of x: "))
            y = float(input("Enter the value of y: "))
            difference = x - y
        
            print(f"Variable Values : x = {x}, y = {y}")
            print(f"Subtraction: x - y = {difference}")
        
        case 3:
            x = float(input("Enter the value of x: "))
            y = float(input("Enter the value of y: "))
            product = x * y
        
            print(f"Variable Values : x = {x}, y = {y}")
            print(f"Multiplication: x × y = {product}")
        
        case 4:
            x = float(input("Enter the value of x: "))
            y = float(input("Enter the value of y: "))
            if y == 0:
                print("Division by 0 is not allowed, choose again.")
                break
            quotient = x / y
        
            print(f"Variable Values : x = {x}, y = {y}")
            print(f"Division: x ÷ y = {quotient}")
        
        case 5:
            x = float(input("Enter the value of x: "))
            y = float(input("Enter the value of y: "))
            modulus = x % y
        
            print(f"Variable Values : x = {x}, y = {y}")
            print(f"Modulus: x % y = {modulus}")
        
        case 6:
            x = float(input("Enter the value of x: "))
            increment = x+1
        
            print(f"Variable Values : x = {x}")
            print(f"Increment: x + 1 = {increment}")
        
        case 7:
            x = float(input("Enter the value of x: "))
            decrement = x-1
        
            print(f"Variable Values : x = {x}")
            print(f"Decrement: x - 1 = {decrement}")

        case _:
            print("Please choose again.")
        
    repeat = input(("Do you want to continue? (YES/NO): "))
    if repeat == "NO" or repeat == "no":
        break
    
    