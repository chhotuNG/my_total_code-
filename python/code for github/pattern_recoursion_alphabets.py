
# # S
# def f1(row):
#     if row==10:
#         return 1
#     else:
#         def f2(col):
#             if col== 8:
#                 return 1
#             else:
#                 if (row==0 and col>0 and col < 5) or (row==1 and col==0) or (row==2 and col==0) or (row==3 and col==0) or (row==4 and col >0 and col <4) or (row==8 and col <4 ) or (row==5 and row+col==12) or (row==6 and row+col==13) or (row==7 and row+col==14):
#                     print("*",end=" ")
#                     f2(col+1)
#                 else:
#                     print(end=" ")
#                     f2(col+1)
#         f2(0)
#     print()
#     f1(row+1)
# f1(0)

# # C
# def f1(raw):
#     if raw==4:
#         return 1
#     else:
#         def f2(col):
#             if col == 4:
#                 return 1
#             else:
#                 if (raw==0 and col%4!=0) or (raw==1 and raw +col==1) or (raw==2 and raw+col==2) or (raw==3 and col%4!=0):
#                     print("*",end=" ")
#                     f2(col+1)
#                 else:
#                     print(end=" ")
#                     f2(col+1)
#         f2(0)
#     print( )
#     f1(raw+1)
# f1(0)

# # A
# def f1(row):
#     if row==7:
#         return 1
#     else:
#         def f2(col):
#             if col==5:
#                 return 1
#             else:
#                 if ((col==0 or col==4) and row !=0) or ((row==0 or row==3) and col>0 and col<4):
#                     print ("*",end=" ")
#                     f2(col+1)
#                 else:
#                     print (end="  ")
#                     f2(col+1)
#         f2(0)
#     print()
#     f1(row+1)
# f1(0)

# # mirror image of G


# def f1(row):
#     if row==7:
#         return 
#     else:
#         def f2(col):
#             if col==9:
#                 return
#             else:
#                 if (col==0 and row >1) or (col==3 and row<6 and row >1) or (row==6 and col==4)or(row==6 and col==5) or (row==6 and col==6) or (col==7 and row >0 and row <6 ) or(row ==1 and col <4):
#                     print("*",end=" ")
#                     f2(col+1)
#                 else: 
#                     print(end="  ")
#                     f2(col+1)
#         f2(0)
#     print()
#     f1(row+1)
# f1(0)


import time 
def time_convert(sec):
    mins=int(sec//60)
    sec=int(sec%60)
    hours=mins%60
    mins=mins%60
    print("time lapsed = {0}:{1}:{2}".format(hours, mins, sec))
input("press enter to start____:")
print("TIME HAS STARTED_____!!!!")
start_time=time.time()

input("press ENTER to stop___:")
print("TIME HAS STOPED_____!!!!")
end_time=time.time()
time_lapsed=end_time-start_time
time_convert(time_lapsed)