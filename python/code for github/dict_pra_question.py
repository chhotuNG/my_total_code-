
# create  a dictionary
# di=dict(name="chhotu",age=17,addres="katihar bihaar")
# # print(di)

# create a dictonary and find the key  and value 

# dic=dict(student1="chhotu",student2="giri",student3="ravindra",student4="bansi",student5="ashish")
# print(dic.keys())
# print(dic.values())
# print(dic["student4"])

# fruits={
#     1:"apple",
#     2:"banana",
#     3:"cherry"
#  }

# print(fruits)

# campus={
#     1:"navgurukul",
#     2:"in",
#     3:{'A':"welcome",
#     'B':"to",
#     'c':"dharmshala"

#      }
#  }
# print(type(campus))

# # # print(campus)

# person=dict(name='chhotu',age=17,gender="male")
# print(person.get("name"))
# result=person["age"]
# print(result)

# person.update({4:"oragnasation"})
# person.popitem()
# print(person)
# print(person)

# thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#  }
# for i ,j in thisdict.items():
#     print(i,j)
#     print(thisdict[i])

# thisdict.clear()
# print(thisdict)
# del thisdict["model"]
# print(thisdict)
# thisdict.popitem()
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# new=thisdict.copy()
# print(new)

#  new_dict=dict(thisdict)

#  print(new_dict)

#  neaseted dictionary

# my_family={
#   "child1":{
#     "name" : "abhijeet",
#     "age"  : 10
#   },
#   "child2":{
#     "name":"amrjeet",
#     "age":13
#   },
#   "child3": {
#     "name":"bansi",
#     "age":15
#   }
# }

# print(my_family)

# child1 = {
#     "name" : "abhijeet",
#     "age"  : 10
#   }
# child2={
#     "name":"amrjeet",
#     "age":13
#   }
# child3 =  {
#     "name":"bansi",
#     "age":15
#   }

# my_family={
#   "child1":child1,
#   "child2":child2,
#   "child3":child3
# }

# print(my_family)

# fromkeys() method 
# x=("key1","key2","key3")
# y=0
# di=dict.fromkeys(x,y)
# print(di)

# dictionary.setdefault(keyname, value)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model")

# print(x)
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model", "White")
# print(x)


# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# l1=list()
# for i in d.items():
#   l1.append(i)
# l1.sort()
# print(dict(l1))

# 1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# l1=list()
# for i in d.items():
#   l1.append(i)
# l1.sort()
# print("original dictionary is",d)
# print("aendingg order of dictionary")
# print(dict(l1))
# l1.reverse()
# print("deending order of dict is ",dict(l1))

# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# d={0: 10, 1: 20}
# d[2]=30
# print(d)

# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={**dic1,**dic2,**dic3}
# print(dic4)



# 4. Write a Python script to check whether a given key already exists in a dictionary. Go to the editor
# dic1={"name":"chhotu","age":17,"class":11}
# print("model" in dic1)

# 5. Write a Python program to iterate over dictionaries using for loops. Go to the editor
# dic1={"name":"chhotu","age":17,"class":11}
# for i in dic1.items():
#   print(i)



# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# num=int(input("enter the number : "))
# dic1=dict()
# for i in range(1,num+1):
#   dic1[i]=i*i

# print(dic1)

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# dic1=dict()
# for i in range(1,16):
#   dic1[i]=i*i
# print(dic1)


# 8. Write a Python script to merge two Python dictionaries. Go to the editor
# dic1={1:1,2:2,3:3}
# dic2={4:4,5:5,6:6}
# dic1.update(dic2)
# print(dic1)

# 9. Write a Python program to iterate over dictionaries using for loops. Go to the editor

# d = {'Red': 1, 'Green': 2, 'Blue': 3} 

# for color_key , value in d.items():
#   print(color_key,"value is",value)

# 10. Write a Python program to sum all the items in a dictionary. Go to the editor

