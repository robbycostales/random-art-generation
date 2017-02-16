from PIL import Image
import turtle
from random import randint

wn = turtle.Screen()
wn.colormode(255)
wn.screensize(800, 800)
im = Image.open("folder_of_color/read_color_pallet.png")
im_size = im.size
(xrange,yrange) = im_size

# this creates an array of rgb values obtained by reading every 100 pixles/

def array_of_rgb(im, xrange, yrange):
    rgb = []
    pix = im.load()
    for x in range(0,xrange,100):
        rgb1 = []
        for y in range(0,yrange,100):
           rgb1.append(pix[x,y])
        rgb.append(rgb1)
    return rgb

# this parses down the array to a list with around one of each color. 
# I use this list as my color pallet.

def parse_down_array(array):
    rgb_list = []
    for i in array:
        for rgb in i:
            if rgb not in rgb_list:
                rgb_list.append(rgb)

    return rgb_list
rgb_list = parse_down_array(array_of_rgb(im, xrange, yrange))


# this is my class art which takes care of drawing the art.

class Art:
    def __init__(self, color_pallet, pic_size_x, pic_size_y,mode):
        self.t = turtle.Turtle()
        self.color_list = color_pallet
        self.xbound = pic_size_x
        self.ybound = pic_size_y
        self.mode = mode

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
            self.t.right(90)
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
        wn.tracer(100000,0)
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


art1 = Art(rgb_list,500,700,1)
art2 = Art(rgb_list, 500, 600,0)

def draw_art2():
    art1.t.reset()
    art1.t.hideturtle()
    art1.draw_art()
    

def draw_art1():
    art2.t.reset()
    art2.t.hideturtle()
    art2.draw_art()



wn.onkeypress(draw_art1, key='o')
wn.onkeypress(draw_art2, key = "r")
wn.onkeypress(exit, key = "Escape")
wn.listen()



wn.mainloop()















