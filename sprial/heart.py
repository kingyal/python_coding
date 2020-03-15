import turtle as t
import random as r
import time

#在min到max的范围内的随机值
def random_rang(min, max):
    return min + (max - min) * r.random()

#颜色的随机值
def random_color():
    color = (r.random(), r.random(), r.random())
    return color

#粉红色
def random_pink():
    color = (1, r.random(), 1)
    return color

#画心
def heart(r):
    factor = 180

    t.begin_fill()
    t.fillcolor(random_pink())
    t.circle(-r, factor)
    t.fd(2 * r)
    t.right(90)
    t.fd(2 * r)
    t.circle(-r ,factor)
    t.end_fill()

t.speed(10)
t.penup()
for i in range(30):
    t.hideturtle()
    t.goto(random_rang(-300, 300), random_rang(-300, 300))
    heart(random_rang(5, 30))

t.goto(-200, -200)
t.color("red") #设置笔的颜色
t.write("小仙女辛苦啦", font=('Arial', 20, 'normal'))
t.done()





