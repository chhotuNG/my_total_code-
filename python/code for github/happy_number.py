
num=int(input("enter number here__: "))
n=num
a=0
while a < 50:
    f=0
    for i in str(num):
        b=int(i)
        f+=b*b
    if f==1:
        print("happy number ")
        a+=50
    else:
        if f !=4:
            num=f
            f=a
            a+=1
        else:
            print("unhappy number ")
            a+=50