
# coding: utf-8

# In[1]:

import request
from bs4 import BeautifulSoup


# In[ ]:




# In[2]:

import requests
from bs4 import BeautifulSoup


# In[ ]:




# In[3]:

r1=requests.get("http://www.tv.com/")
anasayfa=BeautifulSoup(r1.text)


# In[ ]:




# In[4]:

anasayf


# In[ ]:




# In[5]:

link=anasayfa.find("li",class_="shows")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[15]:

link


# In[6]:

sitelink=link.find("a")


# In[ ]:




# In[17]:

sitelink


# In[7]:

shows= sitelink.get("href").strip()


# In[ ]:




# In[19]:

shows


# In[8]:

r2=requests.get(shows)


# In[ ]:




# In[9]:

itemsayfasi=BeautifulSoup(r2.text)


# In[ ]:




# In[23]:

itemsayfasi.title


# In[10]:

dizipanel=itemsayfasi.find("ul",class_="m hub_list")


# In[ ]:




# In[11]:

dizipane


# In[ ]:




# In[13]:

dizipanel.findAl("li")


# In[ ]:




# In[ ]:




# In[14]:

dizipanel.finAll("div",class_="info")






# In[15]:

dizilink=dizipanel.findAll("h4")







# In[17]:

diilink


# In[18]:

data={'isim':'', 'oylama':'', 'elestiri':'', 'summary':''}
obje=[]


# In[ ]:




# In[19]:

for lm in dizilink:
    sayfalar = lm.find("a")
    sayfalink=sayfalar.get("href").strip()
    #print sayfalink
    r3=requests.get("http://www.tv.com"+sayfalink)
    dizisayfasi=BeautifulSoup(r3.text)
    baslik=dizisayfasi.find("div",class_="m show_head")
    diziadi=baslik.find("h1")
    dizioylama=dizisayfasi.find("div", class_="score")
    dizireview=dizisayfasi.find("div", class_="last")
    review=dizireview.find("a")
    summary = dizisayfasi.find("span", itemprop="description")
    
    
    
    
    print diziadi.text+"(dizioylamasi:"+dizioylama.text+")"+"(elestirisayisi:"+review.text+")"
    print "SUMMARY"
    print summary.text
    print""
    data={'isim':diziadi.text, 'oylama':dizioylama.text, 'elestiri':review.text, 'summary':summary.text}
    obje.append(data)

    
    


# In[21]:

import json

with open('anasayfa.json', 'w') as outfile:
    json.dump(obje, outfile)


len(obje)



for lm in dizipanel:
    




