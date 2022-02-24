import turtle

class Disk(object):
    def __init__(self, name="", xpos = 0, ypos = 0, height = 20, width = 40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        screen = turtle.getscreen()
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()

        turtle.begin_fill()
        for i in range(2):
            turtle.forward(self.dwidth / 2)
            turtle.lt(90)
            turtle.forward(self.dheight)
            turtle.lt(90)
            turtle.forward(self.dwidth / 2)
        turtle.end_fill()

    def newpos(self, xpos, ypos):
        pass

    def cleardisk(self):
        pass


if __name__ == "__main__":
    d = Disk(xpos = 100, ypos = 0)
    d.showdisk()
    while(1):
        pass
