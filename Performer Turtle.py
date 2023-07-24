from turtle import*
for i in range(16):
    left(36)
    forward(4*40)
    left(36)
penup()
for x in range(-10,10):
    for y in range(-10,10):
        setpos(x*40,y*40)
        dot(4,'red')   