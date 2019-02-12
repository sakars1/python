# f=open('file.txt', 'w')
# f.writelines('Hello world from file ')

with open("file.txt", "r") as f:
    text = f.read()

print(text)