import turtle

# setting up window
turtle.setup(width = 1100, height = 800)
turtle.bgcolor("black")


#for convinence
screen = turtle.Screen()

#getting paddles and ball ready
pad1 = turtle.Turtle()
pad2 = turtle.Turtle()
ball = turtle.Turtle()

paddle = "paddle.gif"
screen.register_shape(paddle)

def setupPad1(pad1):
    pad1.speed(0)
    pad1.penup()
    pad1.shape(paddle)
    pad1.setposition(500, 0) 


def setupPad2(pad2):
    pad2.speed(0)
    pad2.penup()
    pad2.shape(paddle)
    pad2.setposition(-500, 0)

def setupBall(ball):
    ball.speed(0)
    ball.penup()
    ball.shape('circle')
    ball.color("white")


def padImpact(pad):
    impact = False
    newAngle = 0
    #first check for close x coordinates
    if abs(ball.xcor() - pad.xcor()) < 20:
        # then check y coordinates
        if (ball.ycor() <= pad.ycor() + 50) and ( ball.ycor() >= pad.ycor() - 50):
            

            #turn ball around and record the distance from the center of the pad
            #to use for deciding what angle the ball should rebound at
            ball.left(180)
            impactDist = (ball.ycor() - pad.ycor())

            #
            if pad == pad1:
                ball.setheading(-impactDist + 180)
                newAngle = (-impactDist + 180)
                ball.setx( pad.xcor() + 1)
            elif pad == pad2:
                ball.setheading(impactDist)
                newAngle = impactDist
            impact = True

            # need to keep track of the angle and whether or not an impact has occured.
            # note this will only return if an impact occurs, otherwise the funciton just returns none
            return (impact, newAngle)

def boundryImpact(angle):

    # different cases for if the ball hits the top or bottom,
    # and if its moving left or right

    if ball.ycor() <= -395:
        if direction:
            ball.setheading( -(angle) )
            angle = -(angle)

        elif not direction:
                ball.setheading(-(angle))
                angle = -(angle)
    if ball.ycor() >= 395:
        if direction:


            ball.setheading( -(angle) )
            angle = -(angle)

        elif not direction:
            ball.setheading(-(angle))
                
            angle = -(angle)




    return angle



def resetCheck(direction):
    
    if ball.xcor() > 600 or ball.xcor() < -600:
        ball.setposition(0,0)
        ball.setheading(0)
        pad1.setposition(500, 0) 

        # ball always moves right when reset
        direction = 1
    return direction   



def controlPad2(diff):
    # originaly I wanted to make it so pad2 would change its direction in a more analog fashion
    # but when I tried that it always made it impossible to score on the computer.
    # So until I can figure out a better way, I will just hardcode in the behavior of pad2
    if diff < 0:
        neg = -1
        diff *= -1
    else:
        neg = 1

    if diff >= 0 and diff < 10:
       pad2.sety((pad2.ycor()) )

    if diff >= 10 and diff < 50:
        pad2.sety( (pad2.ycor() + 6 * neg) )

    if diff >= 50 and diff < 100:
        pad2.sety( (pad2.ycor() + 14 * neg) )

    if diff >= 100 and diff < 150:
        pad2.sety( (pad2.ycor() + 18 * neg) )

    if diff >= 150 and diff < 200:
        pad2.sety( (pad2.ycor() + 30 * neg) )

    if diff >= 200 and diff < 250:
        pad2.sety( (pad2.ycor() + 36 * neg) )

    if diff >= 250 and diff < 300:
        pad2.sety((pad2.ycor() + 19 * neg) )
        
    if diff > 300:
        pad2.sety( (pad2.ycor() + 12 * neg) )


if __name__ == "__main__":
    angle = 0
    setupPad1(pad1)
    setupPad2(pad2)
    setupBall(ball)
    
    # "1" means we are moving right, "0" means we are moving left
    direction = 1

    # game loop
    while True:  
        directionChange = False
        # making sure the first pad moves with the mouse
        pad1.sety(-screen.cv.winfo_pointery() + 570)

        controlPad2(ball.ycor() - pad2.ycor())
        
        ball.forward(20)

        # if impactcheck does not return None, then an impact has occurd and
        # thus a tuple with the new angle and a boolean is returned
        if direction and padImpact(pad1) != None:
            tup = padImpact(pad1)
            directionChange = tup[0]
            angle = tup[1]
        elif not direction and padImpact(pad2) != None:
            tup = padImpact(pad2)
            directionChange = tup[0]
            angle = tup[1]

        if directionChange and direction:
            direction = 0
        elif directionChange and not direction:
            direction = 1

        if boundryImpact(angle) != None:
            angle = boundryImpact(angle)
        direction = resetCheck(direction)

    turtle.done()