# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_vel = [1,1]
ball_pos = [WIDTH/2,HEIGHT/2]
paddle1_pos = [0,0]
paddle2_pos = [0,0]
paddle1_vel = [0,0]
paddle2_vel = [0,0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel,  RIGHT, LEFT # these are vectors stored as lists
    
    if direction == RIGHT:
        ball_pos = [WIDTH/2,HEIGHT/2]
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 5)
    
    if direction == LEFT:
        ball_pos = [WIDTH/2,HEIGHT/2]
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 5)
        
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel, paddle2_vel
    
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   
    
    if (ball_pos[0] >= 572 ):
        ball_vel[0]=  -ball_vel[0]
        
        
          
    if (ball_pos[0] <= 28):
        ball_vel[0] = -ball_vel[0]
       
        
    if (ball_pos[1] <= 20):
         ball_vel[1]=  -ball_vel[1]
           
        
    if (ball_pos[1] >= 380):    
        ball_vel[1]=  -ball_vel[1]
        
        
        
        
    # collision with the gutter
    
    if ball_pos[0] <= 28:
        if ((paddle1_pos[1] + 160) < ball_pos[1]) and ((paddle1_pos[1] + 240) > ball_pos[1]):
            score2 = score2
            
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
            
    if ball_pos[0] >= 572:
        if ((paddle2_pos[1] + 160) < ball_pos[1]) and ((paddle2_pos[1] + 240) > ball_pos[1]):
            score1 = score1
            
        else:
            score1 += 1
            spawn_ball(LEFT)
  
  
      
            
    # draw ball
    canvas.draw_circle(ball_pos, 20, 1, 'Blue', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos[1] < -160):
        paddle1_pos[1] = -160 
        
    elif(paddle1_pos[1] >160):
        paddle1_pos[1] = 160
                    
    else:
        paddle1_pos[1] += paddle1_vel[1]
    
    
    if (paddle2_pos[1] < -160):
        paddle2_pos[1] = -160 
        
    elif(paddle2_pos[1] >160):
        paddle2_pos[1] = 160
                    
    else:
        paddle2_pos[1] += paddle2_vel[1]
    
    
    
    # draw paddles
    canvas.draw_line([0,160 + paddle1_pos[1]],[0,240 + paddle1_pos[1]],14,"Yellow")
    canvas.draw_line([600,160 +paddle2_pos[1]],[600,240 + paddle2_pos[1]],14,"Yellow")
    
    # determine whether paddle and ball collide 
    
    
    # draw scores
    canvas.draw_text(str(score1) , [200,100],40,"Red")
    canvas.draw_text(str(score2) , [380,100],40,"Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    v = 4
    
    if (key == simplegui.KEY_MAP["s"]):
        paddle1_vel[1] += v
        
    if (key == simplegui.KEY_MAP["w"]):
        paddle1_vel[1] -= v    
        
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_vel[1] -= v
        
    if (key == simplegui.KEY_MAP["down"]):
        paddle2_vel[1] += v 

   
def keyup(key):
    global paddle1_vel, paddle2_vel
    v=4
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] -= v
        
    if (key == simplegui.KEY_MAP["w"]):
        paddle1_vel[1] += v    
        
    if (key == simplegui.KEY_MAP["up"]):
        paddle2_vel[1] += v
        
    if (key == simplegui.KEY_MAP["down"]):
        paddle2_vel[1] -= v 

def restart():
    global score1, score2
    score1 = 0
    score2 = 0
    
   
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
b1 = frame.add_button("RESTART",restart,100)


# start frame
new_game()
frame.start()
