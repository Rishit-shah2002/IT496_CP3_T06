# Team Composition Predictor 
# Given Team A, Team B and Venue, it will return the playing 11 of both the teams!!!
# Only Teams and players playing in ICC 2023 are considered

# importing libraries
import pandas as pd
import numpy as np

# returns the data of 15 players of the team
def getPlayersData(teamName):
    players_data = pd.read_csv('../Dataset/ICC_Player_Stats.csv') 
    players_data = players_data[players_data['Team Name'] ==teamName]
    return players_data


# return the weghts given according to bowlers, batsman and allrounders required
def getWeights(teamName, venue):
    data = pd.read_csv('../Dataset/ICC_TeamComposition.csv')
    data = data[data["Team_Name"]==teamName]
    data = data[data["Venue"]==venue]
    exp_batsmen = data['Batsmen'].values[0]
    exp_bowlers = data['Bowlers'].values[0]
    exp_allrounders = data['All_rounders'].values[0]
    return [exp_batsmen/11.0 , exp_bowlers/11.0, exp_allrounders/11.0]

# return the 11 players names of the team for a particular venue
def getPlayingEleven(teamName, Venue):
    players_data = getPlayersData(teamName)
    [batsmanWeight, bowlerWeight, AllRounderWeight] = getWeights(teamName, Venue)
    totalAvg = players_data['Average'].sum()
    totalWickets = players_data['Wickets Taken'].sum()
    total = ((players_data['Runs']+players_data['Wickets Taken'])/players_data['Matches']).sum()
    for index,row in players_data.iterrows():
        playerWeight = 0
        if row['Specalist']=="Batsman":
            playerWeight+=(row['Average']/totalAvg)*batsmanWeight
        elif row['Specalist']=="Bowler":
            playerWeight+=(row['Wickets Taken']/totalWickets)*bowlerWeight
        else:
            playerWeight+=((row['Runs']/row['Matches']+row['Wickets Taken']/row['Matches'])/total)*AllRounderWeight
        players_data.loc[index,['Weight']] = playerWeight
    playerList = players_data.sort_values(by=['Weight'], ascending=False)['Player name'].values[0:11]
    return playerList


def getTeamCompsition(team1, team2, venue):
        team1List = getPlayingEleven(team1, venue)
        team2List = getPlayingEleven(team2, venue)
        return team1List, team2List
