#importing warnings and filtering them
import sys
import warnings
warnings.filterwarnings('ignore')

#importing of all the needed libraries
#importing models from tensorflow, and keras libraries
from tensorflow import keras
from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.models import load_model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from glob import glob
import keras.utils as image
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#setting up an image size that will be used
IMAGE_SIZE = [224, 224]

#training and validation path files
train_path = 'Datasets/train'
valid_path = 'Datasets/test'

vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

for layer in vgg.layers: layer.trainable = False

folders = glob('Datasets/train/*')
x = Flatten()(vgg.output)

#setting up the dense layer and activation function for the network
#activation referes to activation function can be changed to be further optimization of model
#possible activation functions;
######  SoftMax, relu, sigmoid, and many more available in python library
## Location of differnet activation functions your library has C:\Users\matts\AppData\Local\Programs\Python\Python310\Lib\site-packages\keras\layers\activation
prediction = Dense(len(folders), activation='softmax')(x)
#creating a object named model
model = Model(inputs=vgg.input, outputs=prediction)
#model structure is summarized
model.summary()

#compiling the model using crossentropy and optimizing model using adam
#metric are defined as accuracy of network out of 1 if 1 model is 100% accurate
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)

#Make sure you provide the same target size as initialied for the image size
training_set = train_datagen.flow_from_directory('Datasets/train', target_size = (224, 224), batch_size = 10, class_mode = 'categorical')
test_set = test_datagen.flow_from_directory('Datasets/test', target_size = (224, 224), batch_size = 10, class_mode = 'categorical')

r = model.fit_generator(training_set, validation_data=test_set, epochs=1, steps_per_epoch=len(training_set), validation_steps=len(test_set))

#saving model
model.save('patient_xrays.h5')
#loading model
model=load_model('patient_xrays.h5')

#loading the image from files can be changed for testing different files
#img=image.load_img('Sample_Xray.jpg',target_size=(224,224))
img=image.load_img(sys.argv[1],target_size=(224,224))

x=image.img_to_array(img)

x=np.expand_dims(x, axis=0)

img_data=preprocess_input(x)

classes=model.predict(img_data)

result=int(classes[0][0])

#prints out if patient has pneumonia or if patient is healthy based on the trained model provided
if result==0: print("Patient has PNEUMONIA")
else: print("Patient is Healthy")
