
from task1 import*
import json

data=open("task1.json","r")
data1=json.load(data)
# print(data1)

def group_by_year():
    empt={}
    for i in data1:
        a=[]
        year=i["year"]
        if year not in empt:
            for key in data1:
                if year==key["year"]:
                    a.append(key)
            empt[year]=a
    with open("task2.json","w+")as file:
        json.dump(empt,file,indent=4)
        a=json.dumps(empt)
group_by_year()

