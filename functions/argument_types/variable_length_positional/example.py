#*args collects extra positional arguments as a tuple.
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, "hello")
# Output:
# 1
# 2
# 3
# hello
