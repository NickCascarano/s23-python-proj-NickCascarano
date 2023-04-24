"""stats functions

This module computes some statistics from the text corpus.
You have to implement these functions.
"""
import celtsoccer

# Finds the club with the highest number of players and returns a tuple,
# with the name of the club and the total number of minutes played by the
# players of that club.


################################################################ Finished Below
def most_common_club(primary_data, club_country_data):
    club_minutes = {}
    for club in club_country_data:
        total_minutes = 0
        for country in club_country_data[club]:
            for player in club_country_data[club][country]:
                player_data = primary_data[country][player]
                total_minutes += player_data[6]
        club_minutes[club] = total_minutes

    max_minutes = None
    max_club = None
    for club, minutes in club_minutes.items():
        if max_minutes is None or minutes > max_minutes:
            max_minutes = minutes
            max_club = club

    return (max_club, max_minutes)
################################################################# Finished Above


# Finds the top scorer for a given country, returns a tuple with the name
# of the player and the number of goals scorer. If there are more than
# one player with the same number of goals, returns the one at the top alphabetically.
################################################################## Working Below
def top_scorer(data): #this function works, done
    top_scorers_dict = {}
    for country, players in data.items():
        top_scorer_name = ''
        top_scorer_goals = 0
        for player_name, player_stats in players.items():
            player_goals = player_stats[8]
            if player_goals > top_scorer_goals:
                top_scorer_name = player_name
                top_scorer_goals = player_goals
            elif player_goals == top_scorer_goals and player_name < top_scorer_name:
                top_scorer_name = player_name
                top_scorer_goals = player_goals
        top_scorers_dict[country] = (top_scorer_name, top_scorer_goals)
    return top_scorers_dict
################################################################## Working Above
# Computes the average goals scored for players of a given club.
# The average is the sum of goals for players for that club,
# divided by the number of players of that club who scored goals
# (don't count players who didn't score).
def avg_goals_scored(data):
  print('Stats module computing -> avg_goals_scored: ' + club_name + ': ',  end='')
  club_dict = {}
  for country, player in data.items():
    for player_name, player_data in player.items():
      player_club_name = player_data[2]
      player_goals_scored = player_data[8]
      if player_club_name not in club_dict:
        club_dict[player_club_name] = [player_goals_scored, 1]
      else:
        club_dict[player_club_name][0] += player_goals_scored
        club_dict[player_club_name][1] += 1

  result = {}
  for club_name, goals_count in club_dict.items():
    goals_scored = goals_count[0]
    player_count = goals_count[1]
    if player_count > 0:
      result[club_name] = goals_scored / player_count
  return result


# Returns a list with tuples, in which each entry is a pair (player, minutes played)
# but including only those players whose club name starts with the letter passed
# as argument letter.
def get_players_club_begin(data, letter):
    print('Stats module computing -> get_players_club_begin: ' + letter + ': ', end='')
    players = []

    # your code goes here

    return players


# Returns a list with tuples, in which each entry is a pair (player, minutes played)
# but including only those players whose name starts with the letter passed as argument letter.
def get_players_name_begin(data, letter):
    print('Stats module computing -> get_players_name_begin: ' + letter + ': ', end='')
    players = []

    # your code goes here

    return players


# Returns a list with tuples, in which each entry is a pair (player, minutes played)
# but including only those players whose minutes played is less than limit.
def get_players_minutes_played(data, limit):
    print('Stats module computing -> get_players_minutes_played: ' + str(limit) + ': ', end='')
    players = []

    # your code goes here

    return players


# Returns a list with tuples, in which each entry is a pair (country, avg_goals)
# where avg_goals is the number of goals scored by players of that country divided by 3.
def compute_avg_goals_countries(data):
    print('Stats module computing -> compute_avg_goals_countries: ', end='')
    countries_avg_goals = []

    # your code goes here

    return countries_avg_goals


# Returns a list with tuples, in which each entry is a pair (country, total_cards).
# In which, total_cards is the total number of cards for players of that country,
# depending on the argument color, you will compute either the total number of
# yellow or red cards ('y' or 'r') which is passed as argument in color.
def compute_cards_per_country(data, color='y'):
    print('Stats module computing -> compute_cards_per_country: ', end='')
    countries_total_cards = []

    # your code goes here

    return countries_total_cards

