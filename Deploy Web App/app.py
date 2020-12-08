from flask import Flask,render_template,request,url_for
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
# from sklearn.svm import SVC #model for svm

#EDA Packages
import pandas as pd
import numpy as np
import pickle

#import model
cv = CountVectorizer()
# model = pickle.load(open('model.pkl', 'rb')) #model for svm
model = load_model('Model.h5')

app = Flask(__name__)

#main page
@app.route("/")
def index():
	return render_template("index.html")

#predict function
@app.route("/",methods=['POST'])
def predict():
	# masih salah di predict nya scv error
	if request.method == 'POST':
		text = request.form['comment']
		data = [text]
		result = model.predict(data)
		#test_set = tf.data.Dataset.from_tensor_slices((X_test.astype(np.unicode), y_test))
	return  render_template('result.html',prediction = result,comment = comment)


if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8080,debug=True)
