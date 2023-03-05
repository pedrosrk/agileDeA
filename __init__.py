from flask import Flask, jsonify, request
from app import dataAnalysis as deA
from mainDB import dataBase as db

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

# Get an user by user_id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = db()
    user = data.get_user(user_id)
    return jsonify(user)

# Update an user by user_id
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    newUser = request.get_json()
    data = db()
    user = data.update_user(user_id, newUser)
    return jsonify(user)

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = db()
    user = data.delete_user(user_id)
    return jsonify(user)

# Create a new user
@app.route('/users/create', methods=['POST'])
def create_user():
    newUser = request.get_json()
    data = db()
    user = data.create_user(newUser)
    return jsonify(user)

def production():
  from waitress import serve
  serve(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0')
    production()