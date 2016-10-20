import turtle

def draw_square(someturtle):    
    someturtle.forward(100)
    someturtle.right(90)
    
    someturtle.forward(100)
    someturtle.right(90)
    
    someturtle.forward(100)
    someturtle.right(90)
    
    someturtle.forward(100)
    someturtle.right(90)
    
    
window  = turtle.Screen()
window.bgcolor("red")

brad = turtle.Turtle()

brad.shape("turtle")
brad.color("yellow")
brad.speed(2)
for i in range(1,37):
    draw_square(brad)
    brad.right(10)