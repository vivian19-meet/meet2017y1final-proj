#start- Mor

import turtle
import random

turtle.hideturtle()

#the size of the screen
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 600
turtle.setup(WINDOW_SIZE_X , WINDOW_SIZE_Y)

RIGHT_ARROW = 'Right'
LEFT_ARROW = 'Left'
TIME_STEP = 100
m=0
turtle_drops = turtle.clone()
turtle_drops.hideturtle()
turtle_drops.penup()
turtle_drops.goto(-WINDOW_SIZE_X/2 + 10, WINDOW_SIZE_Y/2-50)
turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))

catcher = turtle.clone()
catcher.shape("square")
catcher.color('blue')

n=0


START_LENGTH=4
SQUARE_SIZE = 20


catcher.goto(100,-200)


RIGHT=0
LEFT=1

#the edges of the screen
<<<<<<< HEAD:mor- direction.py
direction= RIGHT
UP_EDGE = WINDOW_SIZE_Y/2
DOWN_EDGE = -(WINDOW_SIZE_Y/2)
RIGHT_EDGE = WINDOW_SIZE_X/2
LEFT_EDGE = -(WINDOW_SIZE_X/2)
=======

UP_EDGE = 500
DOWN_EDGE = -500
RIGHT_EDGE = 800
LEFT_EDGE = -800
>>>>>>> ed5fc8f87a27bdd0ca7363e275d3214b09a0b25b:mor.py


    
def right():
    global direction
    direction= RIGHT
    move_catcher()
    print('you moved right!')
    

def left():
    global direction

    direction = LEFT
    move_catcher
    print('you moved left!')

turtle.onkeypress(right , RIGHT_ARROW)
turtle.onkeypress(left , LEFT_ARROW)
<<<<<<< HEAD:mor- direction.py
turtle.listen()

def move_catcher():
    global direction
    my_pos = catcher.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        catcher.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    
    elif direction==LEFT:
        catcher.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")


for i in range (START_LENGTH):
    x_pos=catcher.pos()[0]
    y_pos=catcher.pos()[1]

    x_pos=x_pos+SQUARE_SIZE

    my_pos= (x_pos, y_pos)
    catcher.goto(x_pos, y_pos)

    pos_list.append(my_pos)
    new_stamp = catcher.stamp()
    stamp_list.append(new_stamp)


def eat_food():
    
    food_ind=food_pos.index(snake.pos())
    food.clearstamp(food_stamps[food_ind])
    food_pos.pop(food_ind)
    food_stamps.pop(food_ind)           
#needs to be in move food        
if pos_list in foodpos_list:
    eat_food()
    global n
    n=n+1
    turtle_score.clear()
    turtle_score.goto(-350,-240)
    turtle_score.write("score:"+str(n),font=("Arial",30,("bold","italic")) )






=======


#food touch the down edge
food = turtle.clone()
foodpos = food.pos() 
>>>>>>> ed5fc8f87a27bdd0ca7363e275d3214b09a0b25b:mor.py

#drop_count = #the turtle need to count how many times the food drop

    
##if drop_count < 5:
##    print('drop_count')
##else:
##    print('you missed 5 foods')
##    quit()
##        

<<<<<<< HEAD:mor- direction.py
if food.pos()[1]<= DOWN_EDGE:
=======
if foodpos[1] <= DOWN_EDGE:
>>>>>>> ed5fc8f87a27bdd0ca7363e275d3214b09a0b25b:mor.py
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
