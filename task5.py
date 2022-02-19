from  task1 import movie_details
from Task4  import scrap_movie_details
import requests
import json
file=open("task1.json","r+")
data=json.load(file)
def top_movie_details():
    list=[]
    for i in data:
        movie_url=i["url"]
        a=scrap_movie_details(movie_url)
         
         
        # a=movie_details
        list.append(a)
    i["url"]
    with open("task5.json","w+")as file:
        json.dump(list,file,indent=4)
    return list
top_movie_details()



