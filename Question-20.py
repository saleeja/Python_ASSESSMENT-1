"""20.Create a Python library with the function to input the values with 
expectation handling and demonstrate with the example."""



# Import the functions from your custom library
from myidgenerator import generate_unique_id,input_with_expectation

# Get user input for name and age using the custom input_with_expectation function
name = input_with_expectation("Enter your name: ", str)
age = input_with_expectation("Enter your age: ", int)
password= input_with_expectation("Enter your password:",str)

# Generate a unique ID using the custom generate_unique_id function
unique_id = generate_unique_id(name)

# Display registration information including name, age, and the generated unique ID
print(f"\nRegistration successful!\nName: {name}\nAge: {age}\nYour ID: {unique_id}")
print("Login with your ID and password.Thank you!")

