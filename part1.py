
# coding: utf-8

# In[1]:

soup.title


# In[2]:

import requests
from bs4 import BeautifulSoup


# In[3]:

r = requests.get("http://acm.timus.ru/problemset.aspx?space=1&page=2")


# In[4]:

soup = BeautifulSoup(r.text)


# In[5]:

soup.title


# In[6]:

soup.a


# In[7]:

soup.a.text


# In[8]:

soup.a.text


# In[9]:

soup.a.get("href")


# In[10]:

soup.findAll("a")[3]


# In[11]:

soup.findAll("td", class_="panel")


# In[12]:

soup.findAll("td.panel")


# In[13]:

soup.select("a:first-child")


# In[14]:

prob_ids = []
rows = soup.select("table.problemset")[0].select("tr.content")
for row in rows[1:]:
  elem = row.findAll("td")[1]
  prob_ids.append(elem.text)
prob_ids[:4]    


# In[15]:

base_prob_page_url = "http://acm.timus.ru/status.aspx?space=1&num=%s&status=accepted&count=100"
for id in prob_ids:
    print base_prob_page_url % id


# In[16]:

r = requests.get(base_prob_page_url % 1103)
soup2 = BeautifulSoup(r.text)
rows = soup2.select("table.status")[0].select("tr")
for row in rows[2:7]:
  lang = row.findAll("td")[4].text
  runtime = row.findAll("td")[7].text
  print lang,runtime


# In[17]:

import time
import re

def process_page(prob_id, count=100, next_page=None):
    if (not next_page):
        url = base_prob_page_url % prob_id
    else:
        url = "http://acm.timus.ru/" + next_page + "&count=%d" % count
    print "Fetching %s" % url    
    result = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    rows = soup.select("table.status")[0].findAll("tr", recursive=False)
    for row in rows[2:-1]:
      # print row  
      try:   
        lang = row.findAll("td")[4].text
        runtime = row.findAll("td")[7].text
        entry_id = row.findAll("td")[0].text
      except:
         print row
         return None   
      result.append((entry_id, lang,runtime))
    elem = soup.find("td", class_="footer_right").findAll("a", href=re.compile("from"))
    if (elem == []):
        return result
    else:
        next_link = elem[0].get("href")
        time.sleep(1)
        return result + process_page(prob_id, count, next_link)



# In[18]:

result = process_page(1103)


# In[19]:

len(result)
result[-10:]


# In[20]:

result


# In[ ]:



