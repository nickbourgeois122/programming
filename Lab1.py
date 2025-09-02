# Make sure you are not modifying the method signatures
# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    # TODO: Implement this function
    print("Hello, World!")
    pass  # Replace with your code
# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function
    print('Enter your name:') 
    name=str(input())
    print("Hello, "+name)
    print("Enter your age:")
    age=int(input())
    print("Your Age is, " +  str(age))
    print("Enter your height (feet):")
    height=float(input())
    print("Your height is "+ str(height))
def input_output2():
    name=str(input("Enter your name: "))
    age=int(input("Enter your age: "))
    height=float(input("Enter your height (feet): "))
    print(f"Hello {name}!")
    print(f"You are {age} years old!")
    print(f"You are {height} feet tall!")
hello_world()
input_output()
input_output2()