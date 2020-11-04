class student:
    def setName(self,name):
        self.name = name

    def setmarks(self,marks):
        self.marks = marks

    def getname(self):
        return self.name
    def getmarks(self):
        return self.marks
n = int(input("Please enter the no of entries: "))

for i in range(n):
    s = student()
    Name = input("Please enter the name: ")
    s.setName(Name)
    Marks = int(input("Please enter the marks: "))
    s.setmarks(Marks)

    print("Hi ",s.getname())
    print("Your marks are ",s.getmarks())
print("Next entry......")
print()
