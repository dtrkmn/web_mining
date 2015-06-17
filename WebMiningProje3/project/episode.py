
# coding: utf-8

# In[1]:

import requests
import json 
from bs4 import BeautifulSoup


r1=requests.get("http://www.tv.com/")
anasayfa=BeautifulSoup(r1.text)


# In[2]:

import time
showlink= anasayfa.find("li", class_="shows")
showlinka= showlink.find("a")
link=showlinka.get("href").strip()
r2=requests.get(link)
link=BeautifulSoup(r2.text)
diziler=link.findAll("h4")


# In[22]:

data={'dizi isim':'','isim':'','episode':'','rate':'','description':''}
listem=[]


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[23]:

for lm in diziler:
    dizilink=lm.find("a")
    linkler=dizilink.get("href").strip()
   # print linkler
    
    
    r3=requests.get("http://www.tv.com"+linkler)
    itemsayfasi=BeautifulSoup(r3.text)
    try:
        episode=itemsayfasi.find("ul", class_="_nav_tabs narrow")
        episode_guide=episode.findAll("li")[1]
        season = episode_guide.find("a")
        season2= season.get("href").strip()
        r4=requests.get("http://www.tv.com"+season2)
        episode_bilgi=BeautifulSoup(r4.text)
        #print episode_bilgi.title
        sezon=episode_bilgi.find("ul", class_="filters")
      
        liste= sezon.findAll("li", class_="filter ")
        #print liste.text
        for i in liste:
            liste_a=i.find("a")
            liste_href=liste_a.get("href").strip()
            #print liste_href
            r5 = requests.get("http://www.tv.com" + liste_href)
            item_page=BeautifulSoup(r5.text)   
                        
            part=item_page.find("div",class_="m episode_list  _standard_module all_expanded")
            part1=part.find("ul", class_="episodes _toggle_list")
            part2= part1.findAll("li",class_="episode _clearfix")
            for lm in part2:
                title=lm.find("a", class_="title")
                rate=lm.find("div", class_="_rating")
                episode_number=lm.find("div", class_="ep_info")
                name_of_dizi=item_page.title.text
                description=lm.find("span", class_="_more_less")
                dizi_name=item_page.find("h1",itemprop="name")
                time.sleep(1)
                #print dizi_name.text
                data={'dizi isim':dizi_name.text,'isim':title.text,'episode':episode_number.text,'rate':rate.text,'description':description.text}
                listem.append(data)
                
                #print episode_number.text
                #print title.text + "("+rate.text +"/10.0)"
                # print ""
                #print description.text
                                 
    except:
        episode=itemsayfasi.find("ul", class_="_nav_tabs")
        episode_guide=episode.findAll("li")[1]
        season = episode_guide.find("a")
        season2= season.get("href").strip()
        r4=requests.get("http://www.tv.com"+season2)
        episode_bilgi=BeautifulSoup(r4.text)
        #print episode_bilgi.title
        sezon=episode_bilgi.find("ul", class_="filters")
      
        liste= sezon.findAll("li", class_="filter ")
        for i in liste:
            liste_a=i.find("a")
            liste_href=liste_a.get("href").strip()
            
            #print liste_href
            r5 = requests.get("http://www.tv.com" + liste_href)
            item_page=BeautifulSoup(r5.text)   
            part=item_page.find("div",class_="m episode_list  _standard_module all_expanded")
            part1=part.find("ul", class_="episodes _toggle_list")
            part2= part1.findAll("li",class_="episode _clearfix")
            for lm in part2:

                title=lm.find("a", class_="title")
                rate=lm.find("div", class_="_rating")
                episode_number=lm.find("div", class_="ep_info")
                description=lm.find("div", class_="description")
                name_of_dizi=item_page.title.text
                dizi_name=item_page.find("h1",itemprop="name")
                data={'dizi isim':dizi_name.text,'isim':title.text,'episode':episode_number.text,'rate':rate.text,'description':description.text}
                listem.append(data)

                #print title.text
                #print dizi_name.text
                
                
                #print title.text + "("+rate.text +"/10.0)"
               # prit ""
                    


# In[25]:

with open('episode.json','w') as outfile :
    json.dump(listem,outfile)


# In[ ]:




# In[24]:

len(listem)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



