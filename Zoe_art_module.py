from PIL import Image
import turtle
from random import randint

wn = turtle.Screen()
wn.colormode(255)
im = Image.open("noice.png")
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


def parse_down_array(array):
    rgb_list = []
    for i in array:
        for rgb in i:
            if rgb not in rgb_list:
                rgb_list.append(rgb)

    return rgb_list
rgb_list = parse_down_array(array_of_rgb(im, xrange, yrange))




class Art:
    def __init__(self, color_pallet, pic_size_x, pic_size_y):
        self.t = turtle.Turtle()
        self.color_list = color_pallet
        self.xbound = pic_size_x
        self.ybound = pic_size_y
        self.mode = int(input
        ("enter 1 for rectangular mode and 0 for circular mode."""
            "(in circle mode the pic_size_x is the radius y does not matter):   "))

    def draw_square(self, color, startx, starty, size):
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

    def draw_rectangle(self, color, startx, starty, size1, size2):
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

    def draw_rhombus(self, color, startx, starty, size1, size2, angle):
        self.t.hideturtle()
        self.t.speed(0)
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

    def clean_perimeter_rectangle(self):
        self.t.setheading(0)
        self.t.pensize(450)
        self.t.penup()
        self.t.speed(0)
        self.t.goto(-((self.xbound//2)+225),-((self.ybound//2)+225))
        self.t.pendown()
        self.t.color((255,255,255))
        for i in range(2):
            self.t.forward(self.xbound+450)
            self.t.right(-90)
            self.t.forward(self.ybound+450)
            self.t.right(-90)

    def clean_perimeter_circle(self):
        self.t.setheading(0)
        self.t.pensize(450)
        self.t.penup()
        self.t.speed(0)
        self.t.goto(0,-(self.xbound+100))
        self.t.pendown()
        self.t.color((255,255,255))
        self.t.circle(self.xbound+100)

    def draw_art(self):
        wn.tracer(1000,0)
        for i in range(500):
            num = randint(0,3)
            size1 = randint(10,225)
            size2 = randint(10,225)
            angle = randint(91,160)
            x_bound = randint(-(self.xbound//2),(self.xbound//2))
            y_bound = randint(-(self.ybound//2),(self.ybound//2))
            color = randint(0,(len(self.color_list)-1))
            if num == 0:
                self.draw_rhombus(self.color_list[color], x_bound, y_bound, size1, size2, angle)
            if num == 1:
                self.draw_rectangle(self.color_list[color], x_bound, y_bound, size1, size2)
            if num == 2:
                self.draw_square(self.color_list[color], x_bound, y_bound,size2)
        if self.mode == 0:
            self.clean_perimeter_circle()
        else:
            self.clean_perimeter_rectangle()
        wn.update()
        print("done")


art = Art(rgb_list,500,700)


art.draw_art()


wn.mainloop()