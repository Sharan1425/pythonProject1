s = open(r"C:\Users\Murugappa\Downloads\IMG_0187.jpg","rb")
wr = open(r"C:\Users\Murugappa\Desktop\testingimage.jpg","wb")
data = s.read()
print(data)
a = wr.write(data)
s.close()
wr.close()
print("New image is available in: New Folder")
