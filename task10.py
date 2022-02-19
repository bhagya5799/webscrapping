
import json
tsk_a=open("task5.json","r+")
tsk_b=json.load(tsk_a)

def movie_direcotr_lang():
    list=[]
    for i in tsk_b:
        direct=i["Director"]
        for j in direct:
            if j not in list:
                list.append(j)
                print(list)
    # dict={}
    # for y in list:
    #     dic1={}
    #     for x in tsk_b:
    #         # if y in x["Language"]:
    #         if "Language" in x:
    #             for z in x["Language"]:
    #                 if z is dic1:
    #                     dic1[z]+=1
    #                 if z not in dic1:
    #                     dic1[z]=1
    #     dict[y]=dic1
    # print(dict)
    # with open("task10.json","w+")as file:
    #     json.dump(dict,file,indent=4)
    #     return dict
movie_direcotr_lang()