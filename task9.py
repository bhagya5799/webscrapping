import random
import time
import requests
from bs4 import BeautifulSoup
import os
import json

with open ("task5.json","r+")as file:
    a_data=json.load(file)
movie=a_data
def get_movie_details():
    random_sleep=random.randint(1,3)
    for i in movie:
        path=("/home/admin123/Desktop/task9/task9.py"+i["name"]+".json")
        if os.path.exists(path):
            pass
        else:
            data=open(path,"w+")
            json.dump(i,data,indent=4)
        time.sleep(random_sleep)

        # m_data=str(i)
        # create=path.write(m_data)
        # time.sleep(random_sleep)
        # path.close()
get_movie_details()
