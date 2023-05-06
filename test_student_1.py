from turtle import *
import celtsoccer.stats as stats
import celtsoccer.parser as parser
import celtsoccer.viz as viz
import pprint

# The student working on the parser (populating the dictionaries) should modify this
# script.

# change this value to 1 for displaying the viz plots
display_plots = 0

# which_dataset indicates which dataset to use
#   1 is for the fake_dataset.csv (6 countries, 12 players)
#   2 is for the dataset.csv (5 countries, 111 players)
#   3 is for the dataset_large.csv (32 countries, 160 players)
#   4 is for the dataset_larger.csv (32 countries, 680 players)
# To test your script with a different dataset change the value of this
# variable, by default use 1, which corresponds to fake_data.csv file
which_dataset = 4

datasets = {
    1: 'fake_data.csv',
    2: 'dataset.csv',
    3: 'dataset_large.csv',
    4: 'dataset_larger.csv'
}

if which_dataset < 1 or which_dataset > 4:
    print('----> use a value between 1 and 4 for which_dataset')
    exit()

# ************************************************
# Dictionary variables
# ************************************************

# These are the variables for storing data as dictionaries.
# Initially they are empty, see below to understand when they will be populated.

soccer_data = {}
position_data = {}
roster_data = {}
goals_score_data = {}
country_club_data = {}
club_country_data = {}
year_player_data = {}
start_player_data = {}

# ************************************************
# Invoking functions to build and populate the
# dictionaries.
# ************************************************

print('***************************************************')
print('building dictionaries')
print('***************************************************')

# builds a dictionary that has as key the country, and the value is a nested dictionary,
# where the key is the player's name and the value a list with all the data for that player

soccer_data = parser.read_file(datasets[which_dataset])

print('******* Original Soccer Data *******')
pprint.pprint(soccer_data, width=140, compact=False, sort_dicts=False)
print('There are ', len(soccer_data), ' countries in the dataset!')

# using the dictionary soccer_data built in the previous step to
# build a new dictionary storing the values in the variable position_data

# Note: as you implement the other functions that populate the rest
# of the dictionaries, look at the output of the previously populated
# dictionaries to decide which is the best suited to be passed as
# argument to each function. In this example, soccer_data is used
# but most likely you have to use different containers for each
# invocation of the functions.
# Also, you don't have to read again the data from the file. It has
# already loaded and stored in the variable soccer_data


print('******* Position Data *******')
position_data = parser.build_position_data(soccer_data)
pprint.pprint(position_data, width=50, compact=False, sort_dicts=False)

print('******* Roster Data *******')
roster_data = parser.build_roster_data(soccer_data)
pprint.pprint(roster_data, width=150, compact=False, sort_dicts=False)

print('******* Goals Score Data *******')
goals_score_data = parser.build_goals_score_data(soccer_data)
pprint.pprint(goals_score_data, width=150, compact=False, sort_dicts=False)

print('******* Country Club Data *******')
country_club_data = parser.build_country_club_data(soccer_data)
pprint.pprint(country_club_data, width=150, compact=False, sort_dicts=False)

print('******* Club Country Data *******')
club_country_data = parser.build_club_country_data(soccer_data)
pprint.pprint(club_country_data, width=150, compact=False, sort_dicts=False)

print('******* Year Player Data *******')
year_player_data = parser.build_year_player_data(soccer_data)
pprint.pprint(year_player_data, width=150, compact=False, sort_dicts=False)

print('******* Starts Player Data *******')
start_player_data = parser.build_start_player_data(soccer_data)
pprint.pprint(start_player_data, width=150, compact=False, sort_dicts=False)

print('******* Country List *******')
country_list = parser.build_country_list(soccer_data)
print(country_list)

if display_plots == 1:
    # Implementing the functions below is optional and a bonus for the project
    # they are not required
    print('***************************************************')
    print('******* Showing some plots *******')
    print('***************************************************')

    # Plots the top 3 scorers for team 'Paris S-G', uses fake data
    # just to illustrate how the viz module works
    viz.plot_top_k_fake_items_doc(parser.fake_top_scorers, 'Paris S-G', 4)

    # Plots the counts of goals scored by the top k players of a given club,
    # where k is a number between 1 and 5. For example if you pass 3,
    # the plot includes the top 3 scorers.
    # viz.plot_top_k_scorer_club(soccer_data, 'Juventus', 3)

    # plots the counts of goals scored by the top k players of a given country,
    # where k is a number between 1 and 5. For example if you pass 3, the plot
    # includes the top 3 scorers.
    # viz.plot_top_k_scorer_country(soccer_data, 'Argentina', 3)

    # Plots the total number of goals per country.
    # viz.plot_goals_per_country(soccer_data)

    # Plots the total number of yellow cards per country
    # viz.plot_yellow_cards_per_country(soccer_data)
    # viz.plot_red_cards_per_country(soccer_data)

    # makes the plot function to stop, uncomment this line when working on your code
    # to test the functions in the viz module
    viz.render()

