# lst_comp = [x for x in range(10)]
# gen_exp = (x for x in range(10))
# print("List compression>>>",lst_comp)
# print("Generator Expression>>>", gen_exp)
# for x in gen_exp:
#     print(x)


#map function
def cube(c):
    return c**3
lst=[1,2,3,4,5]
lst_n = list(map(cube,lst))
print(lst_n)

#lamda function
lst_n2 = list(map(lambda x:x**2,lst))
print(lst_n2)

#filter()
def is_even(n):
    if n%2==0:
        return 1
    else:
        return 0


num=[1,2,332,4,4,7,9,80,980,43,5,8,6,7]
lst = list(filter(is_even,num))
print(lst)

lst_comp = [x for x in range(2500) if not [y for y in range(2,x) if x%y==0]]
print(lst_comp)

