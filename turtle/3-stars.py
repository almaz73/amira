import turtle, time

joe = turtle.Turtle()

def starFill(n, len):
    joe.begin_fill()
    star(n, len)
    joe.end_fill()

def star(n, len):
    if n % 2 != 0:
        for i in range(n):
            joe.forward(len)
            angle = n // 2 * 360 / n
            joe.left(angle)


for i in range(5, 16, 2):
    joe.speed(100)
    starFill(i, 300)
    time.sleep(1)
    print(i)
    if i != 15:
        joe.reset()

time.sleep(5)
