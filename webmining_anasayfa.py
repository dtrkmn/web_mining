
# coding: utf-8

# In[1]:

import request
from bs4 import BeautifulSoup


# In[3]:

import requests
from bs4 import BeautifulSoup


# In[4]:

r1=requests.get("http://www.tv.com/")
anasayfa=BeautifulSoup(r1.text)


# In[5]:

anasayfa


# In[14]:

link=anasayfa.find("li",class_="shows")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[15]:

link


# In[16]:

sitelink=link.find("a")


# In[17]:

sitelink


# In[18]:

shows= sitelink.get("href").strip()


# In[19]:

shows


# In[20]:

r2=requests.get(shows)


# In[21]:

itemsayfasi=BeautifulSoup(r2.text)


# In[23]:

itemsayfasi.title


# In[31]:

dizipanel=itemsayfasi.find("ul",class_="m hub_list")


# In[32]:

dizipanel


# In[33]:

dizipanel.findAll("li")


# In[34]:

dizipanel.findAll("div",class_="info")


# In[36]:

dizilink=dizipanel.findAll("h4")


# In[37]:

dizilink


# In[48]:

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

for lm in dizipanel:
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



