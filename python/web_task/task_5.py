# # from bs4 import BeautifulSoup
# # import requests,json

# # def scrap_movie_detail(movie_url):
# #     page = requests.get(movie_url)
# #     soup = BeautifulSoup(page.text,'html.parser')

# #     # scrap movie name 
# #     name=soup.find("h1", attrs={"data-testid":"hero-title-block__title"}).text
# #     # runtime scrap 
# #     run = soup.find('div',class_="sc-94726ce4-3 eSKKHi")
# #     time = run.find_all('li')
# #     li= []
# #     for i in time :
# #         li.append(i.get_text())
# #     for i in li:
# #         if len(i) == 6:
# #             s = ""
# #             for j in i :
# #                 if j.isdigit() :
# #                     s+=j
# #                 else:
# #                     s+=""
# #             runtime1=int(s[0])*60+(int(s[2])+int(s[1])*10)
# #     # scrap_movie_genre
# #     genre = soup.find('li',class_="ipc-inline-list__item ipc-chip__text").get_text()
    
# #     #scrap  bio 
# #     bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text

# #     # scrap director name 
# #     d_name=[]
# #     director_name=soup.find('div', class_="ipc-metadata-list-item__content-container")
# #     x=director_name.find_all("li",class_="ipc-inline-list__item")
# #     for i in x:
# #         d_name.append(i.a.get_text())


# #     # in this div i get country and laungauge details
# #     country=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
# #     language=[]
# #     language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
# #     x=language_name.find_all("li",class_="ipc-inline-list__item")
# #     for i in x:
# #         language.append(i.a.get_text())

# #     # scrap poster image url 
# #     poster_image_url=soup.find("img",class_="ipc-image")["src"]

# #     # scrap genre 
# #     li1 = []
# #     gen = soup.find('div',class_='sc-910a7330-10 dGYvJq').a.text
# #     li1.append(gen)

# #     # scrap contery name 
# #     con =  soup.find('li',attrs={"data-testid":"title-details-origin"}).a.text
    
# #     detail["country"] = con 
# #     detail["genre"] = li1
# #     detail["name"]= name
# #     detail["Director"] = d_name
# #     detail["Language"] = language
# #     detail['bio'] = bio
# #     detail["runtime"] = runtime1
# #     detail["Poster_image_url"] = poster_image_url


# #     return detail

# # detail = {'name':"","Director":"","country":'',"Language":"","Poster_image_url":"","runtime":"",'genre':""}

# # print("loading.....................")
# # x=scrap_movie_detail("https://www.imdb.com/title/tt0986264/")
# # with open("task4.json","w") as p:
# #     json.dump(x,p,indent=4)
    


# # # with open("task1.json","r") as p:
# # #     d=json.load(p)
# # # movies=[]
# # # for i in range(10):
# # #     movies.append(d[i]["url"])

# # # def get_movie_list_details(movies):
# # #     movies_details=[]
# # #     for i in movies:
# # #         movies_details.append(scrap_movie_detail(i))
# # #     return (movies_details)
# # # x=get_movie_list_details(movies)
# # # print("successfully run")
# # # with open("task5.json","w") as m:
# # #     json.dump(x,m,indent=6)


# import time
# from random import randint

# for i in range(1,45):
#     print('')

# space = ""
# for i in range(1,1000):
#     count = randint(1,100)
#     while True:
#         space+=" "
#         count-=1
#         if i%10 == 0:
#             print(')
#         space=""
#         time.sleep(0.2)
    
a=3
for i in range (1,9):
    if i < 5:
        for j in range(0,i):
            print("*",end=" ")
        print()
    elif i > 5:
        for k in range(0,a):
            print("*",end=" ")
        print()
        a-=1
    else:
        continue
 