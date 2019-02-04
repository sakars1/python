number1 = 0

def add_num(number1,number2):
    return number1 + number2


def sub_num(number1,number2):
    return number1 - number2


def mul_num(number1,number2):
    return number1 * number2
def get_inp():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. EXIT")
    ch = int(input("Enter your choice from 0 to 4: "))

while 1:
    get_inp()
    if ch == 1:
        print("the sum is:", add_num(number1,number2))
        continue
    if ch == 2:
        print("the subtraction is:", sub_num(number1,number2))
        continue
    if ch == 3:
        print("the mul is:", mul_num(number1,number2))
        continue
    else:
        print("Exiting...")
        break
