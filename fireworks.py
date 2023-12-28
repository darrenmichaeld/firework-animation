
# Darren Michael Dimanto Polo, Student Id: 20895475
# fireworks

import random   # module providing the randint function
import time     # time module to delay after drawing five fireworks
import turtle   # turtle module for drawing fireworks
import playsound

#### Initialize variables used in the program

# The following width and height match the GIF used by the program
screen_width, screen_height = 900, 564

firework_radius = 100   # The maximum radius a firework can have
firework_count = 30     # The number of fireworks to shoot

# A list of colours to choose from for a firework
firework_colours = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]


#### Initialize the turtle module

turtle.setup(screen_width, screen_height)   # Set the size of the screen
turtle.bgpic("hong_kong.gif")               # Put the background image on the
turtle.speed(0)                                            # screen
turtle.hideturtle()
turtle.width(3)                             # Draw lines with a width of three
turtle.shape("circle")                      # Set the turtle to be bomb shape
turtle.color("red")                         # Set the turtle color to red
turtle.up()
#### For loop to shoot individual firework


for i in range(firework_count):
    # Clear the sky (screen) for every five fireworks
    if i > 0 and i % 5 == 0:
        time.sleep(1)
        turtle.clear()
        
    #### Add your code here
    # Initialize a starting position
   
    xstartpos = random.randint(-(screen_width/2),(screen_width/2))
    ystartpos = -(screen_width/2)
    xstartpos= int(xstartpos)
    ystartpos = int(ystartpos)
    turtle.up()
    turtle.goto(xstartpos, ystartpos)
    turtle.down()
   
    
    # Initialize a destination
    xdest = random.randint(-screen_width/2,screen_width/2)
    ydest = random.randint(0, screen_height/2)
    xdest = int(xdest)
    ydest = int(ydest)
    # Shoot a firework from the start to the destination
    turtle.showturtle()
    turtle.speed(9)
    turtle.color("red")
    turtle.up()
    turtle.goto(xdest,ydest)
    turtle.down()
    #### The turtle is in the sky, explode the firework
    #### Add your code here
    # Pick a firework color from the firework colour list
    thecolor = firework_colours[random.randint(0,6)]
    turtle.color(thecolor)
    turtle.fillcolor(thecolor)
    
    
    # Pick a size for the firework
    theradius = random.randint(firework_radius/2,firework_radius)
  
    
    # Pick the number of explosion directions
    theexp= random.randint(10,20)
    
    #### For loop to draw each ring of explosion
    #### Add your code here
    playsound.play("explosion.wav")
    turtle.up()
    turtle.hideturtle()
    dotsize = 1
    for theradius in range(10,theradius,10):
        turtle.tracer(False)
        turtle.setheading(90)
        turtle.backward(5)
        turtle.setheading(0)
        turtle.forward(theradius)
        turtle.left(90)
        dotsize = dotsize + 0.6
        for thedirection in range(theexp):
            radiusdot = 0
            turtle.dot(dotsize)
            turtle.circle(theradius, 360/theexp)
        turtle.left(90)
        turtle.forward(theradius)
        turtle.tracer(True)
turtle.done() # Need to keep the window display up
