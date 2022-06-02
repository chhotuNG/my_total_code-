
# # 1. Write a Python program to read an entire text file. Go to the editor
# # Click me to see the sample solution
# f = open("question.txt","r")
# print(f.read())
                
# 2. Write a Python program to read first n lines of a file. Go to the editor

# with open("ck.txt") as f:
#     n = int(input("Please Enter the number of lines to be read in your File: "))
#     a = 0   
#     while a!=n:
#         line = f.readline()
#         print(line, end="")
#         a = a + 1

# 3. Write a Python program to append text to a file and display the text. Go to the editor
# a=input("enter the any string____: ")
# f = open("ck.txt","a")
# f.write("\n")
# f.write(a)
# f.close()
# # after the append in file 
# with open("ck.txt") as f:
#     print(f.read())


# 4. Write a Python program to read last n lines of a file. 
# n=int(input("enter num:"))
# with open('ck.txt') as f:
#     for i in (f.readlines()[-n:]):
#             print(i,end='')


# 5. Write a Python program to read a file line by line and store it into a list. Go to the editor
# Click me to see the sample solution
# def f(n):
#     with open(n) as f1:
#         content=f1.readlines()
#         print(content)
# f("ck.txt")

# 6.Python – Copy all the content of one file to another file in uppercase

# f1=open("ck.txt","r")
# f2=open("out_put","a")
# for line in f1:
#     f2.write(line.upper())
# # after addin file is onther file 
# f=open("out_put","r")
# print(f.read())

# # 7.Python program to reverse the content of a file and store it in another file
# f1=open("b.txt","r")
# with open("a.txt","r") as f2:

# 8. Write a python program to find the longest words. Go to the editor
# def longest_word_find(filename):
#     with open(filename,'r') as f:
#         contents = f.read().split(" ")
#         length = 0
#         for i in contents:
#             if len(i)>length:
#                 length = len(i)
#                 longest_word = i
#                 return longest_word
# print(longest_word_find("a.txt"))






# Q) create 3 file simla.txt ,delhi.txtand other .txt. whoever live in simla put them simla.txt and delhi in delhi.txt and other in other.txt 
# RISHABH - MEERUT
# IMTIYAZ - DELHI
# NILIMA - COCHIN
# RATI - SHIMLA
# AYISHAH - DELHI
# RAGHU - SHIMLA
# NASEER - KANPUR
# KARTHIKEYAN - DELHI
# SALMA - JAIPUR
# PANKAJ - DELHI
# BRIJESH - DELHI
# GOVIND - DELHI
# PUNEET - SHIMLA
# SIDDHI - DELHI
# SUMAN - JAIPUR
# RAJEEV - SHIMLA
# MOHINDER - DELHI
# RAJENDRA - JAIPUR
# PRIYANKA - SHIMLA
# NEELA - DELHI
# SASHI - JAIPUR
# SARIKA - DELHI
# DEEPTI - SHIMLA
# HARSHAD - DELHI
# TRISHNA - RAIPUR
# PRADEEP - JAIPUR
# SEKHAR - DELHI
# NAND - DELHI
# ANOOP - DELHI
# BALWINDER - TOKYO

# for i in open("ck.txt","r"):
#     if "delhi" in i:
#         f=open("delhi.txt","a")
#         f.write(i)
#         f.write("\n")
#         f.close()
#     elif "shimla" in i :
#         f=open("shimla.txt","a")
#         f.write(i)
#         f.write("\n")
#         f.close()
#     else:
#         f=open("other.txt","a")
#         f.write(i)
#         f.write("\n")
#         f.close()
# print("succussfull !!!")