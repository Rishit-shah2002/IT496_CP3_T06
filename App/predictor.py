
from tensorflow import keras
import pickle
import sys
sys.path.insert(1,'../Models')
from teamCompositionPredictor import getTeamCompsition
import pandas as pd
from Helpers import getTeamsMapping, getTeamStats, getVenuesMapping, getPlayerRole
import numpy as np

# loading pre-trained models
nn_model = keras.models.load_model('../Models/MatchWinnerPredictor.keras')
with open('../Models/RobustScaler.pkl','rb') as f:
   scaler = pickle.load(f)

teamsMapping = getTeamsMapping()
venuesMapping = getVenuesMapping()
additional_cols1 = ['team1 avg score','team1 avg wickets','team1 avg catches','team1 avg fours',
                   'team1 avg sixes','team1 odi rank']
additional_cols2 = ['team2 avg score','team2 avg wickets','team2 avg catches','team2 avg fours',
                   'team2 avg sixes','team2 odi rank']
matches = pd.DataFrame(columns=['season', 'team1', 'team2', 'Venue', 'team1 avg score',
       'team1 avg wickets', 'team1 avg catches', 'team1 avg fours',
       'team1 avg sixes', 'team1 odi rank', 'team2 avg score',
       'team2 avg wickets', 'team2 avg catches', 'team2 avg fours',
       'team2 avg sixes', 'team2 odi rank'])

class Player:
   def __init__(self,name,role) -> None:
      self.name = name 
      self.role = role

class Prediction:
    def __init__(self,winner,prob, team1, team2) -> None:
       self.winner = winner
       self.winningProbability =str(round(prob*100))+'%'
       self.team1 = team1
       self.team2 = team2

def getPrediction(team1, team2, venue):
    matches.loc[0,['season','team1','team2','Venue']]=['2023',team1,team2,venue]
    matches.loc[0,additional_cols1] = getTeamStats(matches.iloc[0]['team1'])
    matches.loc[0,additional_cols2] = getTeamStats(matches.iloc[0]['team2'])
    matches['Venue'] = matches['Venue'].apply(lambda x:venuesMapping[x])
    matches.loc[0,'team1'] = teamsMapping[matches.iloc[0]['team1']]
    matches.loc[0,'team2'] = teamsMapping[matches.loc[0]['team2']]
    input1 = np.asarray(matches.iloc[0])
    x1 = scaler.transform(np.expand_dims(input1,axis=0))
    y_pred = nn_model.predict(x1)[0]
    if y_pred[0]>y_pred[1]:
       winner = team1
       winProb = y_pred[0]
    else:
       winner = team2
       winProb = y_pred[1]
       
    team1, team2 = getTeamCompsition(team1, team2, venue)
    t1 = [Player(name,getPlayerRole(name)).__dict__ for name in team1]
    t2 = [Player(name,getPlayerRole(name)).__dict__ for name in team2]
    return Prediction(winner, winProb,t1,t2)