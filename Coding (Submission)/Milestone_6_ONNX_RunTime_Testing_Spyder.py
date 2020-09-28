# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:55:59 2020

@author: KevinChng
"""

import numpy as np    # we're going to use numpy to process input and output data
import onnxruntime    # to inference ONNX models, we use the ONNX Runtime
from onnx import numpy_helper
import urllib.request

import time
import cv2

# display images in notebook
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

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

#print('Input Name:', input_name)

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
    

# Read image 2701
img = cv2.imread('2701_Extracted_SG_To_JB\Jan_2701_01T00_00_00.png.png')
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
img1 = cv2.imread('2702_Categories\Car_Traffic_No_Jam\Jan_2702_01T00_00_00.png.png')
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
start = time.time()
raw_result1 = session1.run([], {input_name1: input_data1})
raw_result2 = session2.run([], {input_name2: input_data2})
raw_result3 = session3.run([], {input_name3: input_data3})
raw_result4 = session4.run([], {input_name4: input_data4})
raw_result5 = session5.run([], {input_name5: input_data5})
raw_result6 = session6.run([], {input_name6: input_data6})
raw_result7 = session7.run([], {input_name7: input_data7})
raw_result8 = session8.run([], {input_name8: input_data8})
end = time.time()

Traffic_scale_2701 = round((3*raw_result1[0][0][1] + 2*raw_result2[0][0][1] + raw_result3[0][0][1] + raw_result4[0][0][1])/7*4)
Traffic_scale_2702 = round(raw_result5[0][0][1] + raw_result6[0][0][1] + raw_result7[0][0][1] + raw_result8[0][0][1])
Traffic_scale = (Traffic_scale_2701 + Traffic_scale_2702)/2


