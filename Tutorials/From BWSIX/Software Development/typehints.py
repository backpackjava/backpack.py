# x: int = 10 # type hinting
# y: int = 1
# print(x,type(x))

def add_to_string(a: int | float, b: int | float) -> int | float: # type hinting doesn't change code flow at all
                                        # "|" means or
    return a + b                        # -> int shows us that the return value is of type int

print(type(add_to_string(1.3,2.2)))

try:                                        # interpreter tries to run this
    print(color)
except:
    print("No variable called \"color\"")   # but if it results in an error, except is run


# try:
#     x = int(input("Enter a number to divide by 10."))
#     y = 10/x
# except ValueError:
#     print("Stop")
# except ZeroDivisionError:
#     print("Stop")