#start- Mor

import turtle
import random



#the size of the screen
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 800
turtle.setup(WINDOW_SIZE_X , WINDOW_SIZE_Y)

RIGHT_ARROW = 'Right'
LEFT_ARROW = 'Down'
TIME_STEP = 100
m=0
turtle_drops = turtle.clone()
turtle_drops.hideturtle()
turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))


#the edges of the screen
direction= UP
UP_EDGE = 500
DOWN_EDGE = -500
RIGHT_EDGE = 800
LEFT_EDGE = -800


def right():
    global direction
    direction= RIGHT
    print('you moved right!')
    

def left():
    global direction
    direction = LEFT
    print('you moved left!')

turtle.onkeypress(right , RIGHT_ARROW)
turtle.onkeypress(left . LEFT_ARROW)


#food touch the down edge
food.pos() = foodpos_list[]

#drop_count = #the turtle need to count how many times the food drop

    
##if drop_count < 5:
##    print('drop_count')
##else:
##    print('you missed 5 foods')
##    quit()
##        

if foodpos_list >= DOWN_EDGE:
    food.clearstamp()
    global m
    m=m+1
    turtle_drops.clear()
    turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))

if m == 5:
    print('game over!')
    print ('you droped 5!')
    quit()
    



#end-Mor
