import pickle
with open(r"C:\Users\Murugappa\Desktop\Sharan.txt","rb") as f:
    obj = pickle.load(f)
    print("Object is readable")
    obj.display()
