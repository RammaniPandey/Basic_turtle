import turtle
Cppsecrets = turtle.Screen()
Cppsecrets.bgcolor("black")
Python = turtle.Turtle()
Python.shape("turtle")
Python.color("red")

Python.penup()
Cplusplus = 20
for i in range(30):
   Python.stamp()            
   Cplusplus = Cplusplus +  2          
   Python.forward(Cplusplus)   
   Python.right(24)           

Cppsecrets.mainloop()