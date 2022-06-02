# ##Progress Tracing Question:-
# 1###
# a=int(input("Enter any number:-"))
# a1=a%1000
# a2=a1%100
# a3=a//1000*100
# a4=a3+a2
# print(a4)
# # 2####
# n1 = int(input("Enter 1st number :"))
# n2 = int(input("Enter 2nd number :"))
# n3 = int(input("Enter 3rd number :"))

# if n1 > n2 and n1 > n3:
#  if n2>n3:
#    print("The 2nd largest number is",n2)
#  else:
#    print("The largest number is",n3)
# elif n2 > n1 and n2 >n3:
#  if n1 > n3:
#    print("The 2nd largest number is", n1)
#  else:
#    print("The 2nd largest number is", n3)
# else:
#  if n1 > n2:
#    print("The 2nd largest number is",n1)
#  else:
#    print("The 2nd largest number is", n2
# # 3######
# str1=input("Enter the string:-")
# alpha=0
# digit=0
# space=0
# special=0
# Alpha_count=0
# Digit_count=0
# Space_count=0
# Special_count=0
# for character in str1:
#    if character.isalpha():
#        Alpha_count=Alpha_count+1
#    elif character.isdigit():
#        Digit_count=Digit_count+1
#    elif character.isspace():
#        pass
#    else:
#        Special_count=Special_count+1
# print("Alpha Count", Alpha_count)
# print("Digit Count:-", Digit_count)
# print("Space count:-",Space_count)
# print("Special count:-",Special_count)
4####
# a=input("Enter any string:-")
# b=a.title( )
# print(b)
# ##5###
# n=int(input("Enter number of rows:-"))
# for i in range(1,n+1):
#    for j in range (n,0,-1):
#        if i>=j:
#            print(j,end=" ")
#        else:
#            print(" ",end=" ")
#    print()
###6
# n=int(input("Enter number of row"))
# for x in range (1,n):
#           print(((10**x-1)//9)*x)
###7
# rows=int(input("Enter the number of rows :")) 
# for i in range(1, rows + 1):
#    for j in range(rows-i):
#        print(" ",end=" ")
#    for j in range(1, i - 1):
#        print(j, end=" ")
#    for j in range(i - 1, 0, -1):
#        print(j, end=" ")
#    print()
# ##8##
# n=int(input("enter rows:-"))
# j=n-1
# for i in range(1,n+1):
#     print(''.join([' ']j +[str((10**i//9)*2)]))
#     j-=1
# # ###9##
# my_str= "navgurukul"    
# count = 0
# for i in my_str:
#    if i == "n":  
#        count = count + 1
# print(count)
# ###10##
# my_str="RAVINDRAVERMA"
# count='' ''
# for i in range (65,91):
#    if chr(i) in my_str:
#        c=my_str.count(chr(i))
#        for j in range(c):
#            count+=chr(i)
# print(count)
# #11##
# 3 input
#
# nothing={}
# while True:
#     name=input("enter your name____: ")
#     book_n=input("enter book name_____:")
#     q=int(input('enter quentity of book___'))
#     if name in nothing:
#         d={}
#         l=nothing[name]
#         for i in l:
#             for k in i:
#                 if book_n in i:
#                     for k in i:
#                         if k==book_n:
#                             i[book_n]+=q
#                 else:
#                     d[book_n]=q
#                     nothing[name]=l.append(d)
#     else:
#         d={}
#         l=[]
#         d[book_n]=q
#         l.append((d))
#         nothing[name]=l
#     print(nothing)





 