class Student:
    def __init__(self,name,age,rlno,course):
        self.name = name
        self.age = age
        self.rlno = rlno
        self.course = course

    def display(self):
        print(self.name,"\t",self.age,"\t",self.rlno,"\t",self.course)