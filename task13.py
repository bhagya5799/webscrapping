import json
# from textwrap import indent
from Task4 import movie_details
from task12 import movie__actor_details
url="https://www.rottentomatoes.com/m/millennium_actress_2001"
list13=[]
def movie_full_details():
    dic13={}
    details=movie_details(url)
    
    

    cast=movie__actor_details(url)
    details["cast"]=cast
    list13.append(details)
    print(list13)

    # with open("task13.json","w+")as file:
    #     json.dump(list13,file,indent=4)
    # return list13
movie__actor_details( )