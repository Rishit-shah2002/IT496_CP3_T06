# Team T06 - IT496 CP3 
# This is the main file that is used to run the application

# importing libraries
from flask import Flask,render_template, request, jsonify
import json
from predictor import getPrediction

# Initialize app using Flask
app = Flask(__name__)

jsonDataFile = open('../Dataset/ICC23Data.json')
jsonData = json.load(jsonDataFile)

# IP Address and Port Number to run the app
IpAddr = '127.0.0.1'
Port = 8000


# default route
@app.route('/')
def index():
    teamsList = jsonData['TeamsList']
    venueList = jsonData['VenueList']
    return render_template("index.html",teamsList = teamsList, venueList=venueList)

# getting the prediction
@app.route('/predict',methods=['Post'])
def predict():
    inputData = request.json
    team1 = inputData['team1']
    team2 = inputData['team2']
    venue = inputData['venue']
    print(team1,team2,venue)
    result = getPrediction(team1, team2, venue)
    return jsonify(result.__dict__)

# Run the API
if __name__ == '__main__':
   app.run(host=IpAddr, port=Port,debug=True)

# To run the server, enter the following command in terminal  
# python server.py