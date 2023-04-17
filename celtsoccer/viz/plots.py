import turtle

# This script has functions to plot bar graphs on the screen using the turtle
# graphic library. Implementing the last three functions is optional and a
# bonus to the project
turtle.speed("fastest")
newXPosition = 720 / -2
newYPosition = 675 / -2
print('Window height:' + str(newXPosition))
print('Window width:' + str(newYPosition))


def writeText(theText, x, y):
    turtle.speed("fast")
    turtle.penup()
    turtle.goto(newXPosition + x, newYPosition + y)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.write(theText, True, align="left", font=("Arial", 20, "normal"))


def draw_bar(x, y, height, width, color):
    turtle.pencolor(color)
    turtle.pensize(0)
    turtle.penup()
    turtle.setposition(newXPosition + x, newYPosition + y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()


# plots the counts of the top k items in a container
# this is just an example and is intended for you to understand how to use the plotting module
def plot_top_k_fake_items_doc(data, item, k):
    print('plot_top_k_fake_items_doc: ', end='')

    count = 0  # number of bars
    values = list(data[item].values())  # extract values from dictionary
    values.sort(reverse=True)

    writeText('Top ' + str(k) + ' items in ' + item, 20, 300)

    for v in values[:k]:
        count += 1
        draw_bar(20 * count, 100, v + 100, 10, 'red')
        writeText(v, 20 * count, v + 220)

    writeText('Click anywhere on this window to close the display', 20, 550)

# plots the counts of goals scored by the top k players of a given club, where k is a number between 1 and 5.
# For example if you pass 3, the plot includes the top 3 scorers.
def plot_top_k_scorer_club(soccer_data, club, k):
    print('plot_top_k_scorer_club: ')

    # your code goes here


# plots the counts of goals scored by the top k players of a given country, where k is a number between 1 and 5.
# For example if you pass 3, the plot includes the top 3 scorers
def plot_top_k_scorer_country(soccer_data, country, k):
    print('plot_top_k_scorer_country: ')

    # your code goes here


# Plots the total number of goals per country.
def plot_goals_per_country(soccer_data):
    print('plot_goals_per_country: ')

    # your code goes here


# Plots the total number of yellow cards per country
def plot_yellow_cards_per_country(soccer_data):
    print('plot_yellow_cards_per_country: ')

    # your code goes here


# Plots the total number of red cards per country
def plot_red_cards_per_country(soccer_data):
    print('plot_red_cards_per_country: ')

    # your code goes here


def render():
    turtle.update()  # Render image
    turtle.exitonclick()  # Wait for user's mouse click

    # your code goes here
