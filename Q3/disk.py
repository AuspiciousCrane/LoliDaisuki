import turtle

class Disk(object):
    def __init__(self, name="", xpos = 0, ypos = 0, height = 20, width = 40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        

    def showdisk(self):
        #screen = self.rect.getscreen()
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()

        for i in range(2):
            turtle.forward(self.dwidth / 2)
            turtle.lt(90)
            turtle.forward(self.dheight)
            turtle.lt(90)
            turtle.forward(self.dwidth / 2)


    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos


    def cleardisk(self):
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.color("white","white")
        
        for i in range(2):
            turtle.forward(self.dwidth / 2)
            turtle.lt(90)
            turtle.forward(self.dheight)
            turtle.lt(90)
            turtle.forward(self.dwidth / 2)

        turtle.color("black","white")
        


