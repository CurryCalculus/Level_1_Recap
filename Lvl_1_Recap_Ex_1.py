while True:
    num_1 = int(input("Enter a number (Choose 0 to exit): "))

    if num_1 == 0:
        print("You have exited this thing")
        break

    num_2 = int(input("Enter the second number: "))

    if num_1 > num_2:
        result = num_1
    elif num_2 > num_1:
        result = num_2
        print(f"The higher value is: {result}")
    else:
        print("The numbers are equal.")


