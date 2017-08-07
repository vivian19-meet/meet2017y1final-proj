import turtle
import random

turtle.penup()
turtle.hideturtle()

#the size of the screen
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 600
turtle.setup(WINDOW_SIZE_X , WINDOW_SIZE_Y)

pos_list = []
stamp_list = []
foodpos_list = []
foodstamps_list = []

#the edges of the screen

UP_EDGE = WINDOW_SIZE_Y/2
DOWN_EDGE = -(WINDOW_SIZE_Y/2) 
RIGHT_EDGE = WINDOW_SIZE_X/2
LEFT_EDGE = -(WINDOW_SIZE_X/2)

#making the catcher
n=0
m=0
catcher = turtle.clone()
catcher.shape("square")
catcher.color('blue')
turtle_score=turtle.clone()
turtle_score.hideturtle()
turtle_score.goto(-(WINDOW_SIZE_X)+50,-(WINDOW_SIZE_Y+50))
turtle_score.write('score:'+str(n),font=("Arial",30,("bold","italic")))
turtle_drops = turtle.clone()
turtle_drops.hideturtle()
turtle_drops.goto(-(WINDOW_SIZE_X)+50,-(WINDOW_SIZE_Y+40))
turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))



START_LENGTH=4
SQUARE_SIZE = 20
catcher.goto(-(WINDOW_SIZE_X/2)+150,-(WINDOW_SIZE_Y/2)+90)


for i in range (START_LENGTH):
    x_pos=catcher.pos()[0]
    y_pos=catcher.pos()[1]

    x_pos=x_pos+SQUARE_SIZE

    my_pos= (x_pos, y_pos)
    catcher.goto(x_pos, y_pos)

    pos_list.append(my_pos)
    new_stamp = catcher.stamp()
    stamp_list.append(new_stamp)


RIGHT_ARROW = 'Right'
LEFT_ARROW = 'Left'
TIME_STEP = 100

RIGHT=0
LEFT=1

def right():
    global direction
    direction= RIGHT
    move_catcher()
    print('you moved right!')
    

def left():
    global direction

    direction = LEFT
    move_catcher()
    print('you moved left!')

turtle.onkeypress(right , RIGHT_ARROW)
turtle.onkeypress(left , LEFT_ARROW)
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
    my_pos=catcher.pos()
    pos_list.append(my_pos)
    new_stamp = catcher.stamp()
    stamp_list.append(new_stamp)

    old_stamp = stamp_list.pop(0)
    catcher.clearstamp(old_stamp)
    pos_list.pop(0)

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


if food.pos()[1]<= DOWN_EDGE:
    food.clearstamp()
    global m
    m=m+1
    turtle_drops.clear()
    turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))

if m == 5:
    print('game over!')
    print ('you droped 5!')
    quit()
    



    



    
