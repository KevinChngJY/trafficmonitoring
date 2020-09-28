# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:14:09 2020

@author: KevinChng
"""

import urllib3
from bs4 import BeautifulSoup
import json
import gmplot 

http = urllib3.PoolManager()
r = http.request('GET', 'https://api.data.gov.sg/v1/transport/traffic-images?date_time=2020-02-03T01:01:01')
#r = requests.get(url = "https://api.data.gov.sg/v1/transport/traffic-images?date_time=2020-02-03T01:01:01")
ws = json.loads(r.data.decode('utf-8'))
k = ws["items"][0]['cameras']
latitude_list = list();
longitude_list = list();
for i in range (len(k)):
    latitude_list.append(ws["items"][0]['cameras'][i]["location"]["latitude"])
    longitude_list.append(ws["items"][0]['cameras'][i]["location"]["longitude"])
print(len(k))

gmap1 = gmplot.GoogleMapPlotter(1.2902705,103.851959,11)
gmap1.scatter( latitude_list,longitude_list, '# FF0000', size =40 , marker = False)
gmap1.draw("12.html")