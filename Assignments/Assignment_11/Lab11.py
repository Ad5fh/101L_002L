## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Inheritance
##Algorithm: The program below is used to draw a box and a circle after the thing that's going to draw it called point is setted up as the parent function. 
#################################################################################################################################


import turtle

class Point(object):
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self,x1,y1,width,height,color):
        super().__init__(x1,y1,color)
        self.width=width
        self.height=height

    def draw_action(self):
        for direction in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)

class BoxFilled(Box):
    def __init__(self,x1,y1,width,height,color,fillcolor):
        super().__init__(x1,y1,width,height,color)
        self.fillcolor=fillcolor

    def draw_action(self):
            turtle.fillcolor(self.fillcolor)
            turtle.begin_fill()
            Box.draw_action(self)
            turtle.end_fill() 

class Circle(Point):
    def __init__(self,x1,y1,radius,color):
        super().__init__(x1,y1,color)
        self.radius=radius
      
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self,x1,y1,radius,color,fillcolor):
        super().__init__(x1,y1,radius,color)
        self.fillcolor=fillcolor

    def draw_action(self):
            turtle.fillcolor(self.fillcolor)
            turtle.begin_fill()
            Circle.draw_action(self)
            turtle.end_fill() 

point=Point(-100,100,'blue')
point.draw()
box=Box(-100,100,50,20,"blue")
box.draw()
boxfilled=BoxFilled(1,2,100,200,"red","blue")
boxfilled.draw()
circle=Circle(-200,210,50,"green")
circle.draw()
circlefilled=CircleFilled(-200,210,50,"green","red")
circlefilled.draw()
turtle.done()

