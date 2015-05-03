
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup


# In[2]:

r1=requests.get("http://www.tv.com/")
anasayfa=BeautifulSoup(r1.text)


# In[3]:

anasayfa.title


# In[4]:

showlink= anasayfa.find("li", class_="shows")


# In[5]:

showlink


# In[6]:

showlinka= showlink.find("a")


# In[7]:

link=showlinka.get("href").strip()


# In[8]:

link


# In[9]:

r2=requests.get(link)


# In[10]:

link=BeautifulSoup(r2.text)


# In[11]:

link.title


# In[12]:

diziler=link.findAll("h4")


# In[12]:




# In[12]:




# In[13]:

diziler


# In[13]:




# In[13]:




# In[23]:

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
        for lm in kisi:
            isim=lm.find("a",itemprop="name")
            role=lm.find("div", class_="role")
            print isim.text + "          "+  role.text
        
            
        
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
        for lm in kisi:
            isim=lm.find("a",itemprop="name")
            role=lm.find("div", class_="role")
            print isim.text + "          "+  role.text
        
            
    
    
    
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[31]:

oyuncular


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[23]:




# In[24]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



