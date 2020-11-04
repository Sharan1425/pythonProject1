import re
Email = input("Please enter the Email ID: ")
Data = re.fullmatch("[a-zA-Z0-9-_.]*@[a-zA-Z]*[.]com",Email)
if Data != None:
    print(Email,"is vaid email id")
else:
    print(Email, "is invaid email id")