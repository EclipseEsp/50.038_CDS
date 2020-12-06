import time
from flask import Flask,request
import cv2
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model,load_model
import base64

app = Flask(__name__)

 # VGG16 Model Initializtion
try:
  vgg16_model = 'VGG16_1'
  trained_model = load_model(vgg16_model)

  # img = image.load_img('sample_image.jpg')

  label_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
except Exception as e:
  print(str(e))

# classify_waste
@app.route('/classify_waste',methods=['POST'])
def classify_waste():
  if request.method=='POST':
    imagefile = str(request.get_data())
    # https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
    encoded_data = imagefile.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  try:
    # test = cv2.imread(img)
    test = cv2.resize(img,(224,224))
    # data preprocessing to get the input in the same shape
    x = image.img_to_array(test)  # this is a Numpy array with shape (3, x, y) 
    x = x * 1./255
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, x, y)

    pred = trained_model.predict_classes(x)  #getting your prediction index
    confidence = trained_model.predict_proba(x) #getting your prediction confidence levels
    # label_names = [i for i in train_set.class_indices.keys()]  #label names
    print('Input image is predicted to be {label_names[pred[0]]} with confidence level of {max(confidence[0])*100}%')
  except Exception as e:
    print(str(e))

  # return {'pred': 0}
  return {'pred': max(confidence[0])*100} #time.time()
