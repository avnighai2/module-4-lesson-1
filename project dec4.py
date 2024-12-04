def check_age():
    try:
        # Prompt the user to enter their age
        age = int(input("Enter your age: "))
        
        # Check if the number is odd or even
        if age % 2 == 0:
            print("The age entered is even.")
        else:
            print("The age entered is odd.")
    except ValueError:
        # Handle invalid input
        print("Invalid input! Please enter a valid integer value.")

# Call the function
check_age()
