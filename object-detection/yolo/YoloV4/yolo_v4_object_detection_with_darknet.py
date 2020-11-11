# -*- coding: utf-8 -*-
"""YOLO_v4_Object_Detection_with_Darknet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cTly0pMbtAoSndzHPbHZ7ppYlg-Ygw10

## YOLO v4

<br>
<hr>

#### 1 - Download do Darknet
"""

!git clone https://github.com/AlexeyAB/darknet

ls

cd darknet

ls

"""<hr>
<br>

#### 2 - Compile library
"""

!make

"""<hr>
<br>

#### 3 - Download weights of pre-trained model 

<br>
"""

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

"""<hr>
<br>

#### 4 - Testing Detector
"""

ls

!./darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg

"""<hr>
<br>

#### 5 - Show results
"""

import cv2
import matplotlib.pyplot as plt
def mostrar(caminho):
  imagem = cv2.imread(caminho)
  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis('off')
  plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
  plt.show()

mostrar('predictions.jpg')

"""<hr>
<br>

####  YOLO v4 with support GPU / CUDA
"""

import tensorflow as tf
device_name = tf.test.gpu_device_name()
print(device_name)

rm -rf ./obj/image_opencv.o ./obj/http_stream.o ./obj/gemm.o ./obj/utils.o ./obj/dark_cuda.o ./obj/convolutional_layer.o ./obj/list.o ./obj/image.o ./obj/activations.o ./obj/im2col.o ./obj/col2im.o ./obj/blas.o ./obj/crop_layer.o ./obj/dropout_layer.o ./obj/maxpool_layer.o ./obj/softmax_layer.o ./obj/data.o ./obj/matrix.o ./obj/network.o ./obj/connected_layer.o ./obj/cost_layer.o ./obj/parser.o ./obj/option_list.o ./obj/darknet.o ./obj/detection_layer.o ./obj/captcha.o ./obj/route_layer.o ./obj/writing.o ./obj/box.o ./obj/nightmare.o ./obj/normalization_layer.o ./obj/avgpool_layer.o ./obj/coco.o ./obj/dice.o ./obj/yolo.o ./obj/detector.o ./obj/layer.o ./obj/compare.o ./obj/classifier.o ./obj/local_layer.o ./obj/swag.o ./obj/shortcut_layer.o ./obj/activation_layer.o ./obj/rnn_layer.o ./obj/gru_layer.o ./obj/rnn.o ./obj/rnn_vid.o ./obj/crnn_layer.o ./obj/demo.o ./obj/tag.o ./obj/cifar.o ./obj/go.o ./obj/batchnorm_layer.o ./obj/art.o ./obj/region_layer.o ./obj/reorg_layer.o ./obj/reorg_old_layer.o ./obj/super.o ./obj/voxel.o ./obj/tree.o ./obj/yolo_layer.o ./obj/gaussian_yolo_layer.o ./obj/upsample_layer.o ./obj/lstm_layer.o ./obj/conv_lstm_layer.o ./obj/scale_channels_layer.o ./obj/sam_layer.o darknet

"""<hr>
<br>

#### Modifying Makefile for GPU
"""

!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile

!cat Makefile

"""<hr>
<br>

#### Recompile Library
"""

!make

"""<hr>
<br>

#### Re-testing Detector
"""

!./darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg

mostrar('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/giraffe.jpg

mostrar('predictions.jpg')

!nvidia-smi

!/usr/local/cuda/bin/nvcc --version

import os
def detectar(imagem):
  os.system("cd /content/darknet && ./darknet detect cfg/yolov4.cfg yolov4.weights {}".format(imagem))
  mostrar('predictions.jpg')

detectar('data/person.jpg')

imagens = ['data/horses.jpg', 'data/eagle.jpg']
for img in imagens:
  detectar(img)

!cat data/coco.names

"""<hr>
<br>

#### Conecting with Google Drive
"""

from google.colab import drive
drive.mount('/content/gdrive')

!ls /content/gdrive/My\ Drive/Cursos\ -\ recursos/YOLO/imagens

ls

!cp /content/gdrive/My\ Drive/Cursos\ -\ recursos/YOLO/imagens/cachorros02.jpg data/

detectar('data/cachorros02.jpg')

"""<hr>
<br>

#### Salving predictions
"""

!cp predictions.jpg /content/gdrive/My\ Drive/Cursos\ -\ recursos/YOLO/imagens/resultado.jpg

"""<hr>
<br>

#### Storage files of model
"""

# cd /content/darknet
ls

ls cfg

!zip -r modelo_YOLOv4.zip yolov4.weights cfg/yolov4.cfg cfg/coco.names

ls

"""<hr>
<br>


#### Compact files
"""

!cp modelo_YOLOv4.zip /content/gdrive/My\ Drive/Cursos\ -\ recursos/YOLO/modelo_YOLOv4.zip

"""<hr>
<br>


#### Descompact files
"""

ls

!cp /content/gdrive/My\ Drive/Cursos\ -\ recursos/YOLO/modelo_YOLOv4.zip ./

!unzip modelo_YOLOv4.zip

"""<hr>
<br>

#### Define Threshold
"""

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg

mostrar('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -thresh 0.9

mostrar('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -thresh 0.98

mostrar('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -thresh 0.00001

mostrar('predictions.jpg')

"""<hr>
<br>

#### ext_output 

This hyperparameter show Bounding boxes measures (anchors)
"""

!./darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg -ext_output

"""<br>
<hr>
<br>
<hr>
<br>
"""