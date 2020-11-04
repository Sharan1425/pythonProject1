##picking
import pickle
class Student:
    def __init__(self,name,age,rlno,course):
        self.name = name
        self.age = age
        self.rlno = rlno
        self.course = course

    def display(self):
        print(self.name,"\t",self.age,"\t",self.rlno,"\t",self.course)
s = Student("Sai",25,500,"Artifical Inteligence")
with open(r"C:\Users\Murugappa\Desktop\Sai","wb") as file:
    pickle = pickle.dump(s,file)
    print("Object has been writen to the Sai file")
## Unpicking
import pickle
with open(r"C:\Users\Murugappa\Desktop\Sai","rb") as file:
    object = pickle.load(file)
    print("Below are the object details")
    object.display()


