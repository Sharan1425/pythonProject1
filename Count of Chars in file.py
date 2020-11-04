import os
fname = input("Please enter the file name: ")
if os.path.isfile(fname):
    lineC = WordC = CharC = 0
    f = open(fname,"r")
    for i in f:
        lineC = lineC+1
        x = i.split()
        WordC = WordC + len(x)
        CharC = CharC + len(i)
    print("There are {} lines in the file".format(lineC))
    print("There are {} Words in the file".format(WordC))
    print("There are {} CharC in the file".format(CharC))
    f.close()
    print(f.closed)

else:
    print(fname,"file does not exist")


