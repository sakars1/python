list1 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50]
print(list1)
del_val = input("Enter value you want to delete from list: ")
x = 0
for i in list1:
    if list1[x] == int(del_val):
        list1.pop(x)
    x += 1
print(list1)
