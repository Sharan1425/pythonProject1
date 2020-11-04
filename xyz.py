list = []
alpha = "a"
for i in range(0,26):
    list.append(alpha)
    alpha = chr(ord(alpha)+1)
print(list)