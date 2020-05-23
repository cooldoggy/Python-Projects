import random
import turtle as t
t.bgcolor('yellow')
caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
leaf = t.Turtle()
leaf_shape=((0,0), (14,2), (18,6), (20,20), (6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
gamestarted=False
textturtle=t.Turtle()
textturtle.write('Press SPACE to start', align='center',font=('Arial',16,'bold'))
textturtle.hideturtle()
scoreturtle = t.Turtle()
scoreturtle.hideturtle()
scoreturtle.speed(0)
def outsidewindow():
    leftwall = -t.window_width() / 2
    rightwall= t.window_width() / 2
    topwall= t.window_height() / 2
    bottomwall= -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = x< leftwall or x> rightwall or y< bottomwall or y> topwall
    return outside
def gameover():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))
    gamestarted=False
def displayscore(current_score):
    scoreturtle.clear()
    scoreturtle.penup()
    x= (t.window_width() / 2) -50
    y= (t.window_height() / 2) -50
    scoreturtle.setpos(x, y)
    scoreturtle.write(str(current_score), align = 'right', font = ('Arial', 40, 'bold'))
def placeleaf():
    leaf.ht()
    leaf.setx(random.randint((-t.window_width() // 2), (t.window_width() // 2)))
    leaf.sety(random.randint((-t.window_height() // 2), (t.window_height() // 2) ))
    leaf.st()
def startgame():
    global gamestarted
    if gamestarted:
        return
    gamestarted = True
    score = 0
    textturtle.clear()
    t.clear()
    caterpillar_speed=2
    caterpillar_length=3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    caterpillar.color('red')
    leaf.color('green')
    displayscore(score)
    placeleaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            placeleaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 1
            displayscore(score)
        if outsidewindow():
            gameover()
            break
def moveup():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
def movedown():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
def moveleft():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)
def moveright():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
t.onkey(startgame, 'space')
t.onkey(moveup, 'Up')
t.onkey(moveright,'Right')
t.onkey(movedown,'Down')
t.onkey(moveleft, 'Left')
t.listen()
t.mainloop()
