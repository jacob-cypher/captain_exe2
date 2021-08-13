x=int(input("Enter a number:"))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(2,x):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
