from turtle import *

import celtsoccer
import celtsoccer.stats as stats
import celtsoccer.parser as parser
import celtsoccer.viz as viz
import pprint
from test_student_1 import soccer_data
from test_student_1 import position_data
from test_student_1 import roster_data
from test_student_1 import goals_score_data
from test_student_1 import country_club_data
from test_student_1 import club_country_data
from test_student_1 import year_player_data
from test_student_1 import start_player_data
from test_student_1 import country_list

# The student working on the stats (computing statistics) should modify this
# script.

# change this value to 1 for displaying the viz plots
display_plots = 0

print('***************************************************')
print('building dictionaries')
print('***************************************************')

# As your teammate implements the dictionary-related functions and the
# data is populated in the correct dictionaries, you will be using
# that data for testing your stats functions. In the meantime you can
# use the fake data.

print('***************************************************')
print('computing stats')
print('***************************************************')

# You have to implement the functions in stats, then depending on what
# dictionaries you built before, you have to decide which one to pass as
# argument to these stats functions.
# Presently these functions are returning empty results because
# the dictionaries are empty

pprint.pprint('Computing some stats and printing the results')
result = stats.most_common_club(soccer_data, club_country_data)
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.top_scorer(soccer_data, 'Argentina')
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.avg_goals_scored(soccer_data, 'Brighton')
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.get_players_club_begin(soccer_data, 'A')
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.get_players_name_begin(soccer_data, 'A')
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.get_players_minutes_played(soccer_data, 325)
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.compute_avg_goals_countries(soccer_data)
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.compute_cards_per_country(soccer_data, color='y')
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

result = stats.compute_cards_per_country(soccer_data, color='r')
pprint.pprint(result, width=150, compact=False, sort_dicts=False)

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
    viz.plot_top_k_scorer_club(parser.fake_top_scorers, 'Paris S-G', 5)
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