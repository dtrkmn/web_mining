#!/usr/bin/ python
import json
import re



# -*- coding: utf-8

with open("tweetler.json") as json_file:
    json_data = json.load(json_file)
	
print len(json_data)
got=0
vikings=0
tvd=0
arrow=0
natural=0
ga=0
ouat=0
tb=0
th=0
ncis=0
castle=0
tgw=0
revenge=0
himyf=0
tbbt=0
cm=0
bone=0
maos=0
for i in json_data:
	
	if re.match('.*Game of Thrones.*',i['tweet']):
		got=got+1
	if re.match('.*Vikings.*',i['tweet']):
		vikings=vikings+1
	if re.match('.*Vampire Diaries.*',i['tweet']):
		tvd=tvd+1
	if re.match('.*Arrow.*',i['tweet']):
		arrow=arrow+1
	if re.match('.*Grey''s Anatomy.*',i['tweet']):
		ga=ga+1
	if re.match('.*Supernatural.*',i['tweet']):
		natural=natural+1
	if re.match('.*Once upon a time.*',i['tweet']):
		ouat=ouat+1
	if re.match('.*The Blacklist.*',i['tweet']):
		tb=tb+1
	if re.match('.*The 100.*',i['tweet']):
		th=th+1
	if re.match('.*Castle.*',i['tweet']):
		castle=castle+1
	if re.match('.*NCIS.*',i['tweet']):
		ncis=ncis+1
	if re.match('.*The Good Wife.*',i['tweet']):
		tgw=tgw+1
	if re.match('.*Revenge.*',i['tweet']):
		revenge=revenge+1
	if re.match('.*How I met your mother.*',i['tweet']):
		himyf=himyf+1
	if re.match('.*Marvel Agent''s of SHIELD.*',i['tweet']):
		maos=maos+1
	if re.match('.*the Big Bang Theory.*',i['tweet']):
		tbbt=tbbt+1
	if re.match('.*Criminal Minds.*',i['tweet']):
		cm=cm+1
	if re.match('.*Bones.*',i['tweet']):
		bone=bone+1
veri=[]
gameofthrones={'isim':'Game of Thrones','count':got}
veri.append(gameofthrones)
Vikings={'isim':'Vikings','count':vikings}
veri.append(Vikings)
vampirediaries={'isim':'Vampire Diaries','count':tvd}
veri.append(vampirediaries)
criminalminds={'isim':'Criminal Minds','count':cm}
veri.append(criminalminds)
bones={'isim':'Bones','count':bone}
veri.append(bones)
Arrow={'isim':'Arrow','count':arrow}
veri.append(Arrow)
bigbang={'isim':'the Big Bang Theory','count':tbbt}
veri.append(bigbang)
Marvel={'isim':'Marvel Agent''s of SHIELD','count':maos}
veri.append(Marvel)
mother={'isim':'How I met your mother','count':himyf}
veri.append(mother)
Revenge={'isim':'Revenge','count':revenge}
veri.append(Revenge)
wife={'isim':'The Good Wife','count':tgw}
veri.append(wife)
NCIS={'isim':'NCIS','count':ncis}
veri.append(NCIS)
hundred={'isim':'The 100','count':th}
veri.append(hundred)
blacklist={'isim':'The Blacklist','count':tb}
veri.append(blacklist)
onceupon={'isim':'Once upon a time','count':ouat}
veri.append(onceupon)
supernatural={'isim':'Supernatural','count':natural}
veri.append(supernatural)
Grey={'isim':'Grey''s Anatomy','count':ga}
veri.append(Grey)
Castle={'isim':'Castle','count':castle}
veri.append(Castle)

with open('tweetcount.json', 'w') as outfile:
   
    json.dump(veri, outfile)