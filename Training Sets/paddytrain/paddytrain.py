from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config =ConfigProto()
config.gpu_options.allow_growth =True
session = InteractiveSession(config=config)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import matplotlib.pyplot as plt
import numpy as np 
import os

#basic cnn
# Initialising the CNN
classifier = Sequential()

# step1 - Convolution
classifier.add(Conv2D(32, (3,3), input_shape = (128, 128 ,3),activation = 'relu'))

#step2 - pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))


#adding a second convolutional layer
classifier.add(Conv2D(32, (3,3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))

# STEP 3- flattening
classifier.add(Flatten())

#step4- fullconnection
classifier.add(Dense(units = 128, activation ='relu'))
classifier.add(Dense(units = 4, activation ='sigmoid'))

#compiling the cnn
classifier.compile (optimizer = 'adam', loss ='categorical_crossentropy', metrics = ['accuracy'])


train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range =0.2, horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('E:\\paddy-leaf-quality-detection\\Dataset\\train', #realtivepath from working directory
                                                target_size = (128,128),
                                                batch_size = 6,class_mode ='categorical')
vaild_set = test_datagen.flow_from_directory('E:\\paddy-leaf-quality-detection\\Dataset\\valid', #realtivepath from working directory
                                                target_size = (128,128),
                                                batch_size = 6,class_mode ='categorical')                                                
            
labels =(training_set.class_indices)
print(labels)


classifier.fit_generator(training_set,
               steps_per_epoch = 20,
               epochs = 50,
               validation_data=vaild_set            
               )

classifier_json=classifier.to_json()
with open("paddy.json", "w") as json_file:
    json_file.write(classifier_json)
#serialize weights to HDFS
    classifier.save_weights("paddy_model_weights.h5")
    classifier.save("paddy.h5")
    print("saved model to disk")



               