#range of perfect number 
s=int(input("enter starting number___: "))
e=int(input("enter ending number___: "))
for p in range(s,e+1):
    n=p
    sum=0
    for i in range(1,p):
        if p%i==0:
            sum+=i
    if sum==n:
        print(n)