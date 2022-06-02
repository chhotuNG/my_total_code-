
# range of spy number 
s=int(input("enter starting number____: "))
e=int(input("enter ending number____: "))
print(f"{s} and {e} between spy number_____:")
for a in range(s,e+1):
    sum=0
    pro=1
    n=str(a)
    for i in n:
        sum+=int(i)
        pro*=int(i)
    if sum==pro:
        print(n)