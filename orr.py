import turtle

turtle.penup()
turtle.hideturtle()

SIZE_X=500
SIZE_Y=800
turtle.setup(SIZE_X, SIZE_Y)

pos_list = []
stamp_list = []
foodpos_list = []
foodstamps_list = []

food=turtle.clone()
food.goto(-230,-380)
#start

catcher = turtle.clone()
catcher.shape("square")
catcher.color('blue')
turtle_score=turtle.clone()
turtle_score.hideturtle()
n=0


START_LENGTH=4
SQUARE_SIZE = 20


catcher.goto(100,-200)
turtle_score.goto(-230,-380)
turtle_score.write('score:'+str(n),font=("Arial",30,("bold","italic")))


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
        
if pos_list in foodpos_list:
    eat_food()
    global n
    n=n+1
    turtle_score.clear()
    turtle_score.goto(-350,-240)
    turtle_score.write("score:"+str(n),font=("Arial",30,("bold","italic")) )

