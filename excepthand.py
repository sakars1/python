# try:
#     a = int(input("Enter any num: "))
#     div = a/0
#     print(div)
# except ZeroDivisionError:
#     print("nothing can be divided by zero")
# except:
#     print("problem with your input")

# age = int(input("Enter your age: "))
# if age<18:
#     raise ValueError
# else:
#     print("accepted")

class LowAgeError(Exception):
    def __init__(self):
        super(LowAgeError, self).__init__("Age should be greater than 18")

age = int(input("Enter your age: "))
if age<18:
    raise LowAgeError
else:
    print("accepted")