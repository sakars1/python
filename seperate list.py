list1 = [1, 2, "sakar", "subedi", 1.2, 2.5]
i = 0
int_list = []
str_list = []
fl_list = []
for x in list1:
    if type(x) == str:
        str_list.append(x)
    if type(x) == int:
        int_list.append(x)
    if type(x) == float:
        fl_list.append(x)
print(int_list)
print(str_list)
print(fl_list)
