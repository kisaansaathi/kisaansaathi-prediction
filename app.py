from __future__ import division, print_function
import os
import numpy as np
import codecs
import textract

with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    mp1 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #mp2 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #mp3 = f.read()
with open('Recommondations/maize pest/maize stem borer.txt', encoding='utf-8') as f:
    mp4 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #mp5 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #mp1 = f.read()


#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #rp1 = f.read()
with open('Recommondations/Rice pest/Brown Plant hopper.txt', encoding='utf-8') as f:
    rp2 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #rp3 = f.read()
with open('Recommondations/Rice pest/Gandhi Bug.txt', encoding='utf-8') as f:
    rp4 = f.read()
with open('Recommondations/Rice pest/Green Hopper.txt', encoding='utf-8') as f:
    rp5 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #rp6 = f.read()
with open('Recommondations/Rice pest/leaf folder.txt', encoding='utf-8') as f:
    rp7 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #rp8 = f.read()
#with open('Recommondations/maize pest/fall army worm.txt', encoding='utf-8') as f:
    #rp9 = f.read()
with open('Recommondations/Rice pest/stem borer.txt', encoding='utf-8') as f:
    rp10 = f.read()
#print(input1)

#with open('D:/M.Tech/S.Y/DP3/diseases/marathi2.txt', encoding='utf-8') as f:
    #input2 = f.read()

#with open('D:/M.Tech/S.Y/DP3/diseases/marathi3.txt', encoding='utf-8') as f:
    #input3 = f.read()

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

@app.route('/maize_predict', methods=['GET', 'POST'])
def maize_upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        if f is None:
            st.text("Please upload an image file")
        else:
            image = Image.open(f)
            st.image(image, use_column_width=True)
        # Model saved with Keras model.save()
        MODEL_PATH = 'models/maize model.h5'

        # Load your trained model
        model = load_model(MODEL_PATH)

        # Make prediction
        preds = model_predict(image, model) # call prediction function
	
	

        pest_list=[mp1,'<h3 style="color:red;">ग्रीन स्टिंक बग</h3>','<h3 style="color:red;">मक्का बेधक</h3>',mp4,'<h3 style="color:red;">गुलाबी तना बेधक (Pink Stem Corer)</h3>','<h3 style="color:red;">स्पोडोप्टेरा लिटुरा </h3>','अपलोड की गई छवि डेटासेट पर उपलब्ध नहीं है','<h3 style="color:green;">स्वस्थ मकई का पत्ता, अगर प्रभावित हिस्सा है तो फिर से तस्वीर अपलोड करें</h3>']    

        result = pest_list[int(preds)]
        return result
    return None

@app.route('/rice_predict', methods=['GET', 'POST'])
def rice_upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        if f is None:
            st.text("Please upload an image file")
        else:
            image = Image.open(f)
            st.image(image, use_column_width=True)
        # Model saved with Keras model.save()
        MODEL_PATH = 'models/rice model.h5'

        # Load your trained model
        model = load_model(MODEL_PATH)

        # Make prediction
        preds = model_predict(image, model) # call prediction function
	
	

        pest_list=['<h3 style="color:red;">बीट वेबवर्म </h3>',rp2,'<h3 style="color:red;">यूबलम्मा </h3>',rp4,rp5,'<h3 style="color:red;">हॉर्न कैटरपिलर</h3>',rp7,'<h3 style="color:red;">राइस मील्यबग</h3>','<h3 style="color:red;">राइस स्किपर</h3>',rp10,'<h3 style="color:red;">येलो टेल मोत </h3>','अपलोड की गई तस्वीर डेटासेट पर उपलब्ध नहीं है', '<h3 style="color:green;">स्वस्थ चावल का पत्, अगर प्रभावित हिस्सा है तो फिर से तस्वीर अपलोड करे</h3>']    

        result = pest_list[int(preds)]
        return result
    return None

if __name__ == '__main__':
    
    app.run(debug=True)
