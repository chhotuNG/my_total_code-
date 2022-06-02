import requests,json,os
from bs4 import BeautifulSoup




def top_movie_scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    main_div = soup.find('div',class_='lister')
    tbody = main_div.find('tbody',class_="lister-list")
    trs = tbody.find_all('tr')

    movie_url=[]


    for tr in trs:

        link = tr.find('td',class_='titleColumn').a['href']
        movie_link = 'https://www.imdb.com/'+link
        movie_url.append(movie_link)

    return movie_url


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
print("loading........................................")
scrap =top_movie_scrap(url)
print(scrap[0])



def scrap_movie_detail(movie_url):
    print(movie_url)
    page = requests.get(movie_url)
    soup = BeautifulSoup(page.text,'html.parser')

    # scrap movie name 
    name = soup.find('h1',attrs={"data-testid":"hero-title-block__title"}).get_text()

    # runtime scrap 
    run = soup.find('div',class_="sc-94726ce4-3 eSKKHi")
    time = run.find_all('li')
    li= []
    for i in time :
        li.append(i.get_text())
    for i in li:
        if len(i) == 6:
            s = ""
            for j in i :
                if j.isdigit() :
                    s+=j
                else:
                    s+=""
            runtime1=int(s[0])*60+(int(s[2])+int(s[1])*10)
    # scrap_movie_genre
    genre = soup.find('li',class_="ipc-inline-list__item ipc-chip__text").get_text()
    
    #scrap  bio 
    bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text

    # scrap director name 
    d_name=[]
    director_name=soup.find('div', class_="ipc-metadata-list-item__content-container")
    x=director_name.find_all("li",class_="ipc-inline-list__item")
    for i in x:
        d_name.append(i.a.get_text())


    # in this div i get country and laungauge details
    country=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
    language=[]
    language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
    x=language_name.find_all("li",class_="ipc-inline-list__item")
    for i in x:
        language.append(i.a.get_text())

    # scrap poster image url 
    poster_image_url=soup.find("img",class_="ipc-image")["src"]

    # scrap genre 
    li1 = []
    gen = soup.find_all('div',attrs={"data-testid":"genres"})
    for i in gen:
        for j in i :
            li1.append(j.text)

    # scrap contery name 
    con =  soup.find('li',attrs={"data-testid":"title-details-origin"}).a.text
    
    detail["country"] = con 
    detail["genre"] = li1
    detail["name"]= name
    detail["Director"] = d_name
    detail["Language"] = language
    detail['bio'] = bio
    detail["runtime"] = runtime1
    detail["Poster_image_url"] = poster_image_url


    return detail

detail = {'name':"","Director":"","country":'',"Language":"","Poster_image_url":"","runtime":"",'genre':""}
for url in scrap:
    print(scrap_movie_detail(url))
    break


##https://www.imdb.com/title/tt0068646
##  https://www.imdb.com/title/tt0111161/
