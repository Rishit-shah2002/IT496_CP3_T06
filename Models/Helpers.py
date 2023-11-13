import pandas as pd

# Functions to get team name to team ID mappings and venue name to venue ID mappings. As names should be converted to a 
# numerical value before training the model, and these same mappings should be used for testing too.

# function to get team Name to team ID mapping
def getTeamsMapping():
  teams_data = pd.read_csv('../Dataset/ICC_23_Teams_List.csv')
  teams_mapping={}
  for index,row in teams_data.iterrows():
    teams_mapping[row['Team Name']] = row['Team ID']
  return teams_mapping

# function to get venue name to venue Id mapping
def getVenuesMapping():
  venues_data = pd.read_csv('../Dataset/ICC_VenuesList.csv')
  venues_mapping = {}
  for index,row in venues_data.iterrows():
    venues_mapping[row['Venue']] = row['venue ID']
  return venues_mapping

# to get the team details like
# team avg score, team avg catches, team avg wickets, team odi ranking
def getTeamStats(teamName):
  team_stats = pd.read_csv('../Dataset/ICC_Team_Stats.csv')
  return team_stats[team_stats['Team Name']==teamName][['Avg Score','Avg Wickets','Avg Catches','Avg Fours','Avg Sixes','ICC Ranking(ODI)']].values[0]


# to get the player role from name
def getPlayerRole(playerName):
   players_data = pd.read_csv('../Dataset/ICC_Player_Stats.csv')
   return players_data[players_data['Player name']==playerName]['Specalist'].values[0]