# num=int(input("enter the number : "))
# dic1=dict()
# for i in range(1,num+1):
#   dic1[i]=1
# sum=0
# for i in range(1,num+1):
#   dic1[i]=i
# sum=0
# for j in dic1.values():
#   sum+=j
# print(sum)



# 11. Write a Python program to multiply all the items in a dictionary. Go to the editor

# num=int(input("enter the number : "))
# dic1=dict()
# for i in range(1,num+1):
#   dic1[i]=1
# for i in range(1,num+1):
#   dic1[i]=i
# product1=1
# for j in dic1.values():
#   product1*=j
# print(product1)




# 12. Write a Python program to remove a key from a dictionary. 

# myDict = {'a':1,'b':2,'c':3,'d':4}
# if "d" in myDict:
#   del myDict['d']
# print(myDict)

# 13. Write a Python program to map two lists into a dictionary. Go to the editor

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# dic1=dict()
# for i in range(len(keys)):
#   dic1[keys[i]]=values[i]
# print((dic1))

# 14. Write a Python program to sort a given dictionary by key. Go to the editor

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
# l=[]
# for i in color_dict.keys():
#   l.append(i)
# l.sort()
# for i in range(len(l)):
#   print(l[i],color_dict[l[i]])
	

# 15. Write a Python program to get the maximum and minimum value in a dictionary. Go to the editor


# num=int(input("enter the number : "))
# dic1=dict()
# for i in range(1,num+1):
#   dic1[i]=i
# l=[]
# for k in dic1.keys():
#   l.append(k)
# max1=max(l)
# min1=min(l)
# print("maximum value in dict ",max1)
# print("minimum value in dict ",min1)


# # 17. Write a Python program to remove duplicates from Dictionary. Go to the editor
# student_data={'id1':
# {'name':['sara'],
# 'class':['v'],
# 'subjet_integration':['english,math ,science']
# },
# 'id2':
# {'name':['dravid'],
# 'class':['v'],
# "subject_integration":["english,math,sciene"]
# },
# 'id3':
# {'name':['surya'],
# 'class':['v'],
# 'subjet_integration':['english,math ,science']
# },
# 'id4':
# {'name':['saurab'],
# 'class':['v'],
# "subject_integration":["english,math,sciene"]
# },
# }
# result={}
# for key,value in student_data.items():
#   if value not in result.values():
#     result[key]=value
# print(result)
# 18. Write a Python program to check a dictionary is empty or not. Go to the editor

# di={1:2,2:3}
# if not di:
#   print("empty dict")
# else:
#   print("list has items ")

# 19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# e={}
# for i in d1 :
#   if i not in d2 :
#     e[i]=d1[i]
#   else :
#     e[i]=(d1[i]+d2[i])
# for x in d2 :
#   if x not in e :
#     e[x]=d2[x]
# print(e)



# 20. Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}



# l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# s=set(())
# for i in l:
#   for j in i.values():
#     if j not in s:
#       s.add(j)
# print(s)




# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

# di={'1':['a','b'], '2':['c','d']}
# l=di['1']
# l1=di['2']
# for i in l:
#   for j in l1:
#     print(i+j)


# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary. Go to the editor


# 23. Write a Python program to combine values in python list of dictionaries. Go to the editor
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})



# 24. Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# st='w3resource'
# di=dict(())
# for i in st:
#   a=st.count(i)
#   di[i]=a
# print(di)

# 25. Write a Python program to print a dictionary in table format. Go to the editor

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print("c1  c2  c3")
# for key,value in my_dict.values():
#     for k in j:
#       print(k)


# 26. Write a Python program to count the values associated with key in a dictionary. Go to the editor
# Expected Output:
# 6
# 2
# student=[{'id':1,
# 'success':True,'name':'lary'},
# {'id':2,'success':True,'name':'Rabi'},
# {'id':3,"success":False,'name':'alex'}]
# sum1,sum2=0,0
# for d in student :
#     sum1+=d['id']
#     sum2+=d['success']
# print(sum1)
# print(sum2)



