# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:03:43 2020

@author: KevinChng
"""

import urllib3
import json
import os
import requests, shutil

error=None;
error =[];

for day in range(21,32):
    for hour in range(0,24):
        for minutes in range(0,60,15):
            http = urllib3.PoolManager()
            string_link = 'https://api.data.gov.sg/v1/transport/traffic-images?date_time=2020-01-{:02d}T{:02d}:{:02d}:00'.format(day,hour,minutes)
            r = http.request('GET', string_link)
            ws = json.loads(r.data.decode('utf-8'))
            k = ws["items"][0]['cameras']
            try:
                image6 = k[[i for i in range(0,len(k)) if k[i]['camera_id']=="2701"][0]]['image']
                os.chdir(r'C:\Users\KevinChng\Desktop\NUS Project\2701')
                r = requests.get(image6,stream=True)
                if r.status_code == 200:
                    photo_name = 'Jan_2701_{:02d}T{:02d}_{:02d}_00.png'.format(day,hour,minutes)
                    with open(photo_name,'wb') as f:
                        r.raw.decide_content = True
                        shutil.copyfileobj(r.raw, f)
            except:
                error.append(["Image 2701: Error at {}".format(string_link)])
            try:
                image7 = k[[i for i in range(0,len(k)) if k[i]['camera_id']=="2702"][0]]['image']
                os.chdir(r'C:\Users\KevinChng\Desktop\NUS Project\2702')
                r = requests.get(image7,stream=True)
                if r.status_code == 200:
                    photo_name = 'Jan_2702_{:02d}T{:02d}_{:02d}_00.png'.format(day,hour,minutes)
                    with open(photo_name,'wb') as f:
                        r.raw.decide_content = True
                        shutil.copyfileobj(r.raw, f)
            except:
                 error.append(["Image 2702: Error at {}".format(string_link)])
