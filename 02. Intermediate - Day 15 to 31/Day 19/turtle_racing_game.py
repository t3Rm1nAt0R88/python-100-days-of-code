from turtle import Turtle, Screen
import random


is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(1,7):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i-1])
    timmy.penup()
    timmy.goto(-230, -125 + (i*35))
    turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        # Checking winner
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winnner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winnner!")
        # Turtle racing
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)
    


screen.exitonclick()