from tkinter import *
from random import *

root = Tk()
X_OFFSET = 20
Y_OFFSET = 40
class Recta:
    X_OFFSET = 20
    Y_OFFSET = 40
    def __init__(self, height, width):
        self.height=80
        self.width=100


    def randomRects(self,canvas):
        for i in range(20):
            color = ['medium violet red', 'DarkGoldenrod2', 'black']
            root["bg"] = "grey"
            for i in range (58):
                def rect(x0,y0, x1,y1, steps=20, rotation=0):
                    tes = Recta(10, 20)
                w = 5
                h = 9
                x0 =4
                y0 = 20
                # w = random.randrange(10, 50, 2)
                # h = random.randrange(80, 90, 5)
                # x0 = random.randrange(2, 10, 2)
                # y0 = random.randrange(3, 80, 5)
                x = randrange(int(self['width']) - self.X_OFFSET)
                y = randrange(int(self['height']) - self.Y_OFFSET)
                points = [(x0 + randrange(self.X_OFFSET), y0 + randrange(self.Y_OFFSET))
                          for i in range(15)]
                canvas.create_rectangle(points,h,w,fill=random.choice(color))

c = Canvas(root)
c.pack()

tes = Recta(10,50)
tes.randomRects(c)

root.mainloop()