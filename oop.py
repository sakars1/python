# class Student:
#     def __init__(self):
#         print("Hello")
#     def display(self):
#         print("this is the display func")

# s1=Student()
# s1.display()
# s1=Student
# s1.display(s1)

class Student:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def display(self):
        print("name: ",self.name)
        print("Age: ",self.age)

s1=Student('sakar',24)
s1.display()

s2=Student('sabin',19)
s2.display()