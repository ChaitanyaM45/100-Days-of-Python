'''We will use this code to find rgb values of the colors in the image'''

import colorgram

colors=colorgram.extract(r'C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-018\hirst.jpg',25)

rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)