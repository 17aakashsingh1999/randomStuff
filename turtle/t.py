from turtle import Turtle
from time import sleep
from math import ceil,pi

fward = 4
lt = 10

color = ['red', 'blue', 'yellow', 'green', 'pink', 'violet', 'brown', 'orange']

n = len(color)
d = 0
perD = 360/n

turtles = []

for col in color:
    temp = Turtle()
    temp.color(col)
    temp.width(5)
    temp.left(d)
    d += perD
    turtles.append(temp)

for i in range(ceil(180/lt)):
    for t in turtles:
        t.forward(fward)
        t.left(lt)

for i in range(16):
    for t in turtles:
        t.forward(fward)
        t.left(2)

stem = Turtle()
stem.up()
stem.right(90)
stem.width(30)
f = int(2*(180/lt)*fward/pi)
print(f)
stem.forward(f)
stem.down()
stem.forward(300)

sleep(5)
