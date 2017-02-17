# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

num_range = 100
counter = 7
my_num = random.randrange(0,100) 
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range, counter
    print ""
    print "New game, Range is from 0 to ",num_range
    print "Number of remaining guesses is ", counter
    print ""
    
# define event handlers for control panel
def range100():
    
    global counter,num_range,my_num
    num_range=100
    my_num=random.randrange(0,100)
    counter = 7
    new_game()
   
def range1000():
    global counter,num_range,my_num
    my_num =random.randrange(0,1000)
    num_range = 1000
    counter = 10
    new_game()
    
   
    
    
def input_guess(guess):
        
        global counter
        global my_num,num_range
        inp =int (guess)
        print "Guess was",inp
    
        if inp>my_num:
            print "Higher!"
        elif inp<my_num:
            print "Lower!"
        else:
            print "Correct!"
            counter = 7
            num_range = 100
            new_game()   
            
            
        counter = counter - 1
        if counter ==  0:
            print "Game over!!!"
            print "You ran out of guesses,Answer was",my_num
            print""
            counter = 7
            num_range =100
            new_game()
        else:    
            print "Number of remaining guesses is ", counter
            print ""    
        return
       
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)

f.add_button("Range is [0,100]",range100,200)
f.add_button("Range is [0,1000]",range1000,200)
f.add_input("Enter a guess:",input_guess,200)	
# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
