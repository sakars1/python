num = input("Enter a number to print multiplication table: ")
if not num.isdigit():
    print("You must Enter a number...")
for i in range(1, 11):
    print(num, 'x', i, "=", int(num)*i)
