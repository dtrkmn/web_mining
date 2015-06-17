
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup


# In[3]:

r1=requests.get("http://www.tv.com/")
anasayfa=BeautifulSoup(r1.text)


# In[4]:

anasayfa.title


# In[5]:

showlink= anasayfa.find("li", class_="shows")


# In[6]:

showlink


# In[7]:

showlinka= showlink.find("a")


# In[8]:

link=showlinka.get("href").strip()


# In[9]:

link


# In[10]:

r2=requests.get(link)


# In[11]:

link=BeautifulSoup(r2.text)


# In[12]:

link.title


# In[13]:

diziler=link.findAll("h4")


# In[13]:




# In[13]:




# In[14]:

diziler


# In[14]:




# In[23]:

data={'title':'','oyuncu_ismi':'','rol':''}




# In[ ]:




# In[ ]:




# In[22]:

listoyuncu=[]


# In[ ]:




# In[ ]:




# In[24]:

for lm in diziler:
    dizilink=lm.find("a")
    linkler=dizilink.get("href").strip()
    print linkler
    
    
    r3=requests.get("http://www.tv.com"+linkler)
    itemsayfasi=BeautifulSoup(r3.text)
    try:
        cast=itemsayfasi.find("ul", class_="_nav_tabs narrow")
        oyuncular=cast.findAll("li")[3]
        oyuncu=oyuncular.find("a")
        oyuncu_bilgisi=oyuncu.get("href").strip()
        #print oyuncular.text
        r4=requests.get("http://www.tv.com"+oyuncu_bilgisi)
        cast_crew=BeautifulSoup(r4.text)
        print cast_crew.title
        person=cast_crew.find("ul", class_="persons _standard_list stars")
        kisi=person.findAll("li", class_="person")
        diziisim=cast_crew.find("div", class_="m show_head")
        dizi=diziisim.find("h1")
        print dizi.text
        dizi_ismi=dizi.text
        for lm in kisi:
            isim=lm.find("a",itemprop="name")
            role=lm.find("div", class_="role")
            print isim.text + "          "+  role.text
            data={'title':dizi_ismi,'oyuncu_ismi':isim.text,'rol':role.text}
            listoyuncu.append(data)
        
            
        
    except:
        cast=itemsayfasi.find("ul", class_="_nav_tabs")
        oyuncular=cast.findAll("li")[3]
        #print oyuncular
        oyuncu=oyuncular.find("a")
        oyuncu_bilgisi=oyuncu.get("href").strip()
        r4=requests.get("http://www.tv.com"+oyuncu_bilgisi)
        cast_crew=BeautifulSoup(r4.text)
        person=cast_crew.find("ul", class_="persons _standard_list stars")
        kisi=person.findAll("li", class_="person")
        diziisim=cast_crew.find("div", class_="m show_head")
        dizi=diziisim.find("h1")
        print dizi.text
        dizi_ismi=dizi.text
        for lm in kisi:
            isim=lm.find("a",itemprop="name")
            role=lm.find("div", class_="role")
            print isim.text + "          "+  role.text
            data={'title':dizi_ismi,'oyuncu_ismi':isim.text,'rol':role.text}
            listoyuncu.append(data)

            
    

    
    


# In[ ]:




# In[21]:

listoyuncu


# In[28]:

len(listoyuncu)
import json


# In[ ]:




# In[29]:

with open('oyuncular.json', 'w') as outfile:
    json.dump(listoyuncu, outfile)


# In[ ]:




# In[ ]:




# In[ ]:




# In[15]:




# In[15]:




# In[15]:




# In[15]:




# In[15]:




# In[15]:




# In[16]:

oyuncular


# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:




# In[16]:



