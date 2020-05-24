import turtle
'''
forward(n);backward(n);爬行
left(n);right(n);转向
penup();pendown();抬笔放笔
pensize();pencolor();笔属性
'''
t = turtle.Turtle()
'''
def drawspiral(t, lineLen):#螺旋
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawspiral(t, lineLen - 5)
    
drawspiral(t, 200)
turtle.done()
'''
def tree(brach_len):
    if brach_len > 5:
        t.forward(brach_len)
        t.right(20)
        tree(brach_len - 15)
        t.left(40)
        tree(brach_len - 15)
        t.right(20)
        t.backward(brach_len)

t = turtle.Turtle()
t.speed(1)
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(35)
#t.hideturtle()
turtle.done()
