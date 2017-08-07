import turtle
import time

food=turtle.clone()
food.shape('circle')
turtle.hideturtle()
stamp_list=[]
food_stamps=[]
food_x=int(30)
food_y=int(270)
food.penup()
food.goto(food_x,food_y)

def move_food():
    global food_y,food_x
    food.goto(food_x,food_y-20)
    food_y=food_y-20
    turtle.ontimer(move_food,50)
move_food()


