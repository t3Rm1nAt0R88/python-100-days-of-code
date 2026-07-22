from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_leftward():
    tim.left(10)

def move_rightward():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen = Screen()

my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=move_leftward)
my_screen.onkey(key="d", fun=move_rightward)
my_screen.onkey(key='c', fun=clear_screen)

my_screen.exitonclick()
