from PIL import Image
import turtle
from random import randint
wn = turtle.Screen()
wn.colormode(255)
im = Image.open("read_color_pallet.png")
im_size = im.size
(xrange,yrange) = im_size

def array_of_rgb(im, xrange, yrange):
    rgb = []
    pix = im.load()
    for x in range(0,xrange,100):
        rgb1 = []
        for y in range(0,yrange,100):
           rgb1.append(pix[x,y])
        rgb.append(rgb1)
    return rgb


def parc_down_array(array):
    rgb_list = []
    for i in array:
        for rgb in i:
            if rgb not in rgb_list:
                rgb_list.append(rgb)
    return rgb_list
rgb_list = parc_down_array(array_of_rgb(im, xrange, yrange))




class Art:
    def __init__(self,color_pallet,pic_size_x,pic_size_y):
        self.t = turtle.Turtle()
        self.color_list = color_pallet
        self.xbound = pic_size_x
        self.ybound = pic_size_y

    def draw_square(self,color,startx,starty,size):
        self.t.speed(0)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.penup()
        self.t.goto(startx,starty)
        self.t.pendown()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(size)
            self.t.right(90)
        self.t.end_fill()

    def draw_rectangle(self,color,startx,starty,size1,size2):
        self.t.speed(0)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.penup()
        self.t.goto(startx,starty)
        self.t.pendown()
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(size1)
            self.t.right(90)
            self.t.forward(size2)
        self.t.end_fill()

    def draw_rumbus(self,color, startx, starty, size1,size2,angle):
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(startx,starty)
        self.t.pendown()
        self.t.color(color)
        self.t.begin_fill()
        self.t.forward(size1)
        self.t.right(angle)
        self.t.forward(size2)
        self.t.right(180-angle)
        self.t.forward((size1))
        self.t.right(angle)
        self.t.forward(size2)
        self.t.end_fill()

    def clean_perimeter(self):
        self.t.setheading(0)
        self.t.pensize(400)
        self.t.penup()
        self.t.speed(0)
        self.t.goto(-((self.xbound//2)+200),-((self.ybound//2)+200))
        self.t.pendown()
        self.t.color((255,255,255))
        for i in range(2):
            self.t.forward(self.xbound+400)
            self.t.right(-90)
            self.t.forward(self.ybound+400)
            self.t.right(-90)

    def draw_art(self):
        for i in range(10):
            for color in range(len(self.color_list)):
                num = randint(0,3)
                size1 = randint(50,150)
                size2 = randint(50,150)
                angle = randint(95,160)
                x_bound = randint(-(self.xbound//2),(self.xbound//2))
                y_bound = randint(-(self.ybound//2),(self.ybound//2))
                if num == 0:
                    self.draw_rumbus(self.color_list[color],x_bound,y_bound,size1,size2,angle)
                if num == 1:
                    self.draw_rectangle(self.color_list[color],x_bound,y_bound,size1,size2)
                if num == 2:
                    self.draw_square(self.color_list[color],x_bound,y_bound,size2)
        self.clean_perimeter()
        print("done")


art = Art(rgb_list,400,500)
# art.draw_rumbus(rgb_list[0],0,0,60,80,120)

art.draw_art()



wn.mainloop()