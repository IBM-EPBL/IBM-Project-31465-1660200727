#from crypt import methods
from pyexpat import features, model
import numpy as np
import pickle
#import joblib
#import matplotlib
#import matplotlib.pyplot as plt
#import time
import pandas
#import os
from flask import Flask, request, jsonify, render_template, redirect, url_for



# Declare a Flask app
app = Flask(__name__,template_folder='template')

model = pickle.load(open("rainfall.pkl",'rb'))
scale = pickle.load(open("scale.pkl",'rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chance/',methods=['GET', 'POST'])
def chance():
    return render_template("chance.html")

@app.route('/nochance/',methods=['GET', 'POST'])
def nochance():
    return render_template("noChance.html")


@app.route('/help/')
def help():
    return render_template("help.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/predict',methods=["POST","GET"])
def predict():
    res = " "
     # If a form is submitted
    if request.method == "POST":
        input_feature=[x for x in request.form.values() ]
        features_values=[np.array(input_feature)]
        names = [['Location','MinTemp','MaxTemp','Rainfall','WindGustSpeed',
        'WindSpeed9am','WindSpeed3pm','Humidity9am','Humadity3pm',
        'Pressure9pm','Pressure3am','Temp9pm','Temp3pm','RainyTodaty',
        'WindGustDir','WindDir9pm','WindDir3pm']]
        data = pandas.DataFrame(features_values,columns=names)
        data = scale.fit_transform(data)
        data = pandas.DataFrame(data,columns=names)

        #Get prediction
        prediction = model.predict(data)

    else:
        prediction = ""

    if prediction == 1:
       return redirect(url_for('chance'))

    elif prediction == 0:
        return redirect(url_for('nochance'))
 
    return render_template("index.html", output = res)



#Running the app

if __name__== "___main___":
    app.run(debug = True,host='0.0.0.0',port=80)