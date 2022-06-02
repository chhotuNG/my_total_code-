n=int(input("enter here nmber___: "))
a=str(n)
b=len(a)
sum=0
num=n
while n>0:
    re=int(n%10)
    f=1
    for i in range(1,re+1):
        f=i**b
    sum+=f
    n//=10
if sum == num:
    print(f"{num} is a armstrong number ")
else:
    print(f"{num} is not a armstrong number")