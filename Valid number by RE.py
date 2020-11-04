import re
n = input("Please enter the mobile no: ")
x = re.fullmatch("[7-9]\d{9}",n)
y = re.fullmatch("[0][7-9]\d{9}",n)
z = re.fullmatch("(\+91)?[7-9]\d{9}",n)
if x or y or z != None:
    print(n,"is a valid number")
else:
    print(n, "is a invalid number")