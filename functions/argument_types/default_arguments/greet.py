#Default arguments allow you to specify a default value for a parameter, which is used if no value is provided.

def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")

greet("Charlie")  # Output: Hello, Charlie! You are 25 years old.
greet("David", 40)  # Output: Hello, David! You are 40 years old.

