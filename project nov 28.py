# Function to handle shutdown conditions
def shutdown(input_value):
    if input_value == "Yes":
        return "Shutting down..."
    elif input_value == "No":
        return "Shutdown canceled."
    else:
        return "Sorry, invalid input."

# Input from the user
user_input = input("Do you want to shut down? (Yes/No): ")

# Call the function and display the result
print(shutdown(user_input))
