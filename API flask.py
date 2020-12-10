from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import numpy as np
import autokeras
import keras
import tensorflow as tf
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)
api = Api(app)

model = keras.models.load_model('./Model/English Suicide Prevention Model')

post_args = reqparse.RequestParser()
post_args.add_argument("tweet", type=str, help="Need Tweet predict", required=True)

text = {}

def preprocessing(args):
    # Case Folding
    # Convert text to lowercase
    args["tweet"] = args["tweet"].lower()

    # Remove Twitter megatext_clean Link and RT word
    args["tweet"] = args["tweet"].replace(r'http\S+', '').replace(
        r'www\S+', '').replace(r'rt', '')

    # Remove number
    args["tweet"] = args["tweet"].replace('\d+', '')

    # Remove Punctuation
    args["tweet"] = args["tweet"].replace('[^\w\s]', '')

    # Remove Whitespaces
    args["tweet"] = args["tweet"].strip()

    # Tokenization
    args["tweet"] = nltk.word_tokenize(args["tweet"])
    # StopWords Removal
    stop_words = stopwords.words('english')
    args["tweet"] = [item for item in args["tweet"] if item not in stop_words]

    # Stemming
    ps = PorterStemmer()
    args["tweet"] = [ps.stem(item) for item in args["tweet"]]

    # Lemmetizer
    lemmatizer = WordNetLemmatizer()
    args["tweet"] = [lemmatizer.lemmatize(item) for item in args["tweet"]]

    return args


class Posts(Resource):
    def post(self):
        args = post_args.parse_args()
        args = preprocessing(args)
        test_set = tf.data.Dataset.from_tensor_slices(np.reshape(args["tweet"][0], -1))
        y = model.predict(test_set)
        return {"probability" : float(y)}

api.add_resource(Posts, "/Posts")

if __name__ == '__main__':
    app.run(debug=True)