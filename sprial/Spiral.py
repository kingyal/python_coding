#导入turtle图形库
import turtle
#调用图形库
t = turtle.Pen()

###########1.方形旋转###########
#每次画线的速度
t.speed(0)
#线条的宽度
t.width(1)
#线条颜色,颜色可用英语表示，也可用颜色代码“#ff00ff”表示
t.color("red")
#循环次数
for x in range(50):
    #画直线
    t.forward(2 * x)
    #转动方向
    t.right(121)
    
###########2.圆形旋转###########
#每次画线的速度
t.speed(0)
#线条的宽度
t.width(1)
#线条颜色,颜色可用英语表示，也可用颜色代码“#ff00ff”表示
t.color("gold")
#循环次数
for x in range(50):
    #画直线
    t.circle(2 * x)
    #转动方向
    t.right(90)

###########3.增加颜色###########
#每次画线的速度
t.speed(0)
#线条的宽度
t.width(1)
#设置背景颜色
turtle.bgcolor("black")
#设置线条颜色,颜色可用英语表示，也可用颜色代码“#ff00ff”表示
colors = ['blue','yellow', 'red', 'green']
#循环次数
for x in range(50):
    #设置线条颜色
    t.color(colors[x%4])
    #画直线
    t.forward(2 * x)
    #转动方向
    t.right(90)




    








    
