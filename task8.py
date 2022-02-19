import requests
# from bs4 import requests
import json
from task1 import*
import os
with open("task1.json","r+")as file:
    task1_data=json.load(file)
# a=movie_details
def scrap_movie_details():
    for i in task1_data:
        page=("/home/admin123/Documents/web scrapping (rotten)"+i["movie_name"]+".text")
        if os.path.exists(page):
            pass
        else:
            make=open(page,"w")
            movie_url=requests.get(i["url"])
            make.write(movie_url.text)
            make.close()
scrap_movie_details()
