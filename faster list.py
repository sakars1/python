lst_comp = [x for x in range(10)]
gen_exp = (x for x in range(10))
print("List compression>>>",lst_comp)
print("Generator Expression>>>", gen_exp)
for x in gen_exp:
    print(x)