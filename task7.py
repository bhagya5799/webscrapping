from  task5 import*
import json
with open ("task5.json","r") as file5:
    movie_list=json.load(file5)

def anylysis_director():
    dic={}
    # a=[]
    for i in movie_list:
        # print(i)
        if "Director" in i:
            for j in i["Director"]:
                # a.append(i["language"])
                if j in dic:
                    dic[j]=dic[j]+1

                if j not in dic:
                    dic[j]=1

    with open("task7.json","w+")as file:
        json.dump(dic,file,indent=4)
anylysis_director()
