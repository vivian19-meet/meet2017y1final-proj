import turtle
import time
import random

WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 600
turtle.setup(WINDOW_SIZE_X,WINDOW_SIZE_Y)
turtle.bgpic('sea1.gif')
turtle.penup()
SQUARE_SIZE = 20
food_list = []
stamp_list = []
turtle.hideturtle()
food = turtle.clone()
food.shape('circle')

def make_food():
    #for i in range(1):
    min_x=-int(WINDOW_SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(WINDOW_SIZE_X/2/SQUARE_SIZE)-1
    min_y=int((WINDOW_SIZE_Y/2-50)/SQUARE_SIZE)+1
    max_y=int(WINDOW_SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food_list.append((food_x,food_y))
    food.goto(food_x,food_y)
    stamp1 = food.stamp()
    stamp_list.append(stamp1)





#stamp_list=[]
#food_stamps=[]
#food_x=int(30)
#food_y=int(270)
#food.penup()
#food.goto(food_x,food_y)

def move_food():
    for food.pos in food_list:
        pos_x =food.pos[0]
        pos_y =food.pos[1]
        pos_y = pos_y-SQUARE_SIZE
        food.goto(pos_x,pos_y)
        food_ind= food_list.index(food.pos)
        food_list.append((pos_x,pos_y))
        stamp_ID=stamp_list[food_ind]

        food.clearstamp(stamp_ID)
        foodmove=food.stamp()
        stamp_list.append(foodmove)
        oldfood=food_list.pop(0)
        stamp_list.pop(0)

    turtle.ontimer(move_food,80)
make_food()
move_food()






  
