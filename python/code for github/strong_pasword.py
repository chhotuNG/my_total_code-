pas = input("enter_pasword________: ")
C=0
S=0
s=0
N = 0
if len(pas) <=16 or len(pas) >= 8:
    print('length okkkk.......!!!')
    for i in pas:
        if i <= 'z' or i<= 'a' or  i<='Z' and i >='A' or i <= '9 ' or i >= '0':
            s+=1
            C+=19
            N +=1
        else:
            S+=1
    if s >= 1 and  S >=1 and  N >= 1 and  C >=1 :
        print("strong password")
    else:
        print('week pasword ')
else:
    print('length is not perfect....')

