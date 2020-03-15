#导入turtle图形库
import turtle
#调用图形库
t = turtle.Pen()
#每次画线的速度
t.speed(0)

#设置背景颜色
turtle.bgcolor("black")
#设置线条颜色,颜色可用英语表示，也可用颜色代码“#ff00ff”表示
colors = ['blue','yellow', 'red', 'green', 'orange', 'purple']
sides = int(input('请输入边数：\n'))

#循环次数
for x in range(25):
    #线条的宽度
    t.width(x)
    #设置线条颜色
    t.color('red')
    #画直线
    t.circle(x)
    #转动方向
    t.left((360 / sides))
