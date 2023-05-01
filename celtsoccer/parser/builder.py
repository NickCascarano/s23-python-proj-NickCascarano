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
    position_data = {}

    # iterates over all countries
    for country, player in data.items():

        # for each country, iterates over all players
        for player_name, player_data in player.items():
            # the first entry in player_data is the position the
            # player plays
            player_position = player_data[0]

            # if the position is not in the temp dictionary, creates the entry
            # with that position as key and assigns as value the player name
            if player_position not in position_data:
                position_data[player_position] = [player_name]

            # if the position is already in the temp dictionary, references that entry
            # and appends as value the player name
            else:
                position_data[player_position].append(player_name)

    return position_data


# This function returns a dictionary
# Key -> country
# Value -> list of players from that country

############################################# code finished below
def build_roster_data(data):
    roster_data = {}
    for country, players in data.items():
        roster_data[country] = list(players)
    return roster_data
############################################# code finished above

# This function returns a dictionary
#   Key -> number of goals
# Value -> list all players who scored that number of goals

############################################# code finished below
def build_goals_score_data(data):
    goals_score_data = {}
    for country, players in data.items():
        for player, player_data in players.items():
            player_goals = player_data[8]
            if player_goals not in goals_score_data:
                goals_score_data[player_goals] = []
            if player not in goals_score_data[player_goals]:
                goals_score_data[player_goals].append(player)
    return goals_score_data
############################################# code finished above
# This function returns a dictionary
#   Key -> country
# Value -> nested dictionary, where:
#       Key -> name of a club
#     Value -> list of players in that club for that country
############################################# code finished below
def build_country_club_data(data):
    country_club_data = {}
    for country, players in data.items():
        for player_name, player_data in players.items():
            player_club = player_data[2]
            if country not in country_club_data:
                country_club_data[country] = {}
            if player_club not in country_club_data[country]:
                country_club_data[country][player_club] = []
            country_club_data[country][player_club].append(player_name)
    return country_club_data
############################################# code finished above
# This function returns a dictionary
#   Key -> club name
# Value -> nested dictionary, where:
#       Key -> country
#     Value -> list of players in that country that play for that club
############################################# code finished below
def build_club_country_data(data): #This code will be used for the most_common_club stat
    club_country_data = {}
    for country, players in data.items():
        for player_name, player_data in players.items():
            player_club = player_data[2]
            if player_club not in club_country_data:
                club_country_data[player_club] = {}
            if country not in club_country_data[player_club]:
                club_country_data[player_club][country] = []
            club_country_data[player_club][country].append(player_name)
    build_club_country_data_result = club_country_data
    return build_club_country_data_result
############################################# code finished above

# This function returns a dictionary
#   Key -> year
#   Value -> list of players that were born in that year

############################################# code finished below
def build_year_player_data(data):
    birth_year_data = {}
    for country, players in data.items():
        for player, player_data in players.items():
            player_birth_year = player_data[3]
            if player_birth_year not in birth_year_data:
                birth_year_data[player_birth_year] = []
            if player not in birth_year_data[player_birth_year]:
                birth_year_data[player_birth_year].append(player)
    return birth_year_data
############################################# code finished above


# This function returns a dictionary
#   Key -> starts
# Value -> nested dictionary, where:
#       Key -> country
#     Value -> list of players from that country that started that number of games

############################################# code finished below
def build_start_player_data(data):
    player_start_data = {}
    for country, players in data.items():
        for player_name, player_data in players.items():
            player_starts = player_data[5]
            if player_starts not in player_start_data:
                player_start_data[player_starts] = {}
            if country not in player_start_data[player_starts]:
                player_start_data[player_starts][country] = []
            player_start_data[player_starts][country].append(player_name)
    return player_start_data
############################################# code finished above


def build_country_list(data):
    temp_data = {}
    for country, player in data.items():
        if country not in temp_data:
            temp_data[country] = player

    key_list = []
    for key in temp_data:
        key_list.append(key)

    return key_list


