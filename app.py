from __future__ import division, print_function
import os
import numpy as np
import codecs
import textract

with open('Recommondations/fall army worm.txt', encoding='utf-8') as f:
    input1 = f.read()
#print(input1)

#with open('D:/M.Tech/S.Y/DP3/diseases/marathi2.txt', encoding='utf-8') as f:
    #input2 = f.read()

#with open('D:/M.Tech/S.Y/DP3/diseases/marathi3.txt', encoding='utf-8') as f:
    #input3 = f.read()

with open('Recommondations/maize stem borer.txt', encoding='utf-8') as f:
    input4 = f.read()

#with open('D:/M.Tech/S.Y/DP3/diseases/marathi5.txt', encoding='utf-8') as f:
    #input5 = f.read()
#with open('D:/M.Tech/S.Y/DP3/diseases/marathi6.txt', encoding='utf-8') as f:
    #input6 = f.read()

#text = textract.process("D:/M.Tech/S.Y/DP3/diseases/marathi2.docx")
#text = text.decode("utf-8")

# Keras

from keras.models import load_model
from keras.preprocessing import image
from werkzeug.utils import secure_filename # use to store the file name
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from PIL import Image, ImageOps
import streamlit as st

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/maize model.h5'

# Load your trained model
model = load_model(MODEL_PATH)

# print('Model loaded. Start serving...')

#print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_data, model):
    size=(224,224)
    img = ImageOps.fit(img_data, size)

    # Preprocessing the image
    x = image.img_to_array(img)
    x = x * 1./255
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x]) #Stack arrays in sequence vertically (row wise).
    res = np.argmax(model.predict(images)) #Returns the indices of the maximum values .
    return res

#@app.route(’/’) , where @app is the name of the object containing our Flask app
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        if f is None:
            st.text("Please upload an image file")
        else:
            image = Image.open(f)
            st.image(image, use_column_width=True)
        # Make prediction
        preds = model_predict(image, model) # call prediction function
	
	

        disease_list=[input1,'Green Stink Bug','Maize Cob Borer',input4,'Pink Stem Borer', 'Spodoptera litura','No Leaf', 'Healthy Corn Leaf']    

        result = disease_list[int(preds)]
        return result
    return None



if __name__ == '__main__':
    
    app.run(debug=True)
