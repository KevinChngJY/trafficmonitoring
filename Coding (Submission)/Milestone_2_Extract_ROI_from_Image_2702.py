# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:36:16 2020

@author: KevinChng
"""

""

from PIL import Image, ImageDraw
import json
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import os
#from glob import glob
#import cv2 as cv

# Camera 2702
os.chdir(r'C:\Users\KevinChng\Desktop\NUS Project\2702')
with open("Hi.json") as json_file:
    data = json.load(json_file)
ROI1_del = data["shapes"][0]["points"]
ROI2_del = data["shapes"][1]["points"]
#ROI3_del = data["shapes"][2]["points"]
#ROI4_del = data["shapes"][3]["points"]
polygon_ROI1 = [tuple(k) for k in ROI1_del]
polygon_ROI2 = [tuple(k) for k in ROI2_del]
#polygon_ROI3 = [tuple(k) for k in ROI3_del]
#polygon_ROI4 = [tuple(k) for k in ROI4_del]
width = data["imageWidth"]
height = data["imageHeight"]
filelist=os.listdir(r'C:\Users\KevinChng\Desktop\NUS Project\2702')
for fichier in filelist[:]:
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
error=None;
error =[];
for name in filelist:
    try:
        os.chdir(r'C:\Users\KevinChng\Desktop\NUS Project\2702')
        img = Image.open(name)
        #img = cv.imread(name)
        ImageDraw.Draw(img).polygon(polygon_ROI1, outline=1, fill=(255,255,255))
        ImageDraw.Draw(img).polygon(polygon_ROI2, outline=1, fill=(255,255,255))
        #ImageDraw.Draw(img).polygon(polygon_ROI3, outline=1, fill=(255,255,255))
        #ImageDraw.Draw(img).polygon(polygon_ROI4, outline=1, fill=(255,255,255))
        #plt.imshow(img)
        os.chdir(r'C:\Users\KevinChng\Desktop\NUS Project\2702_Extracted')
        img.save("{}.png".format(name))
    except:
        error.append(["Image 2702: Error at {}".format(name)])
