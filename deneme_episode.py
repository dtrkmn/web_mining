
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup


# In[3]:

r1=requests.get("http://www.tv.com/")
anasayfa=BeautifulSoup(r1.text)


# In[4]:

anasayfa.title


# In[4]:




# In[5]:

showlink= anasayfa.find("li", class_="shows")


# In[5]:




# In[6]:

showlink


# In[7]:

showlink


# In[7]:




# In[8]:

showlinka= showlink.find("a")


# In[9]:

link=showlinka.get("href").strip()


# In[10]:

link


# In[11]:

r2=requests.get(link)


# In[12]:

link=BeautifulSoup(r2.text)


# In[13]:

link.title


# In[14]:

diziler=link.findAll("h4")


# In[15]:

diziler


# In[ ]:

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
        print liste.text
        for i in liste:
            liste_a=i.find("a")
            liste_href=liste_a.get("href").strip()
            print liste_href
            r5 = requests.get("http://www.tv.com" + liste_href)
            item_page=BeautifulSoup(r5.text)   
            print item_page.title
            part=item_page.find("div",class_="m episode_list  _standard_module all_expanded")
            part1=part.find("ul", class_="episodes _toggle_list")
            part2= part1.findAll("li",class_="episode _clearfix")
            for lm in part2:
                title=lm.find("a", class_="title")
                rate=lm.find("div", class_="_rating")
                episode_number=lm.find("div", class_="ep_info")
             
                description=lm.find("span", class_="_more_less")
                print episode_number.text
                print title.text + "("+rate.text +"/10.0)"
                print ""
                print description.text
             
                
                
    
    
    except:
        episode=itemsayfasi.find("ul", class_="_nav_tabs")
        episode_guide=episode.findAll("li")[1]
        season = episode_guide.find("a")
        season2= season.get("href").strip()
        r4=requests.get("http://www.tv.com"+season2)
        episode_bilgi=BeautifulSoup(r4.text)
        print episode_bilgi.title
        sezon=episode_bilgi.find("ul", class_="filters")
      
        liste= sezon.findAll("li", class_="filter ")
        for i in liste:
            liste_a=i.find("a")
            liste_href=liste_a.get("href").strip()
            
            print liste_href
            r5 = requests.get("http://www.tv.com" + liste_href)
            item_page=BeautifulSoup(r5.text)   
            print item_page.title
            part=item_page.find("div",class_="m episode_list  _standard_module all_expanded")
            part1=part.find("ul", class_="episodes _toggle_list")
            part2= part1.findAll("li",class_="episode _clearfix")
            for lm in part2:
                title=lm.find("a", class_="title")
                rate=lm.find("div", class_="_rating")
                episode_number=lm.find("div", class_="ep_info")
                description=lm.find("div", class_="description")
                print episode_number.text
                print title.text + "("+rate.text +"/10.0)"
                print ""
                print description.text
                    


# In[ ]:




# In[1]:




# In[ ]:




# In[36]:




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




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[15]:




# In[ ]:



