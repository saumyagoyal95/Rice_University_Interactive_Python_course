# template for "Stopwatch: The Game"
import simplegui

# define global variables
x = 0
y = 0
z = str(y)+ "/" + str(x) 
t=0
m=0
s1=0
s2= 0
p = str(m) + ":" +  str(s1) + str(s2) + "." + str(t)
running = False   


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format():
    global t,s1,s2,m,p,k
    
   
    p = str(m) + ":" +  str(s1) + str(s2) + "." + str(t)
    t = t+1
    k = False
    if t == 10:
        t = 0
      
        s2 = s2 + 1
      
       
        if s2 == 10 :
            s2 = 0
            t  = 0
            k = True
            s1 = s1 + 1
        
            
            if s1 == 6 :
             
                m = m + 1
                s1 = 0
                s2 = 0
                t = 0
              
# define event handlers for buttons; "Start", "Stop", "Reset"

def func_start():
    global running
    timer.start()
    running = True

def func_stop():
    global t,x,y,z,k,running
    timer.stop()
    
    if running == True:
            x = x + 1
            running = False
    
    if t==1:
        y = y + 1
        
    z =str(y)+ "/" + str(x)     
        
    
def func_reset():
    
    timer.stop()
    global t, s1,s2,m,p,x,y,z
    t = 0
    s1= 0
    s2 = 0
    m = 0
    p = str(m) + ":" +  str(s1) + str(s2) + "." + str(t)
    x = 0
    y = 0
    z =str(y)+ "/" + str(x) 
    
    
# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100,format)

# define draw handler

def draw_sthing(canvas):
    global p,z
    canvas.draw_text(str(p), [100,100], 50 , "White")
    canvas.draw_text(str(z), [200,30], 40, "Green")

    
# create frame
                               
frame = simplegui.create_frame("Stopwatch",300,200)

# register event handlers

frame.set_draw_handler(draw_sthing)
b1 = frame.add_button("Start", func_start,100)
b2 = frame.add_button("Stop", func_stop,100)
b3 = frame.add_button("Reset", func_reset,100)
                               
# start frame
                               
frame.start()


# Please remember to review the grading rubric
