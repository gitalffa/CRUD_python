import turtle

window = turtle.Screen()
tortuga = turtle.Turtle()

def make_square(forward, left):
    i = 0
    while(i < 4):
        tortuga.forward(forward)
        tortuga.left(left)
        i = i + 1
    window.mainloop()


make_square(100, 90)