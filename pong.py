
import turtle
import time
import random

# This variable represents the x position
# of the player's paddle. Initially, it
# will be 0 (i.e. in the center). The y
# position of the paddles never changes,
# so we don't need a variable for it.
user1x = 0

# This variable represents the x position
# of the computer's paddle. Initially, it
# will be 0 (i.e. in the center)
user2x = 0

# These variables store the current x and y
# position of the ball. Their values will be
# updates on each frame, as the ball moves.
ballx = 0
bally = 0

# These variables store the current x and y
# velocity of the ball. Their values will be
# updates on each frame, as the ball moves.
ballvx = 0
ballvy = 0

# These variables store the current score 
# of the game.
user1points = 0
user2points = 0


def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the paddles,
    the ball, and the current score.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    global user1x
    global user2x
    global ballx
    global bally
    global ballvx
    global ballvy
    global user1points
    global user2points
    turtle.clear()
    turtle.up()
    turtle.goto(-50+user1x, 200)
    turtle.down()
    turtle.color("red")
    turtle.forward(70)
    turtle.up()
    turtle.goto(-50+user2x, -200)
    turtle.down()
    turtle.color("blue")
    turtle.forward(70)
    turtle.up()
    turtle.goto(ballx, bally)
    turtle.down()
    turtle.color("purple")
    turtle.dot()
    turtle.up()
    turtle.goto(220, 220)
    turtle.color("black")
    turtle.write("Pong!")
    turtle.goto(-230,220)
    turtle.write(user1points)
    turtle.goto(-220,220)
    turtle.write(user2points)
    turtle.goto(-245,230)
    turtle.write("User")
    turtle.goto(-220,230)
    turtle.write("CPU")

    # This sets up the graphics of the code.

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x.
    """
    global user1x
    user1x -= 15

    # If the user presses left, user1x goes down by -15. Paddle goes left.


def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x.
    """
    global user1x
    user1x += 15

    # If the user presses right, user1x goes up by 15. Paddle goes right.


def reset():
    """
    signature: () -> NoneType
    Reset the global variables representing
    the position and velocity of the ball and
    the position of the paddlesto their initial
    state, effectively restarting the game. The
    initial velocity of the ball should be random
    (but there there must be nonzero vertical
    velocity), but the speed of the ball should
    be the same in every game.
    """
    global user1x, user2x
    global ballvx, ballvy
    global ballx, bally
    
    user1x = 0
    user2x = 0
    ballx = 0
    bally = 0
    ballvx = random.randint(-7, 7)
    if -3 <= ballvx:
        ballvx = random.randint(-7,-4)
    elif ballvx <= 3:
        ballvx = random.randint(4, 7)
        
    ballvy = random.randint(-7, 7)
    if -4 <= ballvy:
        ballvy = random.randint(-7,-5)
    elif ballvy <= 4:
        ballvy = random.randint(5, 7)

    # Resets the game. vx is an extreme value to speed the game up.



def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by moving the computer's paddle
    to an appropriate location by updating
    the user2x variable. The computer
    paddle should move towards the ball in an
    attempt to get under it.
    """
    global user2x

    # Set speed.
    
    speed = random.randint(3, 8)

    if ballx > user2x + 7:
        user2x += speed
    elif ballx < user2x - 7:
        user2x -= speed

    # Set enemy AI.



def physics():
    """
    signature: () -> NoneType
    This function handles the physics of the game
    by updating the position and velocity of the
    ball depending on its current location. This
    function should detect if the ball has collided
    with a paddle or a wall, and if so, adjust the
    direction of the ball (as stored in the ballvx
    and ballvy variables) appropriately. If the ball
    has not collided with anything, the position of the
    ball should be updated according to its current
    velocity.
    This function should also detect if one of
    the two players has missed the ball. If so, it
    should award a point to the other player, and
    then call the reset() function to start a new
    round.
    """
    global ballx, bally
    global ballvx, ballvy
    global user1points, user2points
    global user1x
    global user2x

    # Set up the velocity for the ball.

    ballx += ballvx
    bally += ballvy

    # Player paddle
    areauser11 = user1x + 35 # Right of paddle
    areauser12 = user1x - 35 # Left of paddle

    # CPU paddle
    areauser21 = user2x + 35 # Right of paddle
    areauser22 = user2x - 35 # Left of paddle

    # Physics of the ball. If you change the physics of the ball...
    # ...the paddles will follow.

    # Set up width of screen.
    width = turtle.window_width()

    # Set up height of screen.
    height = turtle.window_height()
    
    if ballx <= -width / 2: #Left
        ballvx = -ballvx
        ballx += ballvx

    elif ballx >= width / 2: #Right
        ballvx = -ballvx
        ballx += ballvx

    # Set up edges for bounce PLAYER
    PLedgeLeft = areauser11 - 15
    PLedgeRight = areauser11 + 15

    PRedgeLeft = areauser12 - 15
    PRedgeRight = areauser12 + 15

    # Set up edges for bounce CPU
    CLedgeLeft = areauser21 - 15
    CLedgeRight = areauser21 + 15

    CRedgeLeft = areauser22 - 15
    CRedgeRight = areauser22 + 15


    
    # Set up the conditions to get a point.
    # Keep track of the angle.
    # Angle of the ball.
    # Calculate angle = ballvx * 70
    
    if (ballx <= areauser11 and ballx >= areauser12-7) and bally >= height - 340: #PLAYER
        if PRedgeLeft <= ballx <= PRedgeRight: #Right side - Go to right
            ballvy = -ballvy
            bally += ballvy
            ballvx = 7 # MUST go right
            ballx += ballvx

        elif PLedgeLeft-6 <= ballx <= PLedgeRight: #Left side - Go to left
            ballvy = -ballvy
            bally += ballvy
            ballvx = -7 # MUST go left
            ballx += ballvx

        elif user1x == ballx: #Middle - go straight
            ballvx = 0
            ballx += ballvx
            ballvy = -ballvy
            bally += ballvy
            
        else: #Everywhere else
            ballvy = -ballvy
            bally += ballvy
            ballvx = -ballvx
            ballx += ballvx

    elif bally >= height - 330:
        user2points += 1
        reset()

    if (ballx <= areauser21 and ballx >= areauser22-7) and bally <= -height + 340: #CPU
        if CRedgeLeft <= ballx <= CRedgeRight: #Right side - Go to right
            ballvy = -ballvy
            bally += ballvy
            ballvx = 7 # MUST go right
            ballx += ballvx

        elif CLedgeLeft-6 <= ballx <= CLedgeRight: #Left side - Go to left
            ballvy = -ballvy
            bally += ballvy
            ballvx = -7 # MUST go left
            ballx += ballvx

        elif user2x == ballx: #Middle - go straight
            ballvx = 0
            ballx += ballvx
            ballvy = -ballvy
            bally += ballvy
            
        else: #Everywhere else
            ballvy = -ballvy
            bally += ballvy
            ballvx = -ballvx
            ballx += ballvx

    elif bally <= -height + 330:
        user1points += 1
        reset()
        


def main():
    """
    signature: () -> NoneType
    Run the pong game. You shouldn't need to
    modify this function.
    """
    print (turtle.window_width())
    print (turtle.window_height())
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.listen()
    reset()
    while True:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()






