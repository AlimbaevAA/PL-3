import time
import requests
import re

file=open('index.html', 'w')
file.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Party People</title><style>span{font-size: 1.3em;font-weight: bold;color: #9A078A;}li{list-style: none;}ul{padding-left: 0;}li.f{border: 1px solid #167F0E; border-radius: 13px; padding: 15px; margin-bottom: 20px;}li.inf{border: 4px inset #1C25D8; border-radius: 7px; margin: 15px;padding: 15px;}</style></head><body><h1 style="color: #CC0D0D;text-align: center;">New York</h1><ul>')
r=requests.get('https://api.meetup.com/2/concierge?key=1c646d532d2e10563c5507c1f4e60f&sign=true&photo-host=public&country=us&city=New York&category_id=34&state=NY')
info=re.findall(r'"name":"([\w\ \(\)\:]+)","id":"[\w ]+","time":([\d]+)', r.text)
adress=re.findall(r'"address_1":"([\w\ \.\&]+)"', r.text)
for d in range(7):
	file.write('<li class="f"><ul><u>'+str(d)+'-'+str(d+1)+' day</u>')
	for j in range(len(info)):
		if (int(info[j][1])<((d+1)*86400000+time.time()*1000)) and (int(info[j][1])>(d*86400000+time.time()*1000)):
			file.write('<li class="inf">' '<span>Date:  </span>'+ str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(float(info[j][1])/1000))) + '&emsp;||' + '&emsp;<span>Event:  </span>' + str(info[j][0]) + '&emsp;||' + '&emsp;<span>Location:  </span>' + str(adress[j]) + '</li>')
	file.write('</ul></li>')
file.write('</ul></body></html>')