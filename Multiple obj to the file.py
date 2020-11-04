import pickle,Emp
file = open(r"C:\Users\Murugappa\Desktop\testing.txt","wb")
n = int(input("Please enter the no of employees you want to enter: "))
for i in range (n):
    name = input("Please enter the name: ")
    age = int(input("Please enter the age:"))
    rlno = int(input("Please enter the Rollno:"))
    course = input("Please enter the course: ")
    obj = Emp.Student(name,age,rlno,course)
    pickle.dump(obj,file)
print("Details of the students have been added to specified file")


import Emp,pickle
file = open(r"C:\Users\Murugappa\Desktop\testing.txt","rb")
print("Students Details are:")
while True:
    try:
        obj = pickle.load(file)
        obj.display()
    except EOFError:
        print("All students are displied")
        break
file.close()