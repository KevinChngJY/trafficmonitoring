# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:06:46 2020

@author: KevinChng
"""

from flask import Flask, render_template
import urllib3
import json
import os
import requests, shutil
import onnxruntime 
import time
import cv2
from PIL import Image, ImageDraw
import numpy as np 
from datetime import datetime
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response

@app.route("/")
def home():
    owd = os.getcwd()
    datetime_object = streamLTA()
    preprocess3(owd)
    preprocess4(owd)
    combineTwoImages(owd)
    Traffic_scale_2701, Traffic_scale_2702, Traffic_scale, Duration = detection(owd)
    Duration = round(Duration, 2)
    os.chdir(owd)
    return render_template("index.html",value=Duration, updatedate = datetime_object,traffic_one=Traffic_scale_2701,traffic_two=Traffic_scale_2702,traffic=Traffic_scale)

def streamLTA():    
    http = urllib3.PoolManager()
    #string_link = 'https://api.data.gov.sg/v1/transport/traffic-images?date_time=2020-01-01T15:30:00'
    #live
    string_link = 'https://api.data.gov.sg/v1/transport/traffic-images?'
    r = http.request('GET', string_link)
    ws = json.loads(r.data.decode('utf-8'))
    error=None;
    error =[];

    k = ws["items"][0]['cameras']
    updatedate = ws['items'][0]['timestamp'];
    datetime_object = datetime.strptime(updatedate[0:19], '%Y-%m-%dT%H:%M:%S')
    datetime_object.strftime("%d-%b-%Y %H:%M:%S")
    try:
          image6 = k[[i for i in range(0,len(k)) if k[i]['camera_id']=="2701"][0]]['image']
          os.chdir(r'static\img')
          r = requests.get(image6,stream=True)
          if r.status_code == 200:
              photo_name = '2701.png'
              with open(photo_name,'wb') as f:
                  r.raw.decide_content = True
                  shutil.copyfileobj(r.raw, f)
    except:
        error.append(["Image 2701: Error at {}".format(string_link)])
    try:
        image7 = k[[i for i in range(0,len(k)) if k[i]['camera_id']=="2702"][0]]['image']
        #os.chdir(r'static\img')
        r = requests.get(image7,stream=True)
        if r.status_code == 200:
            photo_name = '2702.png'
            with open(photo_name,'wb') as f:
                r.raw.decide_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        error.append(["Image 2702: Error at {}".format(string_link)])
    return datetime_object
        
def combineTwoImages(owd):
    os.chdir(owd)
    os.chdir(r'static\img')
    images = [Image.open(x) for x in ['2701.png', '2702.png']]
    images[0] = images[0].resize((220*7,180*7))   # image resizing
    images[1] = images[1].resize((220*7,180*7))
    get_concat_h(images[0], images[1]).save('Combine.jpg')
    
def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def detection(owd):
    os.chdir(owd)
    os.chdir("..")
    start = time.time()
    # Run the model on the backend
    session1 = onnxruntime.InferenceSession('network1.onnx', None)
    session2 = onnxruntime.InferenceSession('network2.onnx', None)
    session3 = onnxruntime.InferenceSession('network3.onnx', None)
    session4 = onnxruntime.InferenceSession('network4.onnx', None)
    session5 = onnxruntime.InferenceSession('network5.onnx', None)
    session6 = onnxruntime.InferenceSession('network6.onnx', None)
    session7 = onnxruntime.InferenceSession('network7.onnx', None)
    session8 = onnxruntime.InferenceSession('network8.onnx', None)
    
    # get the name of the first input of the model
    input_name1 = session1.get_inputs()[0].name
    input_name2 = session2.get_inputs()[0].name 
    input_name3 = session3.get_inputs()[0].name 
    input_name4 = session4.get_inputs()[0].name 
    input_name5 = session5.get_inputs()[0].name 
    input_name6 = session6.get_inputs()[0].name 
    input_name7 = session7.get_inputs()[0].name 
    input_name8 = session8.get_inputs()[0].name

    os.chdir(r'Milestone 7 Flask\static\img')
    # Read image 2701
    img = cv2.imread('2701.png.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_2701_1 = img[60:60+137,480:480+155]
    img_2701_2 = img[114:114+181,320:320+160]
    img_2701_3 = img[186:186+181,160:160+320]
    img_2701_4 = img[267:267+140,2:2+160]
    image_data1 = preprocess2(img_2701_1)
    image_data2 = preprocess2(img_2701_2)
    image_data3 = preprocess2(img_2701_3)
    image_data4 = preprocess2(img_2701_4)
    input_data1 = preprocess(image_data1)
    input_data2 = preprocess(image_data2)
    input_data3 = preprocess(image_data3)
    input_data4 = preprocess(image_data4)
    #display_image = plt.imshow(img)
    
    # Read image 2702
    img1 = cv2.imread('2702.png.png')
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img_2702_1 = img1[363:363+118,433:433+208]
    img_2702_2 = img1[264:264+100,313:313+194]
    img_2702_3 = img1[162:162+78,188:188+128]
    img_2702_4 = img1[2:2+118,100:100+94]
    image_data5 = preprocess2(img_2702_1)
    image_data6 = preprocess2(img_2702_2)
    image_data7 = preprocess2(img_2702_3)
    image_data8 = preprocess2(img_2702_4)
    input_data5 = preprocess(image_data5)
    input_data6 = preprocess(image_data6)
    input_data7 = preprocess(image_data7)
    input_data8 = preprocess(image_data8)
    #display_image1 = plt.imshow(img1)
    
    # Prediction
    raw_result1 = session1.run([], {input_name1: input_data1})
    raw_result2 = session2.run([], {input_name2: input_data2})
    raw_result3 = session3.run([], {input_name3: input_data3})
    raw_result4 = session4.run([], {input_name4: input_data4})
    raw_result5 = session5.run([], {input_name5: input_data5})
    raw_result6 = session6.run([], {input_name6: input_data6})
    raw_result7 = session7.run([], {input_name7: input_data7})
    raw_result8 = session8.run([], {input_name8: input_data8})
    
    Traffic_scale_2701 = round((3*raw_result1[0][0][1] + 2*raw_result2[0][0][1] + raw_result3[0][0][1] + raw_result4[0][0][1])/7*4)
    Traffic_scale_2702 = round(raw_result5[0][0][1] + raw_result6[0][0][1] + raw_result7[0][0][1] + raw_result8[0][0][1])
    Traffic_scale = (Traffic_scale_2701 + Traffic_scale_2702)/2
    
    end = time.time()
    
    Duration = end - start;
    return Traffic_scale_2701, Traffic_scale_2702, Traffic_scale, Duration
    
def preprocess(input_data):
    # convert the input data into the float32 input
    img_data = input_data.astype('float32')

    #normalize
    #mean_vec = np.array([0.485, 0.456, 0.406])
    #stddev_vec = np.array([0.229, 0.224, 0.225])
    #norm_img_data = np.zeros(img_data.shape).astype('float32')
    #for i in range(img_data.shape[0]):
    #    norm_img_data[i,:,:] = (img_data[i,:,:]/255 - mean_vec[i]) / stddev_vec[i]
        
    #add batch channel
    norm_img_data = img_data.reshape(1, 3, 227, 227).astype('float32')
    return norm_img_data

def preprocess2(input_data):
    img = cv2.resize(input_data,(227,227))
    rgbArray = np.zeros((227,227,3), 'uint8')
    rgbArray[..., 0] = img[:,:,0]
    rgbArray[..., 1] = img[:,:,1]
    rgbArray[..., 2] = img[:,:,2]
    #img2 = Image.fromarray(rgbArray)
    image_data = np.array(img).transpose(2, 0, 1)
    return image_data

def preprocess3(owd):
    # Camera 2701
    os.chdir(owd)
    os.chdir('..')
    with open("2701_coordinate.json") as json_file:
        data = json.load(json_file)
    ROI1_del = data["shapes"][0]["points"]
    ROI2_del = data["shapes"][1]["points"]
    polygon_ROI1 = [tuple(k) for k in ROI1_del]
    polygon_ROI2 = [tuple(k) for k in ROI2_del]
    os.chdir(r'Milestone 7 Flask\static\img')
    img = Image.open("2701.png")
    ImageDraw.Draw(img).polygon(polygon_ROI1, outline=1, fill=(255,255,255))
    ImageDraw.Draw(img).polygon(polygon_ROI2, outline=1, fill=(255,255,255))
    img.save("2701.png.png")
    
def preprocess4(owd):
    # Camera 2702
    os.chdir(owd)
    os.chdir('..')
    with open("2702_coordinate.json") as json_file:
        data = json.load(json_file)
        ROI1_del = data["shapes"][0]["points"]
        ROI2_del = data["shapes"][1]["points"]
        ROI3_del = data["shapes"][2]["points"]
        ROI4_del = data["shapes"][3]["points"]
        polygon_ROI1 = [tuple(k) for k in ROI1_del]
        polygon_ROI2 = [tuple(k) for k in ROI2_del]
        polygon_ROI3 = [tuple(k) for k in ROI3_del]
        polygon_ROI4 = [tuple(k) for k in ROI4_del]
        os.chdir(r'Milestone 7 Flask\static\img')
        img = Image.open("2702.png")
        ImageDraw.Draw(img).polygon(polygon_ROI1, outline=1, fill=(255,255,255))
        ImageDraw.Draw(img).polygon(polygon_ROI2, outline=1, fill=(255,255,255))
        ImageDraw.Draw(img).polygon(polygon_ROI3, outline=1, fill=(255,255,255))
        ImageDraw.Draw(img).polygon(polygon_ROI4, outline=1, fill=(255,255,255))
        img.save("2702.png.png")

if __name__ == "__main__":
    app.run(debug=True)