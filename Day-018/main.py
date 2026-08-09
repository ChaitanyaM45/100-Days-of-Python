from turtle import Turtle, Screen
import random
# import colorgram

# colors=colorgram.extract(r'C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-018\hirst.jpg',25)

# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colors=[(184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27), (228, 229, 231), (12, 57, 73), (31, 100, 120), (101, 41, 48), (57, 137, 121), (108, 40, 29), (22, 65, 50), (40, 80, 7), (94, 62, 68), (110, 8, 9), (199, 91, 65), (116, 167, 77), (131, 178, 92), (224, 231, 225), (139, 167, 175), (216, 202, 142), (178, 147, 150), (179, 205, 177), (225, 177, 167)]
tim=Turtle()
Screen().colormode(255)
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()
no_of_dots=100
for i in range(1,no_of_dots+1):
    tim.dot(30,random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if i%10==0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()



Screen().exitonclick()