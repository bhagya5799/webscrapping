from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json
url="https://www.rottentomatoes.com/m/inside_out_2015"
def movie__actor_details():
    sample=requests.get(url)
    soup=BeautifulSoup(sample.text,"html.parser")

    a=soup.find("div",class_="castSection")
    d1=a.find_all("div",class_="cast-item media inlineBlock")
  
    d2=a.find_all("div",class_="cast-item media inlineBlock moreCast hide")
    # print(d1)

    list=[]
    for i in d1:
        dic={}
        a=i.find("a")["href"][11:]
        dic["actor_name"]=a
        list.append(dic)

    for j in d2:
        dict1={}
        a1=j.find("a")["href"][11:]
        dict1["actor_name"]=a1
        list.append(dict1)
    # print(list)
    with open("task12.json","w+")as file:
        json.dump(list,file,indent=4)



movie__actor_details()