# 27. Write a Python program to convert a list into a nested dictionary of keys. Go to the editor


# num_list = [1, 2, 3, 4]
# new=current={}
# for i in num_list:
#   current[i]={}
#   current=current[i]
# print(new)

# 28. Write a Python program to sort a list alphabetically in a dictionary. Go to the editor


# 29. Write a Python program to remove spaces from dictionary keys. Go to the editor

# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# print("Original dictionary: ",student_list)
# for key in student_list.keys():
#     print(key)
# student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
# print("New dictionary: ",student_dict)


# 30. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
# d= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# l=list(d.values())
# max1=l[0]
# l1=[]
# for i in d.items():
#   l1.append(i)
# print(l1)

# 31. Write a Python program to get the key, value and item in a dictionary. Go to the editor

# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key value count")
# count=1
# for (key,value) in dict_num.items():
#     print(key,'  ',value,'  ',count)
#     count+=1

# 32. Write a Python program to print a dictionary line by line. Go to the editor
# students={'Alex':{'class':'v',
# 'roll_id':2},
# 'puja':{'class':'v',
# 'roll_id':3}
# }
# for i in students:
#     print(i)
#     for b in students[i]:
#         print(b,':',students[i][b])



# 33. Write a Python program to check multiple keys exists in a dictionary. Go to the editor

# student={
#     'name':"alex",
#     'class':"v",
#     'rool_id':'2'
# }
# print(student.keys()>={'name',"class"})

# 34. Write a Python program to count number of items in a dictionary value that is a list. Go to the editor

# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = 0
# for i in dict.values():
#     for value in i:
#         ctr+=1
# print(ctr)


# 35. Write a Python program to sort Counter by value. Go to the editor
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
# data={'Math':81, 'Physics':83, 'Chemistry':87}
# list1=sorted(data.values())
# result=[]
# for num in list1[::-1]:
#     for key ,value in data.items():
#         if num==value:
#             result.append((key,value))
# print(result)

# 36. Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
# Click me to see the sample solution

# 37. Write a Python program to replace dictionary values with their average. Go to the editor
# student_detail=[
# {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
# {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
# {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# D2={}
# for i in student_detail:
#     n=i.pop('V')
#     n2=i.pop('VI')
#     i["V+VI"]=(n+n2)/2
#     D2["id"]=i["id"]
#     D2["subject"]=i["subject"]
#     D2["V+VI"]=i['V+VI']
#     print(D2)



# 38. Write a Python program to match key values in two dictionaries. Go to the editor
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
# Click me to see the sample solution
# d,d1={'key1': 1, 'key2': 2, 'key3': 2}, {'key2': 2, 'key1': 1}
# for i in d:
#   if d[i]==d1[i]:
#     print("1 is present in both x and y")
#     break
#   else:
#     print("1 not present in both x and y ")
#     break

# 40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary. Go to the editor
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

# dict_nums=dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40)))
# print("original dictionary :")
# print(dict_nums)
# print(dict_nums["x"][4])
# print(dict_nums["y"][4])
# print(dict_nums["z"][4])
# for k ,v in dict_nums.items():
#     print(k,"has value",v)

# 41. Write a Python program to drop empty Items from a given Dictionary. Go to the editor
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# d={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dict1={key:value for (key,value)in d.items() if value is not None }
# print(dict1)

# 42. Write a Python program to filter a dictionary based on values. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
# m= {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d={}
# for key ,value in m.items():
#     if value > 170: 
#         d[key]=m[key]
# print(d)

# 43. Write a Python program to convert more than one list to nested dictionary. Go to the editor
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
# s=['S001', 'S002', 'S003', 'S004']
# s1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# n=[85, 98, 89, 92]
# l=[]
# for i in range(len(s)):
#     d={}
#     d1={}
#     a=s[i]
#     b=s1[i]
#     c=n[i]
#     d1[b]=c
#     d[a]=d1
#     l.append(d)    
# print(l)

