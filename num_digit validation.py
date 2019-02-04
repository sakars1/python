while 1:
    name = input("Enter your name: ")
    age = input("Enter your date of birth: ")
    num = input("Enter your phone number: ")
    if name == '' or num == '' or age == '':
        print("Any field should not be blank...")

    elif name.isalpha() and age.isdigit() and int(age) > 18 and num.isdigit():
        print(name, '\n', age, '\n', num)
        break

    else:
        print("Name must only contain alphabets. Age must be greater than 18. Age and Number must be numeric...")
