import turtle, time

def sq(a):
    for i in range(4):
        joe.color(colors[i%4])
        joe.forward(a)
        joe.left(90)

colors = ['red', 'brown', 'green', 'blue']
len = 30

joe = turtle.Turtle()
joe.speed(100)

for i in range(60):
    sq(len)
    joe.right(10)
    len+=4

time.sleep(5)