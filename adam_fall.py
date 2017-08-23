import turtle
import random
width = 800
height = 600
unitsize = 20
turtle.tracer(1,0)
turtle.setup(width,height)
turtle.hideturtle()
turtle.penup()



food_list = []
step = 25
bottom = -height/2 + 100
turtle.register_shape('food-chicken.gif')
def create_food():
    y_pos = height/2 - 50
    min_x = -int(width/2/unitsize)+1
    max_x = int(width/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    food = turtle.clone()
    food.shape('food-chicken.gif')
    food.goto(x_pos,y_pos)
    food.showturtle()
    food_list.append(food)
food_delay = 0
delay_num = 7
def falling_food():
    global food_delay
    food_destroy = []
    for food in food_list:
        x_pos = food.pos()[0]
        y_pos = food.pos()[1]
        if y_pos >= bottom:
            y_pos = y_pos - step
            food.goto(x_pos,y_pos)
        else:
            ind = food_list.index(food)
            food_destroy.append(ind)

    for ind in food_destroy:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
    if food_delay <= delay_num:
        food_delay += 1
    else:
        food_delay = 0
        create_food()
    turtle.ontimer(falling_food,100)

falling_food()
    
