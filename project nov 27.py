# Function to calculate the circumference of a circle
def calculate_circumference(radius):
    circumference = 2 * 3.14159 * radius  # Formula: 2 * π * r
    return circumference

# Input radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the result
result = calculate_circumference(radius)
print(f"The circumference of the circle is: {result}")
