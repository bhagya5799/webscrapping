
import json
import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"

page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")#html .parser

def movie_details():
    l=[]
    divs=soup.find("div",class_= "panel-body content_body allow-overflow")
    tbody=divs.find("table",class_="table")
    tr=tbody.find_all("tr")
    for i in tr:
        dic={}
        td=i.find_all("td")
        for k in td:
            rank=i.find("td",class_="bold").get_text()[:-1]
            dic["Rank"]=int(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[:-1]
            dic["rating"]=float(rating)
            title=i.find("a",class_="unstyled articleLink")['href'] [3:]       
            dic["movie_name"]=str(title)
            reviews=i.find("td",class_="right hidden-xs").get_text()
            dic["reviews"]=int(reviews)
            year=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            dic["year"]=int(year)
            movieurl=title=i.find("a",class_="unstyled articleLink")['href']
            url="https://www.rottentomatoes.com"+movieurl
            dic["url"]=str(url)
        l.append(dic)
        if {} in l:
            l.remove({})
    with open("task1.json","w+") as file:
        json.dump(l,file,indent=4)
        return l
    


movie_details()
