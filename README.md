# <p align='center'>IT496 - Introduction to Data Mining</p>
### <p align='center'>ICC Cricket World Cup 2023 ML Challange</p>
**Course Project**: 3 <br/>
**Lab Group**: T06<br />
##### Table of Contents  
[1.Project Overview](#project-overview) <br/>
[2.Web Application](#web-application) <br/>
[3.Dataset scraping](#dataset-scraping) <br/>
[4.Tasks and Implementation](#tasks-and-implementation) <br/>
[5.Results and Conclusion](#results-and-conclusion) <br/>
## <p align='center'>Project Overview</p>
In this project we have worked on the ICC Cricket World Cup 2023 prediction, which involves building and deploying machine learning models to make informative predictions related to the tournament. As a part of it, we have did the following tasks<br/>
**Task 1**:
* decid the task
* decide the taks

**Task 2**:
*  Predicting the Finalist Teams and Players
  
**Task 3**:
* Predicting the winner of ICC World cup 2023
## <p align='center'>Web Application</p>
This application demonstrates the Match winner prediction model that was built as a part of this project.<br/>
To run this Application follow these steps:
### 1. Clone the repository and navigate to project folder:
```bash
git clone https://github.com/Gangaraj-eng/IT496_CP3_T06
cd .\IT496_CP3_T06
```

### 2. Install the required packages:
```bash
pip install -r requirements.txt
```
In case if there are any version issues, please install these packages manually - Flask, Numpy, Pandas, tensorFlow, scikit-learn
### 3. Navigate to the App folder and run server.py file
```
cd .\App
python server.py
```
The application will be accessible at http://127.0.0.1:8000/

### 4. Make predictions by giving inputs
* Select the two playing teams and Venue
* Click on the predict button
* Predict results for winner and the respective team composition prediction(playing 11) of each team will be displayed<br/>

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/3fa8c772-781b-47d9-861c-2297ab8b4e2b)
## <p align='center'>Dataset Scraping</p>
To carry out proper predictions, comprehensive and reliable data is essential. We have collected the data related to the past cricket matches, team performance and players statistics from various websites.The collected dataset files can be found [here](https://github.com/Gangaraj-eng/IT496_CP3_T06/tree/main/Dataset). These dataset includes the following files
1. ICC_Player_Stats.csv - Individual player statistics in ODI’s
2. ICC_Matches_Stats.csv - Data related to all the matches played in ICC world cup for the last 7 seasons from 1999, 2003, 2007, 2011, 2015, 2019, 2023
3. ODI_Matches.csv - Data related to all the ODI Matches from 2017-2023
4. ICC_Team_Stats.csv - Team wise statistics which includes data like ODI ranking of the team, number of matches played by team and some average statistics of team players.
5. Matches_Stats.csv - combined matches data of ICC world cup and ODI data collected.
6. ICC_TeamComposition.csv - Composition of batter, bowlers and all rounders of the team for the ICC world cup 2023
7. ICC_Venues_List.csv - List of all the venues used for ICC and ODI Matches
8. ICC 2023 Kaggle: Data of ICC 2023 collected from kaggle
    * deliveries.csv - ball wise data for each match
    * matches.csv  - matches wise teams and winners data
    * points_table.csv - data related to points table

**Individual player statistics in ODI**
The individual statistics of each player of all time from the day of debut till date were scraped. The data includes attributes like matches played, runs scored, batting average, not-outs, boundaries scored, and centuries and half-centuries.The players participating in the current World Cup are only included in the team.Only the team of 15 players declared before the World Cup are included.<br/>
Source: [ESPN cricketing website](https://www.espncricinfo.com/records/most-runs-in-career-83548) <br/>
![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/2e471e7a-b97d-4711-991f-62904fc12fe3)
<br/>

**Head to Head statistics of each country in ODI**
The head-to-head data of each match played in the past 8 years in the ODI is collected in this sheet. The attributes present in it are the names of two teams in that particular match, the venue, the margin of victory, and the winner.<br/>
Source: [ESPN cricketing website](https://www.espncricinfo.com/records/year/team-match-results/2016-2016/one-day-internationals-2)<br/>

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/ac1c7870-3d6a-4f38-b78a-9c062aee7e6a)



**Head to Head statistics of each team in the past World Cups**
This is very similar to the above dataset, but the only difference here is that the matches held during the past World Cups are included, example:1999,2003,2007.This data is scraped from the cricbuzz website using python with BeautifulSoap.The code used for scrapping can be found in this [file](https://github.com/Gangaraj-eng/IT496_CP3_T06/blob/main/Models/DataPreparation.ipynb)<br/>
Source: [Cricbuzz](https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches)<br/>

**Team Composition**
The Dataset contains a number of Batsmen, Bowlers and All-Rounders for each team given the match venue.
Source: EPSN cricketing website<br/>

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/54e592be-0698-4d36-8624-b7c5882afaec) <br/>


## <p align='center'>Tasks and Implementation</p>

**Match Winner Prediction model**: 
Given two teams and venue, the model will predict which team will probably win the match. For this task, team wise statistics like team rank, team number of matches, team avg score over the past matches are extracted from multiple csv data files that we have collected. The final data that is used for training the model have the following columns - Season, Team1, Team2, Winner, Venue, Team1 Avg score, Team 1 Avg wickets, Team 1 Avg catches, Team 1 Avg fours, Team 1 Avg sixes, Team 1 ODI Rank, Team 2 Avg score, Team 2 Avg wickets,Team 2 Avg catches, Team 2 Avg fours, Team 2 Avg sixes, Team 2 ODI Rank.<br/>
**Model used**: Neural Netowrk<br/>
**Mapping**: All the team are given a unique ID and all the venues are given a unique ID. The encoding from string to a number is done using these mapping which can be extracted from the teams and venues csv files respectively.<br/>
The architecture of the model is as shown 

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/212a6914-fe57-49fb-bb21-a9c1f3c19f92)

The input data is standardised using RobustScaler, and this Robust Scaler is fitted on train data, and saved in a file so that the same scaler can be used at the inference time.<br/>
The train and validation accuracy and loss vs the number of epochs: <br/>
![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/6dd55b69-c35c-4fa1-8bd2-b3c87ff4f743)

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/6950831d-9d97-4625-9e42-976fdd4944bc)<br/>
With increase in number of epoch, both the validation and training loss are decreasing and accuracy is increasing which indicates that model is actually learning.
<br/>
**Test Accuracy**: 76%<br/>
The test accuracy of the above model is 76%. Then this model is saved as a keras file for use at inference time!!.<br/>
The saved model can be found at [MatchWinnerPredictor.keras](https://github.com/Gangaraj-eng/IT496_CP3_T06/blob/main/Models/MatchWinnerPredictor.keras)<br/>
The implementation can be found at [MatchWinnerPredictorModel.ipynb](https://github.com/Gangaraj-eng/IT496_CP3_T06/blob/main/Models/MatchWinnerPredictorModel.ipynb)

**Task 2**:  To predict the two finalist teams<br/>
Approach : We have trained the model using the data from the last 6 ICC world cups in addition to the ICC 2023 matches completed till now. There are 4 teams left in the tournament. Two semi-finals and one-final. The venues of these 3 matches are fixed and the teams that are going to play with each other are also given. These are the 3 matches that are left:
| Team 1 | Team 2| Venue | Match |
| --- | --- | --- | --- |
| India | New Zealand | Wankhede Stadium, Mumbai | semi-finals|
| South Africa | Australia | Eden Gardens, Kolkata | semi-finals | 
|  - |  - | Narendra Modi Stadium, Ahmedabad | finals| 
<br/>
The teams that play the final are yet to be decided. Using the Neural network model that we had built, we predicted the winner for the two semi-final matches which gives the input teams for the final!!.<br/>


**Team Composition Prediction**:  For predicting the playing 11 of each team, we had used the following approach
Approach:  Given the team, the venue and the opposite team, we had collected the team composition of the number of bowlers, batsmen and all rounders that were used by these teams in the previous world cup matches. Given the inputs, we assign weights to each player depending upon the requirement of number of bowlers, batsmen and all rounders according to the venue. As we have the data about each player and his role, a batsman is given weight according to the runs score and the number of batsmen required in the current match, similarly a bowler is given weight according to the wickets taken by him and the required bowlers and so on. To give the weights, we used the ratio of current player performance divided by the performance of all the 15 players in the team. For a batsmen, <br/>
	```
 Weight =(runs scored by player)/(total runs by all players) * batsman_weight```
<br/>
Similarly for bowler and all rounder. For an all rounder, we considered both runs and wickets.<br/>

**Task 3**: To predict the finalist of ICC world cup 2023<br/>
Using the Neural Network model built and the two finalist teams from the previous task, we had given these two teams as input to the model and predicted the winning team of the finals.<br/>




## <p align='center'>Results and Conclusion</p>
**Task 2**: The two semi-final schedules were given as input to the model.
<br/>
![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/b854419d-7618-4002-8ed6-0624244826ab)<br/>
The model predicted the winning probabilty for Team 1(India) as 0.699 and for Team 2(New Zealand) as 0.304. Thus India has won the semi-final 1.<br/>
<br/>
![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/7d36871f-dfd4-4647-95ac-22069f053bf9)<br/>
The model predicted the winning probabilty for Team 1(South Africa) as 0.76 and for Team 2(India) as 0.24. Thus South Africa has won the semi-final 1.<br/>

**Team Composition Prediction**:
The following are the list of 11 players from both the finalist teams.

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/53b8377b-a28a-4b55-9db3-71e14c6a6c15)

**Task 3**: 
The above two teams India and South Africa were given as inputs to the model.<br/>
![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/2b1af08a-95cd-42ec-8674-e119e1065565)<br/>

**Result**: According to our model, India will win the ICC World Cup 2023 Tournament with a probabilty of 80%!!<br/>

**Contributions**:
| Name | ID | Contribution|
| --- | --- | ---|
| Saineni Rohit Rao | 202001003 | Attribute summary: 18-34 <br/> Data Preprocessing <br/> Documentation | 
| Rohan Reddy Patlolla | 202001076 | Attribute summary: 52-68 <br/> Exploratory data analysis <br/> Train test splitting and model defining |
| Nipun Shah | 202001096 | Attribute summary: 35-51 <br/> Data Preprocessing <br/> Documentation |
| Gangaraju Bopparam | 202001107 | Attribute summary: 1-17 <br/> Training, Hyperparameter tuning <br/> and Evaluation |
| Rishit Shah | 202001411 | Attribute summary: 68-87 <br/> Exploratory Data Analysis <br/> Documentation |
