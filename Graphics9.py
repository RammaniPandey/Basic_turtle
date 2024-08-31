import turtle
turtle.bgcolor("black")
Cppsecrets = turtle.Screen()
Cppsecrets.title("Animation Circle ")
turtle=turtle.Turtle()
turtle.color("red")
turtle.speed(0)
turtle.hideturtle()
for i in range(1000):
  turtle.circle(i*2)
  turtle._rotate(5 )