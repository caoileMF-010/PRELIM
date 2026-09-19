num = int(input("Enter a number that is a multiple of 5 between 1 and 100: "))

if num % 5 == 0:
    if num > 0 and num <= 100:
        print("The number you inputted is valid.")
    else:
        print("The number you inputted is invalid.")

else:
    print("The number you inputted is invalid.")

