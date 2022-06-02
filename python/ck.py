# import requests,json,os
# if not os.path.exists("courses.json"):
#     x = requests.get('http://saral.navgurukul.org/api/courses')
#     a = (x.json())

#     with open("courses.json","w") as f:
#         json.dump(a,f,indent=6)
# d={}
# with open("courses.json","r") as file:
#     jsdata = file.read()
#     # pares
#     obj= json.loads(jsdata)
#     av = (list(obj["availableCourses"]))
#     p=1
#     for i in av:
#         for k in i.keys():
#            if k=='name':
#                d[f"{p}"]=i['name']
#                p+=1
# for k,v in d.items():
#     print(k,v)
# n=input("choose your courses_____: ")               
# for k,v in d.items():
#     if k==n:
#         ch_s=v
# z=0
# with open("courses.json","r" ) as f1:
#     jsdata=f1.read()
#     obje=json.loads(jsdata)
#     ab=list(obje["availableCourses"])
#     for i in ab:
#         for k,v in i.items():
#             if v==ch_s and z < 1:
#                 id_s=(i['id'])
#                 z+=1
# print(id_s)
# if not os.path.exists("course_list.json"):
#     coure=requests.get(f'http://saral.navgurukul.org/api/courses/{id_s}/exercises')
#     cu=coure.json()
#     with open("course_list.json","w") as f2:
#             json.dump(cu,f2,indent=6)
# with open("course_list.json","r") as f3:
#     a=(f3.read())

# li1=['id','slug',"parent_exercise_id","name","sequence_num","github_link"]
# for l in li1:
#     print(l)
# s=input("select____:  ")
# with open("course_list.json","r") as f3:
#     jsd=f3.read()
#     ob=json.loads(jsd)
#     for l in ob.values():
#         for v in l:
#             for k1, v1 in v.items():
#                 if k1==s:
#                     print(k1,v1)

