from flask import Flask, jsonify, request, render_template
from app import dataAnalysis as deA
from mainDB import dataBase as db
import random

app = Flask(__name__)

#---------------------------------------------------------------------------------Modeling Routes---------------------------------------------------------------------------------
@app.route('/portuguese', methods=['POST'])
def portugueseModel():
    data = request.get_json()
    sentimentAnalysis = deA(data['text'])
    result = sentimentAnalysis.sentimentMultinomialNBModel()
    return jsonify(result)


@app.route('/english', methods=['POST'])
def englishModel():
    data = request.get_json()
    sentimentAnalysis = deA(data['text'])
    result = sentimentAnalysis.englishSentiment()
    return jsonify(result)

#---------------------------------------------------------------------------------User Routes--------------------------------------------------------------------------------------
# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    data = db()
    users = data.get_users()
    return jsonify(users)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')