import random
from turtle import Turtle, Screen
colors = ["red", "yellow", "orange", "blue", "green", "purple"]




screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race ? enter a color ")
# y_axis = -70
y_axis =[-70, -40, -10, 80, 50, 20]
turtle_list = []
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_axis[index])
    turtle_list.append(new_turtle)

if user_bet:
    start_game = True

while start_game:
    for turtle_ in turtle_list:
        if turtle_.xcor() > 240:
            start_game = False
            winning_color = turtle_.pencolor()

            if winning_color == user_bet:
                print(f"Hurray!!! You Won... The {winning_color} turtle is the winner")
            else:
                print(f"You lost The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle_.forward(random_distance)




    # y_axis += 30


screen.exitonclick()

