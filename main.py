#fib
N = int(input("Please enter the range of fib series: "))
a = 0
b = 1
print(a)
print(b)
for i in range(N):
    c = a+b
    a,b = b,a+b
    print(c)