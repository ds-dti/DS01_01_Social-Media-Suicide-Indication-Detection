from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import autokeras
import keras
import tensorflow as tf

app = Flask(__name__)
api = Api(app)

model = keras.models.load_model('./Model/English Suicide Prevention Model')

post_args = reqparse.RequestParser()
post_args.add_argument("tweet", type=str, help="Need Tweet predict", required=True)

text = {}

# def preprocessing(text):

class Posts(Resource):
    def post(self):
        args = post_args.parse_args()
        test_set = tf.data.Dataset.from_tensor_slices([args["tweet"]])
        y =  model.predict(test_set)
        return {"probability" : float(y)}

api.add_resource(Posts, "/Posts")

if __name__ == '__main__':
    app.run(debug=True)