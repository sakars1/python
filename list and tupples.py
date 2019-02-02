# marks = []
# i = 0
# while i < 5:
#     marks.append(input("Enter marks"))
#     i = i+1
# sum = 0
# for mark in marks:
#     sum += int(mark)
# print("the sum is :", sum)

# string = input("Enter your string: ")
# w_string = input("which string to count: ")
#
# count = string.count(w_string)
# print(count)

# list1 = [1, 2, 5, 20, 30, 19]
# minn = min(list1)
# maxxm = max(list1)
# sum = minn + maxxm
#
# print("the sum of max and min is: ", sum)

# strr = input("Enter your string: ")
# rep = input("Enter string to replace: ")
# new_s = input("replaced string: ")
# new = strr.replace(rep, new_s)
# print(new.upper())

# list1 = [1, 2, 3, 4, 5, 5, 6, 7, 8]
#
# length = len(list1)
#
# list1.pop(0)
# list1.append(30)
# print(list1)
#

# marks = int(input("Enter your mark: "))
# if (marks >= 90) and (marks <= 100):
#     print("you grade is A")
# elif (marks >= 70) and (marks < 90):
#     print("you grade is B")
# elif (marks >= 40) and (marks < 70):
#     print("you grade is C")
# elif marks < 40:
#     print("you are fail")
# else:
#     print("you are an alien")
#
# a = (input("Enter your name: "))
# if a.isalpha() == True and len(a) >= 3:
#     print("valid")
# else:
#     print("not valid")
# print("1 \n 2 \n 3 \n 4 \n 5")
# for i in range(1,100):
#     print(i)
name = input("Enter your name: ")
while name.isalpha() == False:
    print("invalid name...")
    name = input("Enter your name again: ")
print("Welcome "+name)
