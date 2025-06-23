#Task 8: Sports Statistics
#Create a program for a football team that:

#Stores overall goals scored, overall goals conceded and number of games played
#Calculates goal difference
#If they played 10 games, calculate the average goals per game
#Display all relevant statistics

overall_goals_scored = 6
overall_goals_conceded = 5
number_of_games_played = 3

goal_difference = (overall_goals_scored - overall_goals_conceded)
if number_of_games_played == 10:
    average_goals = overall_goals_scored / number_of_games_played
    print("average goals per game", average_goals)
    

print("overall goals scored =",overall_goals_scored)
print("overall goals conceded =",overall_goals_conceded)
print("number of games played =",number_of_games_played)
print("goal difference =",goal_difference)