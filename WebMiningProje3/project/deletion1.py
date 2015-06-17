#!/usr/bin/python

import json
import re
obj=json.load(open("episode1.json"))

print len(obj)


y=[]
data={'dizi isim':'','isim':'','episode':'','rate':'','description':''}
def deletion():                                     # kullanicidan aldigimiz dizinin sezonlarini bulurr.
	for i in obj:
	   if (re.match(r"^Coronation Street .*",i['dizi isim'])):
			pass
	#inputtaki dizi ile baslayan sezonlari bul             
	   else:
		  data={'dizi isim':i['dizi isim'],'isim':i['isim'],'episode':i['episode'],'rate':i['rate'],'description':i['description']}
		  y.append(data)
	return y

#print deletion()			
listem=deletion()
with open('episode2.json','w') as outfile :
    json.dump(listem,outfile)