# 44. Write a Python program to filter the height and width of students, which are stored in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

# l={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# d={key:value for key,value in l.items() if value[0] >= 6.0 and value[1] >= 70 }
# print(d)

# 45. Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
# Click me to see the sample solution
# d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# for value in d.values():
#     a=12
#     if value  == a:
#         print(value == a)
       





# 46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Go to the editor
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d1=[]
# for i in d:
#     if i[0] not in d1 :
#         d1.append(i[0])




# 47. Write a Python program to split a given dictionary of lists into list of dictionaries. Go to the editor
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
# d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# l=list((d.get("Science")))
# l1=list((d["Language"]))
# l3=[]
# for i in range(len(l)):
#     d1={}
#     d1["Science"]=l[i]
#     d1["language"]=l1[i]
#     l3.append(d1)
# print(l3)

# 48. Write a Python program to remove a specified dictionary from a given list. Go to the editor
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# l=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# l.remove(l[0])
# print(l)

# 49. Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
# sd=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# fd={}


# 50. A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary. Go to the editor
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# d1={}
# for i in d:
#     d[i].clear()
#     d1[i]=d[i]
# print(d1)

# 51. A Python Dictionary contains List as value. Write a Python program to update the list values in the said 
# dictionary. Go to the editor
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
# #           [1,1]                       [2,5]               [-3,6]
# sub= {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# d={}
# l=[]
# l2=[]
# for i in sub['Math']:
#     i+=1
#     l.append(i)
# d['Math']=l
# for j in sub['Physics']:
#     i
#     j+=2
#     l2.append(j)
# d["Phusics"]=l2
# d["Chemistry"]=sub['Chemistry']
# print(d)

# 52. Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]
# sub=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# subject=input("enter the subject name >>>> ")
# l=[]
# for i in sub:
#     for j in i:
#       if j==subject:
#           l.append(i[j])
# print(l)
# 53. Write a Python program to find the length of a given dictionary values. Go to the editor
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}

# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

# color={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# d={}
# for i in color.values():
#     d[i]=len(i)
# print(d)


# 55. Write a Python program to access dictionary key's element by index. Go to the editor
# Expected Output:
# physics
# math
# chemistry
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])

# 56. Write a Python program to convert a given dictionary into a list of lists. Go to the editor
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
# d= {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# l=[]
# for key in d:
#     l1=[]
#     l1.append(key)
#     l1.append(d[key])
#     l.append(l1)
# print(l)

# 57. Write a Python program to filter even numbers from a given dictionary values. Go to the editor
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}
# Click me to see the sample solution

# d= {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# d1={}
# for i in d:
#     l=[]
#     for j in d[i]:
#       if j%2 ==0:
#          l.append(j)
#     d1[i]=l
# print(d1)

# 58. Write a Python program to get all combinations of key-value pairs in a given dictionary. Go to the editor
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 3, 5], 'VI': [1, 5]}]
# Click me to see the sample solution

# d= {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# nl=[]
# for n in d:
#    d1=dict()
#    for n1,v in d.items():
# #       if n !=n1:
# #          #  print(n,'<first loop',n1)
# #           d1[n1]=v
# #    nl.append(d1)
# # print(nl)

# # 59. Write a Python program to find the specified number of maximum values in a given dictionary. Go to the editor
# # Original Dictionary:
# d={'a': 120, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 507, 'h': 8, 'i': 100}
# # 1 maximum value(s) in the said dictionary:
# # ['f']
# # 2 maximum value(s) in the said dictionary:
# # ['f', 'i']
# # 5 maximum value(s) in the said dictionary:
# # ['f', 'i', 'g', 'd', 'c']
# # Click me to see the sample solution
# l=list()
# for v in d.values():
#    print(v)
#    l.append(v)
# print(l)
# l.sort(reverse=True)
# l2=list()
# print(l)
# for num in l:
#    for k,v in d.items():
#       if v == num and k not in l2 :
#          l2.append(k)
# print(l2)

