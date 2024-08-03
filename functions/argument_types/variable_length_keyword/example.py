#**kwargs collects extra keyword arguments as a dictionary.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Alice", age=30)  
# Output:
# name = Alice
# age = 30

