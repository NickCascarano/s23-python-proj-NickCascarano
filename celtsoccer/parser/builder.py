# *************************************************
# Functions
# *************************************************
# build_position_data: builds the position_data dictionary by using as input values
# passed as argument on the parameter data, when the function is invoked
# Don't modify this function.
# This function returns a dictionary where:
# Key -> position
#   Value -> list all players in that position

def build_position_data(data):
    temp_data = {}

    # iterates over all countries
    for country, player in data.items():

        # for each country, iterates over all players
        for player_name, player_data in player.items():
            # the first entry in player_data is the position the
            # player plays
            player_position = player_data[0]

            # if the position is not in the temp dictionary, creates the entry
            # with that position as key and assigns as value the player name
            if player_position not in temp_data:
                temp_data[player_position] = [player_name]

            # if the position is already in the temp dictionary, references that entry
            # and appends as value the player name
            else:
                temp_data[player_position].append(player_name)

    return temp_data

# This function returns a dictionary
# Key -> country
# Value -> list of players from that country

def build_roster_data(data):
    temp_data = {}

    # your code goes here

    return temp_data

# This function returns a dictionary
#   Key -> number of goals
# Value -> list all players who scored that number of goals

def build_goals_score_data(data):
    temp_data = {}

    # your code goes here

    return temp_data


# This function returns a dictionary
#   Key -> country
# Value -> nested dictionary, where:
#       Key -> name of a club
#     Value -> list of players in that club for that country

def build_country_club_data(data):
    temp_data = {}

    # your code goes here

    return temp_data


# This function returns a dictionary
#   Key -> club name
# Value -> nested dictionary, where:
#       Key -> country
#     Value -> list of players in that country that play for that club

def build_club_country_data(data):
    temp_data = {}

    # your code goes here

    return temp_data


# This function returns a dictionary
#   Key -> year
#   Value -> list of players that were born in that year

def build_year_player_data(data):
    temp_data = {}

    # your code goes here

    return temp_data


# This function returns a dictionary
#   Key -> starts
# Value -> nested dictionary, where:
#       Key -> country
#     Value -> list of players from that country that started that number of games

def build_start_player_data(data):
    temp_data = {}

    # your code goes here

    return temp_data



