s = int(input('enter starting number____: '))
e = int(input("enter ending number ____: "))

for n in range(s,e+1):
    a=str(n)
    b=len(a)
    sum=0
    num=n
    while n >0:
        re=int(n%10)
        f=1
        if re !=0:
            for i in range(1,re+1):
                f=i**b
        else:
            f=re*re
        sum+=f
        n//=10
    if sum==num:
        print(num)
    else:
        sum=0