# # # if you want to scrape a website :
# # # use the API 
# # # HTML web Scraping using some tool like bs4


# import requests 
# from bs4 import BeautifulSoup 
# url="http://codewithharry.com"
# # step 1: Get the HTML 
# content = requests.get(url)
# htmlcontent = content.content
# # print(htmlcontent)
# # step 2 
# soup = BeautifulSoup(htmlcontent,'html.parser')
# # print(soup.prettify)

# # # step 3 : HTML tree treversal 
# # # 1.tags
# # # 2.navigableString
# # # 3. Beautifulsoup 
# # # 4.comments


# # title = soup.title

# # print(type(soup))   #   <class 'bs4.BeautifulSoup'>
# # print(type(title))  #   <class 'bs4.element.Tag'>
# # print(type(title.string)) # <class 'bs4.element.NavigableString'>
# # print(title)

# # # get all the  peras of the from page

# # peras = soup.find_all('p')
# # # print(peras)


# # # get all the  anchor tags from  of the  page

# anchors = soup.find_all('a')
# # print(anchors)

# # # get first elements for the html page 
# # # print(soup.find('p'))

# # # get classes of any  elements  in the html page 

# print(soup.find('p')['class'])

# # # find all the elements withclass elements lead 

# print(soup.find_all('p',class_='lead'))

# # # Get the text from the tags/soup 

# print(soup.find('p').get_text())

# # # Get text of html page 

# print(soup.get_text())

# # # Get all the link from html page 

# # anchors = soup.find('P')

# # print(anchors)

# # all_link = set()

# # for link in anchors:
# #     if (link.get('href') != '# '):
# #         linktext = 'http://codewithharry.com'+link.get('href')
# #         all_link .add(link)
# #         print(linktext)


a = "this is a book"
b = a.replace(" ","")
print(b)