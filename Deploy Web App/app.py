from flask import Flask,render_template,request,url_for
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

#EDA Packages
import pandas as pd
import numpy as np
import pickle

#import model
cv = CountVectorizer()
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def predict():

	# masih salah di predict nya scv error
	if request.method == 'POST':
		text = request.form['comment']
		data = [text]
		result = model.predict(data)

	return  render_template('result.html',prediction = result,comment = comment)


if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8080,debug=True)
