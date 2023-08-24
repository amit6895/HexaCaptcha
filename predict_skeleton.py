

# DO NOT CHANGE THE NAME OF THIS METHOD OR ITS INPUT OUTPUT BEHAVIOR

# INPUT CONVENTION
# filenames: a list of strings containing filenames of images

# OUTPUT CONVENTION
# The method must return a list of strings. Make sure each string is either "ODD"
# or "EVEN" (without the quotes) depending on whether the hexadecimal number in
# the image is odd or even. Take care not to make spelling or case mistakes. Make
# sure that the length of the list returned as output is the same as the number of
# filenames that were given as input. The judge may give unexpected results if this
# convention is not followed.
import tensorflow as tf 
import os
import cv2
import numpy as np

def load_images(filenames):
  #directory = 'assn2/train'
  num= len(filenames) 
  #print(num)
  # List to store the loaded images
  images = []

  # Iterate over the files in the directory
  for i in range(num):
    #filename = filenames[i] 
    # Construct the full file path
    #print(filename)
    file_path = filenames[i] 

    # Load the image using OpenCV
    image = cv2.imread(file_path)

    # Add the image to the list
    images.append(image)
  for i in range(num):
    images[i]=images[i][:,350:450]

  images= np.array(images)
  return images


def decaptcha( filenames ):
  # Invoke your model here to make predictions on the images
  loaded_model = tf.keras.models.load_model("model.h5")

  images = load_images(filenames)

  images = images /255. 

  y_preds = loaded_model.predict(images , verbose=0)>0.5

  num = len(y_preds) 
  labels = [] 
  #print(y_preds)
  for i in range(num):
    if(y_preds[i]==False):
      labels.append("ODD")
    else:
      labels.append("EVEN")


  return labels