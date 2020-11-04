#fib
n = int(input("Please enter the range of fib series: "))
a = 0
b = 1
print(a)
print(b)
for i in range(n):
    c = a+b
    a,b = b,a+b
    print(c)