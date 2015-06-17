#!/usr/bin/python

import sys
import os
import json 
import operator
import re
import web
import time
import codecs

urls = (
    '/chart1', 'chart1',
    '/chart2', 'chart2',
    '/chart3', 'chart3',
    '/chart4', 'chart4',
    '/query_title', 'find_titles',
    '/', 'index',
    '/chart1_query', 'chart1_query',
    '/chart2_query', 'chart2_query',
    '/chart3_query', 'chart3_query',
    '/chart4_query', 'chart4_query',
    
   )
   
rate=json.load(open("episode2.json"))
elestiri=json.load(open("anasayfa2.json"))
rate1=json.load(open("anasayfa2.json"))


render = web.template.render("templates", base="base")


###############################################################################

class chart1:
    def GET(self):
       return render.chart1()
class chart2:
    def GET(self):
       return render.chart2()
class chart3:
    def GET(self):
       return render.chart3()
class chart4:
    def GET(self):
       return render.chart4()
	   
############################################TOP 10#####################################################


class chart1_query:
	
	#rate1 = sorted(rate1, key=lambda k: k['oylama'], reverse=True)
	
	def GET(self):
		obje2=[]
		rate1=json.load(open("anasayfa2.json"))
		rate1 = sorted(rate1, key=lambda k: k['oylama'], reverse=True)
		for i in rate1[0:10]:

	
			data={'isim':i["isim"].encode('utf8'), 'oylama':float(i["oylama"])}
			obje2.append(data)
		obje2 = sorted(obje2, key=lambda k: k['oylama'], reverse=True)
		print json.dumps(obje2)
		return json.dumps(obje2)
		

#################################SOCİAL ANALYSİS##############################
		
class chart4_query:
	
	#rate1 = sorted(rate1, key=lambda k: k['oylama'], reverse=True)
	
	def GET(self):
		obje2=[]
		veri={'name':'','y':''}
		count=json.load(open("tweetcount.json"))
		for i in count:
			veri={'name':i['isim'].encode('utf8'),'y':int(i['count'])}
			obje2.append(veri)
		print json.dumps(obje2)
		return json.dumps(obje2)
###############################################################################


class chart2_query:
	
	
	def GET(self):
		data=[]
		data=review()
		print json.dumps(data)
		return json.dumps(data)

###############################################################################


class find_titles:
    def GET(self):
       time.sleep(1.5);
       inp = web.input()
       title = inp.get("title")
       veri=[{'dizi isim':'','derece':''}]
       veri=ratingseason(title)
       print veri
       return  json.dumps(veri)   
       
###############################################################################

class index:
    def GET(self):
       return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("127.0.0.1", 1238))


###########################################TOP OF SEASON######################################################

rate=json.load(open("episode2.json"))
def rate_calculate(isim):                              
        arr = []
	result = 0.0
	for i in rate:
		if i['dizi isim']==isim:
		   
		   arr.append(i['rate'])
		   result=result + float(i['rate'])

	derece = result / len(arr)
	return derece

   
 
x=[]
def chooseseries(dizi):  
    
    y=[]                                   
    for i in x:
	   if re.match(r"^%s.*"%dizi,i):                
		  y.append(i)
    return y


def ratingseason(dizi):
    
    sonuc=[]
    sonucjson={'dizi isim':'','derece':''}
    #rate =json.load(open("episode2.json"))
    #rate = sorted(rate1, key=lambda k: k['oylama'], reverse=True)
    for i in rate:	   
		x.append(i["dizi isim"])
    liste1=[]
    liste1=chooseseries(dizi)
    liste1 =list(set(liste1))
    for i in liste1:
		sonucjson={'name':i,'derece':float(rate_calculate(i))}
		sonuc.append(sonucjson)
		
    return sonuc
#print ratingseason('Arrow')

#####################################################################


##########################################ELESTİRİ SAYISI##################################################

elestiri=[]



def review():
	obje=[]
	elestiri=json.load(open("anasayfa2.json"))
	data2={'isim':'','elestiri':''}
	for i in elestiri:
		data={'name':i["isim"].encode('utf8'), 'y':float(i["elestiri"])}
		obje.append(data)
	return obje
print review()

#################################################################################################################################
def extract_time(rate):
    try:        
        return float(rate["rate"])
    except KeyError:
        return 0


	