# 60. Write a Python program to find shortest list of values with the keys in a given dictionary. Go to the editor
# Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 
# Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']
# d={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 
# l=list()
# for i in d:
#    if len(d[i])==1:
#       l.append(i)
# print(l)


# 61. Write a Python program to count the frequency in a given dictionary. Go to the editor
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})
# Click me to see the sample solution
# d={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# l=list()
# for i in d:
#    l.append(d[i])
# print(l)
# d={}
# for j in l:
#    d[j]=d.get(j,0)+1
# print(d)

# 62. Write a Python program to extract values from a given dictionaries and create a list of lists from those values. Go to the editor
# Original Dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Extract values from the said dictionarie and create a list of lists using those values:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# [[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
# [['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]
# student_information=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# l=list()
# n=input("enter extra value >>>> ")
# for i in student_information:
#    l1=list()
#    for j in i.keys():
#       if j==n:
#          continue
#       else:
#          l1.append(i[j])
#    l.append(l1)
# print(l)

# 63. Write a Python program to convert a given list of lists to a dictionary. Go to the editor
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
# l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# d={}
# for i in l:
#    l1=i[1:]
#    for i in (i[:1]):
#       d[i]=l1
# print(d)


# 64. Write a Python program to create a key-value list pairings in a given dictionary. Go to the editor
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
# Click me to see the sample solution
# d={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# d1={}
# l=[]
# for k,v in d.items():
#    for j in v:
#       print(j)
#       d1[k]=j
# l.append(d1)
# print(l)

# 65. Write a Python program to get the total length of all values of a given dictionary with string values. Go to the editor
# Original dictionary:
# {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20
# color_dict= {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# a=0
# for v in color_dict.values():
#    for i in v:
#       a+=1
# print(a)

# 66. Write a Python program to check if a specific Key and a value exist in a dictionary. Go to the editor
# Original dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Check if a specific Key and a value exist in the said dictionary:
# True
# True
# True
# False
# False
# False
# student=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# print("original list >>")
# print(student)
# n=input("enter key >>>>  ")
# n1=(input("enter the value of key >>> "))
# for i in student:
#    if n in i.keys() and n1 in i.values() :
#       print( n in i.keys() and n1 in i.values())
#       break
#    else:
#       print( n in i.keys() and n1 in i.values())
#       break
# 67. Write a Python program to invert a given dictionary with non-unique hashable values. Go to the editor
# Sample Output:
# {8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}
# Click me to see the sample solution

# 68. Write a Python program to combines two or more dictionaries, creating a list of values for each key. Go to the editor
# Sample Output:
# Original dictionaries:
# {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# {'x': 300, 'y': 'Red', 'z': 600}
# Combined dictionaries, creating a list of values for each key:
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}


# 69. Write a Python program to group the elements of a given list based on the given function. Go to the editor
# Sample Output:
# Original list & function:
# [7, 23, 3.2, 3.3, 8.4] Function name: floor:
# Group the elements of the said list based on the given function:
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
# Original list & function:
# ['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
# Group the elements of the said list based on the given function:
# {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}


# 70. Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value. Go to the editor
# Sample Output:
# {1: 1, 2: 4, 3: 9, 4: 16}
# Click me to see the sample solution
# l=[1,2,3,4]
# d={}
# for i in l:
#   d[i]=i*i
# print(d)

# 71. Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list. Go to the editor
# Sample Output:
# Russell
# 2
# Click me to see the sample solution

# 72. Write a Python program to invert a dictionary with unique hashable values. Go to the editor
# Sample Output:
# {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}


# 73. Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key. Go to the editor
# Sample Output:
# Original list of dictionaries:
# [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# Convert a list of dictionaries into a list of values corresponding to the specified key:
# [18, 22, 20, 18]
# l=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# l1=[]
# for i in l :
#   l1.append(i["age"])
# print(l1)

