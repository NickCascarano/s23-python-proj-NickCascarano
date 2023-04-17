"""stats functions

This module computes some statistics from the text corpus.
You have to implement these functions.
"""


# Finds the club with the highest number of players and returns a tuple,
# with the name of the club and the total number of minutes played by the
# players of that club.
def most_common_club(data):
    print('Stats module computing -> most_common_club: ', end='')

    total_minutes_played = 0
    club = ''

    # your code goes here

    return (club, total_minutes_played)


# Finds the top scorer for a given country, returns a tuple with the name
# of the player and the number of goals scorer. If there are more than
# one player with the same number of goals, returns the one at the top alphabetically.
def get_top_scorer(data, country):
    print('Stats module computing -> get_top_scorer: ', end='')

    goals_scored = 0
    country = ''

    # your code goes here

    return (country, goals_scored)


# Computes the average goals scored for players of a given club.
# The average is the sum of goals for players for that club,
# divided by the number of players of that club who scored goals
# (don't count players who didn't score).
def avg_goals_scored(data, club):
    print('Stats module computing -> avg_goals_scored: ' + club + ': ',  end='')

    club_avg_goals_scored = 0
    club = ''

    # your code goes here

    return (club, club_avg_goals_scored)


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

