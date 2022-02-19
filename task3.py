from task2 import*

import json


file=open("task2.json","r")
data=json.load(file)
# print(data)

def year_details():
    move_dec={}
    list1=[]
    for index in data:
        a=int(index)
        # print(type(a))
        mod=(a%10)
      
        decade=a-mod
        # print(decade)
        if decade not in list1:
            list1.append(decade)
        list1.sort()
    # print(list1)
    for i in list1:
        move_dec[i]=[]
    for i in move_dec:
        dec10=i+9
        for x in data:
    
            if int(x)<=dec10 and int(x)>=i:
                for v in data[x]:
                    move_dec[i].append(v)
    print(move_dec)
    with open("task3.json","w+")as file:
        json.dump(move_dec,file,indent=4)
        a=json.dumps(move_dec)
year_details()
# print(year_details)   




    
    




