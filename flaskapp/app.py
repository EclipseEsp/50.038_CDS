import time
from flask import Flask
import cv2
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model,load_model

app = Flask(__name__)

 # VGG16 Model Initializtion
try:
  vgg16_model = f'VGG16_model-20201201T171520Z-001/VGG16_model/VGG16_1'
  trained_model = load_model(vgg16_model)

  # img = image.load_img('sample_image.jpg')

  label_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
except Exception as e:
  print(str(e))


# classify_waste
@app.route('/classify_waste')
def classify_waste():
  try:

    test = cv2.imread('sample_image.jpg')
    test = cv2.resize(test,(224,224))
    # data preprocessing to get the input in the same shape
    x = image.img_to_array(test)  # this is a Numpy array with shape (3, x, y) 
    x = x * 1./255
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, x, y)

    pred = trained_model.predict_classes(x)  #getting your prediction index
    confidence = trained_model.predict_proba(x) #getting your prediction confidence levels
    # label_names = [i for i in train_set.class_indices.keys()]  #label names
    print(f'Input image is predicted to be {label_names[pred[0]]} with confidence level of {max(confidence[0])*100}%')
  except Exception as e:
    print(str(e))


  return {'pred': max(confidence[0])*100} #time.time()
