# Used Colorgram to extract the colors from an image
# import colorgram

# colors = colorgram.extract("images.jpeg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

import random
import turtle as t

t.colormode(255)

color_list = [
    (205, 202, 198),
    (189, 169, 141),
    (132, 169, 193),
    (43, 104, 148),
    (139, 69, 94),
    (178, 78, 44),
    (218, 163, 20),
    (193, 140, 158),
    (18, 33, 72),
    (154, 28, 49),
    (138, 181, 161),
    (186, 93, 124),
    (46, 53, 108),
    (188, 203, 214),
    (49, 129, 89),
    (217, 198, 129),
    (6, 107, 59),
    (210, 197, 203),
    (221, 172, 181),
    (76, 156, 115),
    (207, 183, 181),
    (203, 89, 67),
    (49, 23, 51),
    (195, 206, 200),
    (7, 61, 29),
    (109, 118, 164),
    (64, 151, 175),
    (165, 201, 211),
    (157, 29, 22),
    (171, 203, 190),
]

timmy = t.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.goto(-200, -200)
timmy.speed("fastest")
for i in range (1, 11):
    for j in range(1, 11):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.goto(-200, -200 + i*50)





my_screen = t.Screen()
my_screen.exitonclick()
