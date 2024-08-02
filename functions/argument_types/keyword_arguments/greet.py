#Keyword arguments are passed using the name of the parameter, allowing you to specify them in any order.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="Bob")  # Output: Hello, Bob! You are 30 years old.

