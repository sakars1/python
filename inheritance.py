class Child:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Child):
    def __init__(self,degree,Child):
        self.degree=degree
        self.name=Child.name
        self.age=Child.age

    def details(self):
        print(self.name)
        print("Degree :",self.degree)


s1=Child('sakar',24)
s2=Student(12,s1)
s2.display()
s2.details()
