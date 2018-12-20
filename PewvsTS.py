import json
import requests
import time
#import curses
print("PewDiePie vs T-Series\n_________________________")
key=""
s=time.time()
while time.time()<s+20:
	r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC-lHJZR3Gqxm24_Vd_AJ5Yw&key="+key)
	data = json.loads(r.text)
	pdp=int((((data['items'])[0])['statistics'])['subscriberCount'])
	r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCq-Fj5jknLsUf-MWSy4_brA&key="+key)
	data = json.loads(r.text)
	ts=int((((data['items'])[0])['statistics'])['subscriberCount'])
	print ("PewDiePie :"+str(pdp))
	print ("T-Series  :"+str(ts))
	if ts>pdp:
		lead=ts-pdp;
	else:
		lead=pdp-ts
	if ts>pdp:
		print("T-series",end='')
	else:
		print("PewDiePie",end='')
	print(" leads by",lead)
	time.sleep(1)
	print("\033[F\033[F\033[F\033[F")
print("\n\n")
