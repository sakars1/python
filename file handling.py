# f=open('file.txt', 'w')
# f.writelines('Hello world from file ')

# with open("file.txt", "r") as f:
#     text = f.read()
#
# print(text)

f=open('file.txt', 'w')
text=input("write to the file.... write quit to stop")
while text!='quit':
    f.writelines(text+'\n')
    text=input()
print("done with writing now saving...")
f.close()