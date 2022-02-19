
import json
from textwrap import indent
from task1 import*
from task5 import*
tsk_a=open("task5.json","r+")
tsk_b=json.load(tsk_a)

dict={}
def analys_movie_ganer():
    for i in tsk_b:
        if "Genare" in i:
            a=i["Genare"]
            for j in a:
                if j in dict:
                    dict[j]+=1
                else:
                    dict[j]=1
            

        print(dict)

    with open("task11.json","w+")as file:
        json.load(dict,file,indent=4)


analys_movie_ganer()