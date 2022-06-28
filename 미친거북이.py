import turtle as t
from random import *
t.shape("circle")
t.hideturtle()
t.speed(0)
c_list = ["blue", "red", "green", "orange", "black" ,"gold"]
a_list = [90, -90]


while True:
    n = randint(0,5)
    k = randint(0,1)
    t.color(c_list[n])
    t.forward(20)
    t.right(a_list[k])
    

