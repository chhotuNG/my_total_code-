    #range of happy number 
s=int(input("enter starting number____: "))
e=int(input("enter ending number____: "))
for num in range(s,e+1):
    n=num
    a=0
    while a < 50:
        f=0
        for i in str(num):
            b=int(i)
            f+=b*b
        if f==1:
            print(n)
            a+=50
        else:
            num=f
            f=a
            a+=1