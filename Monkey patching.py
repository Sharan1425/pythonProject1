class test():
    def __init__(self,x):
        self.x = x
    def get_data(self):
        print("Some code to run the database")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
t = test(5)
#t.f1()
#t.f2()
def new_getdata(self):
    print("Some code to run the new database")
test.get_data = new_getdata
print("After monkey patching")
t.get_data()