# 74. Write a Python program to create a dictionary with the same keys as the given dictionary and values generated by running the given function for each value. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# Dictionary with the same keys:
# {'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}
# d={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# d1={}
# for i in d:
#   for j in i:
#     print(i[j])

# 75. Write a Python program to find all keys in the provided dictionary that have the given value. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty']
# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# l=[]



# 76. Write a Python program to combine two lists into a dictionary, where the elements of the first one serve as the keys and the elements of the second one serve as the values. The values of the first list need to be unique and hashable. Go to the editor
# Sample Output:
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# l1=['a', 'b', 'c', 'd', 'e', 'f']
# l2=[1, 2, 3, 4, 5]
# d={}
# for i in range(len(l2)):
#   d[l1[i]]=l2[i]
# print(d)
# 77. Write a Python program to convert given a dictionary to a list of tuples. Go to the editor
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

# color_dict={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# l=[]
# for i,j in color_dict.items():
#   l1=[]
#   l1.append(i)
#   l1.append(j)
#   l.append(tuple(l1))
# print(l)

# 78. Write a Python program to create a flat list of all the keys in a flat dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']

# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# l=[]
# for i in d:
#   l.append(i)
# print(l)
# 79. Write a Python program to create a flat list of all the values in a flat dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the values of the said flat dictionary:
# [19, 20, 21, 20]
# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# l=[]
# for i in d:
#   l.append(d[i])
# print(l)

# 80. Write a Python program to find the key of the maximum value in a dictionary. Go to the editor
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

# d={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# max1="Theodore"
# l=[]
# for i in d:
#   if d[i] > d[max1] :
#     max1=i
#     l.append(max1)
# min1="Theodore"
# for j in d:
#   if d[j] <= d[min1]:
#     min1=j
#     l.append(min1)
# print(tuple(l))


  
    




# #merakilearn.org

# Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.

# Example :-

# Code Example
# dict1={“name”:”Raju”, “marks”:56}

# Note :-
# If input is “name” then output will be “exist”

# If input is “class” then output will be “not exists”.

# dict1= dict1={'name':"raja",'marks':56}
# v=input("enter the key : ")
# if v in dict1:
#   print("exist in dict1")
# else:
#   print("not exist ")


# Ek program likhiye jo ki dictionaries ki values ka sum print kare.

# Example :-
# Input :-

# Code Example
# my_dict = {
#    'data1':100,
#    'data2': -54,
#    'data3': 247
#    }
# my_dict={
#   'data1':100,
#   'data2':-54,
#   "data3":247
# }

# sum =0
# for i in my_dict.values():
#   sum+=i
# print(sum)

# Write a program remove the first key value pair from a nested dictionary.

# Example :-
# Input :-

# Code Example
#     Dic= {
#   1: 'NAVGURUKUL',
#   2: 'IN',  
#     3:{ 
#     'A' : 'WELCOME',
#     'B' : 'To',
#     'C' : 'DHARAMSALA'
#    }
#   }

# Output :-
# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',
# 3:
# { 'B' : 'To',
# 'C' : 'DHARAMSALA'
# }
# }

# di={
#   1:"navgurkul",
#   2:'in',
#   3:{
#     'A':"welcome",
#     'b':"To",
#     'c':"Dharmshala",
#   }
# }
# d=di[3].copy()
# d.pop('A')
# di.popitem()
# di[3]=(d)
# print(di)

# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.

# Example :-
# Input :-

# Code Example
# list1=[“one”,”two”,”three”,”four”,”five”]

# list2=[1,2,3,4,5,]

# Output :-
# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# d={}
# for i in range(len(list1)):
#   d[list1[i]]=list2[i]
# print(d)

# l=[
#   {"first":"1"}, 
#   {"second": "2"}, 
#   {"third": "1"}, 
#   {"four": "5"}, 
#   {"five":"5"}, 
#   {"six":"9"},
#   {"seven":"7"}
# ]

