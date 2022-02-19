
from task1 import*
movie_url="https://www.rottentomatoes.com/m/millennium_actress_2001" 
def scrap_movie_details(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,'html.parser')
    li=soup.find_all("li",class_="meta-row clearfix")
    title_div=soup.find('h1',class_='scoreboard__title').text
    details={}
    details["name"]=title_div
    for i in li:
        data=i.text
        k=data.split()
        # print(k)
        if "Rating:" in k:
            details["rating"]=k[1]
        if "Genre:" in k :
            details["Genare"]=k[1:]
            # a=k[1:]
            # b=" "
            # for i in a:
            #     b=b+i
            # b=b.split(",")
            # details["Director"]=b



        if "Language:" in k:
            details["Language"]=k[2:]

        if "Director:" in k:
            #  details["Director"]=k[1:]
            a=k[1:]

            # list=[]
            # b=" "
            # i=0
            # while i<len(a):
            #     b=b+a[i]
            # l=b.split(",")
            # details["Director"]=l
            b=" "
            for i in a:
                b=b+i
            b=b.split(",")
            details["Director"]=b

        if "Release:" in k:
            details["Release"]=k[2]
       
        if "Runtime:" in k:
            time=k[1:]
            i=0
            # print(time)
            
            while i<len(time):
                
                hour=time[0][0]
                minu=time[1]
                min=minu[:-1]
                # print(min,"m")

                # tom=int(hour)*60+int(min)
                i+=1
            tom=int(hour)*60+int(min)
            details["Runtime"]=tom
    with open("task4.json","w+") as file:
        json.dump(details,file,indent=4)
          
            # file.close()
        return details 
    # print(details)
    
scrap_movie_details(movie_url)