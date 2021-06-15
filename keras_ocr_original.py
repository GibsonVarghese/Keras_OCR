# -*- coding: utf-8 -*-
"""Keras-OCR_original.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtwhb1iv1BYggirqgyBMXNAP_JkiZefJ
"""



pip install git+https://github.com/faustomorales/keras-ocr.git#egg=keras-ocr

pip install keras-ocr

import matplotlib.pyplot as plt

import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()

images = [
    keras_ocr.tools.read(url) for url in ['https://res.sastasundar.com/incom/images/product/Eltroxin-1566553124-10000287-1.jpg',
                                          'https://res.cloudinary.com/du8msdgbj/image/upload/l_watermark_346,w_480,h_480/a_ignore,w_480,h_480,c_fit,q_auto,f_auto/v1537711328/p2avby02m4amgue3aj0m.jpg',
                                          'https://5.imimg.com/data5/JV/MN/JW/SELLER-51283965/pedark-4-500x500.jpeg',
                                          'https://post.healthline.com/wp-content/uploads/sites/3/2020/02/323304_2200-800x1200.jpg']]

len(images)

plt.figure(figsize=(10,20))
plt.imshow(images[2])



plt.figure(figsize=(10,20))
plt.imshow(images[3])

prediction_groups = pipeline.recognize(images)

fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for ax,image,predictions in zip(axs,images,prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)

prediction_groups

prediction_groups[0]

import pandas as pd

# upload a brand name file
from google.colab import files
uploaded = files.upload()

import io
data =pd.read_csv(io.BytesIO(uploaded['brand.csv']))

type(data)

type(prediction_groups)

prediction_groups[0][2]

import re
result =re.sub("[^a-zA-Z]"," ",str(prediction_groups))

result

db =result.split()
print(db)



prediction_groups
ele ='man'
flag=0

for i in db:
  if(i==ele):
    print("Brand name :", i)
    flag=1
    break
if(flag==0):
  print("Brand not found")