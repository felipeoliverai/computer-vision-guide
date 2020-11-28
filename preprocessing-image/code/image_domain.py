### Image Domain 


import cv2 
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
%matplotlib inline

# reading images in RGB and Gray scale 

# RGB 
image_1 = cv2.imread('/content/drive/MyDrive/Deep Learning - Projetos/computer-vision-guide/images /mountain.jpg')
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)

# Gray scale 
image_2 = cv2.imread('/content/drive/MyDrive/Deep Learning - Projetos/computer-vision-guide/images /mountain.jpg', cv2.IMREAD_GRAYSCALE)


# show images 
fig, axes = plt.subplots(1,2, figsize=(12,6))
ax = axes.ravel()
ax[0].imshow(image_1)
ax[0].set_title('Mountain RGB')
ax[1].imshow(image_2, cmap='gray')
ax[1].set_title('Mountain Gray Scale')
plt.subplots_adjust(wspace=0.6)
plt.show()

"""<hr>
<br>

#### Diff Absolute 

img_1 = cv2.imread('/content/drive/MyDrive/Deep Learning - Projetos/computer-vision-guide/images /room-1.jpeg', cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread('/content/drive/MyDrive/Deep Learning - Projetos/computer-vision-guide/images /room-2.jpeg', cv2.IMREAD_GRAYSCALE)


fig, axes = plt.subplots(1,2, figsize=(12,6))
ax = axes.ravel()
ax[0].imshow(img_1, cmap='gray')
ax[1].imshow(img_2, cmap='gray')
plt.subplots_adjust(wspace=0.6)
plt.show()

# diff absolute (image modifity ----- reference image)
# positive values 

img_diff = cv2.absdiff(img_2, img_1)
plt.figure(figsize=(10,6))
plt.imshow(img_diff, 'gray')
plt.show()



#### Image threshold pixels 

# Thresholds in OpenCV

modes = ['cv2.THRESH_BINARY',
         'cv2.THRESH_BINARY_INV',
         'cv2.THRESH_TRUNC',
         'cv2.THRESH_TOZERO',
         'cv2.THRESH_TOZERO_INV']


def threshold(image, thresh, mode):
  global dst
  mode = eval(mode)
  th, dst = cv2.threshold(image, thresh, 255, mode)
  plt.figure(figsize=(10,5))
  plt.imshow(dst, cmap='gray')
  plt.show()


threshold(image=image_2, thresh=213, mode='cv2.THRESH_BINARY')

threshold(image=image_1, thresh=140, mode='cv2.THRESH_TRUNC')

threshold(image=img_2, thresh=215, mode='cv2.THRESH_BINARY')


#### Masked 

"""
applying masked top on original image
"""

# Masked 

masked = cv2.multiply(img_1, (dst//255))
plt.figure(figsize=(10,5))
plt.imshow(masked, cmap='gray')
plt.title('Image masked', fontsize=13) 
plt.show()
