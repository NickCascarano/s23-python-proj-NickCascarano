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
def top_scorer(data, country=''):
  local_max = 0
  for country_name, player in data.items():
    if country_name == country:
      for player_name, player_data in player.items():
        goals_scored = player_data[8]
        if goals_scored > local_max:
          result = (player_name, goals_scored)
          local_max = goals_scored
        elif goals_scored < local_max:
          continue
        elif goals_scored == local_max:
          if player_name < result[0]:
            result = (player_name, goals_scored)
  return result
################################################################## Working Above
# Computes the average goals scored for players of a given club.
# The average is the sum of goals for players for that club,
# divided by the number of players of that club who scored goals
# (don't count players who didn't score).
def avg_goals_scored(data, club=''):
  running_total = 0
  count = 0
  for country, player in data.items():
    for player_name, player_data in player.items():
      if club == player_data[2]:
        if player_data[8] > 0:
          running_total += player_data[8]
          count += 1
  return (club, round((running_total / count),2))


# Returns a list with tuples, in which each entry is a pair (player, minutes played)
# but including only those players whose club name starts with the letter passed
# as argument letter.
def get_players_club_begin(data, letter):
    print('Stats module computing -> get_players_club_begin: ' + letter + ': ', end='')
    players = []
    for country, player in data.items():
      for player_name, player_data in player.items():
        first_letter_of_club  = player_data[2][0]
        if letter == first_letter_of_club:
          players.append((player_name, player_data[7]))
    return players


# Returns a list with tuples, in which each entry is a pair (player, minutes played)
# but including only those players whose name starts with the letter passed as argument letter.
def get_players_name_begin(data, letter):
    print('Stats module computing -> get_players_name_begin: ' + letter + ': ', end='')
    players = []
    for country, player in data.items():
      for player_name, player_data in player.items():
        player_first_letter = player_name[0]
        if player_first_letter == letter:
          players.append((player_name, player_data[6]))
    return players


# Returns a list with tuples, in which each entry is a pair (player, minutes played)
# but including only those players whose minutes played is less than limit.
def get_players_minutes_played(data, limit):
    print('Stats module computing -> get_players_minutes_played: ' + str(limit) + ': ', end='')
    players = []
    #7
    for country, player in data.items():
      for player_name, player_data in player.items():
        minutes_played = player_data[6]
        if minutes_played < limit:
          players.append((player_name, minutes_played))
    return players


# Returns a list with tuples, in which each entry is a pair (country, avg_goals)
# where avg_goals is the number of goals scored by players of that country divided by 3.
def compute_avg_goals_countries(data):
    print('Stats module computing -> compute_avg_goals_countries: ', end='')
    countries_avg_goals = []

    for country, player in data.items():
      running_total = 0
      for player_name, player_data in player.items():
          running_total += player_data[8]
      countries_avg_goals.append((country, round((running_total / 3),2)))

    return countries_avg_goals


# Returns a list with tuples, in which each entry is a pair (country, total_cards).
# In which, total_cards is the total number of cards for players of that country,
# depending on the argument color, you will compute either the total number of
# yellow or red cards ('y' or 'r') which is passed as argument in color.
def compute_cards_per_country(data, color='y'):
    print('Stats module computing -> compute_cards_per_country: ', end='')
    countries_total_cards = []
    running_total = 0
    for country, player in data.items():
      for player_name, player_data in player.items():
        if color == 'r':
          cards = player_data[12]
        elif color == 'y':
          cards = player_data[11]
        else:
          print('Please Input a Valid Card Color')
        running_total += cards
      countries_total_cards.append((country, running_total))
      running_total = 0
    return countries_total_cards

