# importing required libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = r'C:\Users\UCS\.spyder-py3\Plant-Leaf-Disease-Prediction-main/model/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_Plant_leaf_dieas(leaf_disease_plant):
  test_image = load_img(leaf_disease_plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==0:
      return "Pepperbell-Bacterial spot", 'Pepper__bell__Bacterial_spot.html'
  elif pred==1:
      return "Pepperbell-healthy", 'Pepper_bell_healthy.html'
  elif pred==2:                              
      return "Potato-Early blight", 'Potato__Early_blight.html'
  elif pred==3:
      return "Potato-healthy", 'Potato__healthy.html'
  elif pred==4:
      return "Tomato-Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'
  elif pred==5:
      return "Tomato-Healthy and Fresh", 'Tomato-Healthy.html'  
  elif pred==6:
      return "Tomato-Late Blight Disease", 'Tomato - Late_blight.html'  
  elif pred==7:
      return "Tomato-Leaf Mold Disease", 'Tomato - Leaf_Mold.html'
  elif pred==8:
      return "Tomato-Septoria Leaf Spot Disease", 'Tomato - Septoria_leaf_spot.html'
  elif pred==9:
      return "Tomato-Tomato Mosaic Virus Disease", 'Tomato - Tomato_mosaic_virus.html'
  elif pred==10:
      return "Tomato-Tomoato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'
  

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join(r'C:\Users\UCS\.spyder-py3\Plant-Leaf-Disease-Prediction-main/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page =  pred_Plant_leaf_dieas(leaf_disease_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    

