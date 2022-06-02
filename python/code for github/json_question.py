
# # Q.1 Json data ko python object main convert karne ka program likho?.

# import json
# json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'

# python_ob=json.loads(json_obj)
# print("\n json data to python::::")
# print(python_ob)

# # Q.2 Python object ko json data main convert karne ka program likho?
# import json
# d={
#     "name":"chhotu",
#     "age":17,
#     "city":"dharmshala"}

# x=json.dumps(d)
# print(x)


# # Q.3 Python object ko json string mai convert karne ka program likho?

# d={
#     "name":"chhotu",
#     "age":17 ,
#     "city":"dharmshala"
# }
# x=json.dumps(d)
# print(x)
# print(type(x))

# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
# import json
# d={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4,
#     '5':8}

# x=json.dumps(d,sort_keys=True,indent=4)
# print(x)

# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

# import json 
# def is_complex_ob(object):
#     if  '__complex__' in object:
#         print(complex(object["real"],object["img"]))
#     else:
#         print(object)
# a='{"__complex__": true, "real": 4, "img": 5}'
# b='{"real": 4, "img": 5}'
# x=json.loads(a)
# is_complex_ob(x)
# x=json.loads(b)
# is_complex_ob(x)

# Q6.Python object key unique key value ko access karne ka program likho?
# import json 
# python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# print("original_object ")
# print(python_obj)
# x=json.loads(python_obj)
# print("unique_value ::::")
# print(x)

# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?


# Python program to convert text
# file to JSON
  
  
# import json
  
  
# the file to be converted to 
# json format
# filename = 'f.txt'
  
# dictionary where the lines from
# text will be stored
# dict1 = {}
  
# creating dictionary
# with open(filename) as fh:
  
#     for line in fh:
  
#         # reads each line and trims of extra the spaces 
#         # and gives only the valid words
#         command, description = line.strip().split(None, 1)
  
#         dict1[command] = description.strip()
  
# # creating json file
# # the JSON file is named as test1
# out_file = open("test1.json", "w")
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()


# filename="f.txt"
# dict1={}
# with open(filename) as fh:
#     for line in fh:
#         command, description=line.strip().split(None,1)
#         dict1[command]=description.strip()
# out_file=open("test2.json","w")
# json.dump(dict1,out_file,indent=4,sort_keys=False)
# out_file.close()


# Q8.Tumhare pass four employes ki details hai list mai:-


# Code Example
# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-


# Code Example
# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }
#
#
#

# Q8.Tumhare pass four employes ki details hai list mai:-


# Code Example
# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-

import json 
l1=['prem','prog','24','2400']
l2=['giri','try','34','3245']
l3=['raj','mat','44','2334']
l4=['name','post','age','sal']
e=['e1','e2','e3']
d={}
l=[l1,l2,l3]
a=0
for j in l:
    d11={}
    for k in range(len(j)):
            d11[l4[k]]=j[k]
    a+=1
    d["e{0}".format(a)]=d11
with open("fa.json","a") as file1:
    json.dump(d,file1,indent=6)