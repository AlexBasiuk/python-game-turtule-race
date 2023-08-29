import random
import turtle
from turtle import Turtle, Screen
is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make your bet", prompt="Who is going to win the race? Enter of color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtules = []

for turtule_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtule_index])
    new_turtle.color(colors[turtule_index])
    all_turtules.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtules:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()