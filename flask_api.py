from flask import Flask, request, jsonify
app = Flask(__name__)

import pickle
import pandas as pd
with open("classifier.pkl","rb")as f:
    classifier = pickle.load(f)

@app.route("/")
def greet():
    return "Hello world"

@app.route("/input")
def get_input():
    return "please provide input"

@app.route("/predict", methods = ['POST'])
def predict():
    data = request.get_json()
    print(data)
    input_df = pd.DataFrame([{
    "variance": data['variance'],
    "skewness": data['skewness'],
    "curtosis": data['curtosis'],
    "entropy": data['entropy']}])
    #result = classifier.predict([[variance,skewness,curtosis,entropy]])
    result = classifier.predict(input_df)
    if result[0] == 1:
        pred = "Authorised"
    if result[0] == 0:
        pred = "Unauthorised"
    print("The result is ",result[0])
    #return jsonify({"The Currency Note is ": int(result[0])})
    return jsonify({"The Currency Note is ": pred})

