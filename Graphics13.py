#Python program for drawing a Spirograph in Turtle   
# Importing the turtle Python library   
import turtle as trtl  
  
# Setting the background color as black,  
# size of pen as 2.5 and   
# the curve drawing speed as 20(relative)  
trtl.Screen().bgcolor('black')  
trtl.pensize(0.1)  
trtl.speed(20)  
  
# Iterating the drawing six times overall  
for j in range(500):  
  
    # Choosing the colors for the combination  
    for color in ('violet', 'white', 'blue',  
                'green', 'yellow', 'orange',  
                'red',):  
        trtl.color(color)  
          
        # Drawing a circle of selected size 80  
        trtl.circle(80)  
          
        # Moving 10 pixels to the left every time   
        # a circle is drawn for drawing the next one  
        trtl.left(10)  
      
    # Hiding the turtle after the completion of our drawing  
    trtl.hideturtle()