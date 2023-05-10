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

def plot_top_k_scorer_club(data, club, k):
    # get the top k players and their goal counts for the specified club
    players = data[club]
    top_k = sorted(players.items(), key=lambda x: x[1][-1], reverse=True)[:k]
    top_k_names = [player[0] for player in top_k]
    top_k_goals = [player[1][-1] for player in top_k]

    # create the turtle window and set up the coordinate system
    window = turtle.Screen()
    window.setworldcoordinates(-1, -5, k, max(top_k_goals) + 5)
    window.bgcolor("white")

    # create the turtle for drawing the bars
    bar_turtle = turtle.Turtle()
    bar_turtle.speed(0)
    bar_turtle.penup()

    # create the turtle for drawing the x-axis labels
    label_turtle = turtle.Turtle()
    label_turtle.speed(0)
    label_turtle.penup()

    # draw the bars and labels
    for i in range(len(top_k)):
        bar_turtle.goto(i + 0.5, 0)
        bar_turtle.pendown()
        bar_turtle.setheading(90)
        bar_turtle.begin_fill()
        bar_turtle.forward(top_k_goals[i])
        bar_turtle.color("black")
        bar_turtle.write(str(top_k_goals[i]), align="center", font=("Arial", 10, "normal"))
        bar_turtle.right(90)
        bar_turtle.forward(0.5)
        bar_turtle.right(90)
        bar_turtle.forward(top_k_goals[i])
        bar_turtle.end_fill()
        bar_turtle.penup()
        label_turtle.goto(i + 0.5, -3)
        label_turtle.write(top_k_names[i], align="center", font=("Arial", 10, "normal"))

    # draw the x-axis
    bar_turtle.goto(-0.5, 0)
    bar_turtle.pendown()
    bar_turtle.forward(k)
    bar_turtle.penup()

    # add the axis labels
    label_turtle.goto(-0.5, -4)
    label_turtle.write("Player", align="center", font=("Arial", 12, "bold"))
    label_turtle.goto(k/2-0.5, -6)
    label_turtle.write("Goals Scored", align="center", font=("Arial", 12, "bold"))

    # hide the turtles and exit the window
    bar_turtle.hideturtle()
    label_turtle.hideturtle()
    turtle.done()

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
