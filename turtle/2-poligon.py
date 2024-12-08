import turtle, time

pen = turtle.Turtle()
pen.speed(100)
pen.up()
pen.setposition(-90, -200)
pen.down()


def poligon(n, len):
    print(n)
    sumAngle = (n - 2) * 180
    if sumAngle % n == 0:
        myAngle = sumAngle // n
        for i in range(n):
            pen.forward(len)
            pen.left(180 - myAngle)


for i in range(3, 20):
    poligon(i, 100)

time.sleep(8)