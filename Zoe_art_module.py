from PIL import Image
import turtle
from random import randint


wn = turtle.Screen()
wn.colormode(255)
#wn.screensize(800, 800)
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
        if self.mode[1] == 0:
            self.t.goto(0,-(600))
            self.t.pendown()
            self.t.color((255,255,255))
            self.t.circle(600)
        else:
            self.t.goto(0,-(self.xbound+100))
            self.t.pendown()
            self.t.color((255,255,255))
            self.t.circle(self.xbound+100)


        

    def draw_art(self):
        wn.tracer(0,0)
        if self.mode[1] == 2:
            for i in range(200):
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
        elif self.mode[1] == 1:
            for i in range(200):
                size1 = randint(10,225)
                size2 = randint(10,225)
                angle = randint(91,160)
                x_bound = randint(-(self.xbound//2),(self.xbound//2))
                y_bound = randint(-(self.ybound//2),(self.ybound//2))
                color = randint(0,(len(self.color_list)-1))
                self.draw_rhombus(self.color_list[color], x_bound, y_bound, size1, size2, angle)

        elif self.mode[1] ==0:
            for i in range(200):
                size1 = randint(10,225)
                size2 = randint(10,225)
                angle = randint(91,160)
                x_bound = randint(-(self.xbound//2),(self.xbound//2))
                y_bound = randint(-(self.ybound//2),(self.ybound//2))
                color = randint(0,(len(self.color_list)-1))
                self.draw_rectangle(self.color_list[color], x_bound, y_bound, size1, size2)

        if self.mode[0] == 0:
            self.clean_perimeter_circle()
        else:
            self.clean_perimeter_rectangle()
        wn.update()





def reset_and_hide():
    art1.t.reset()
    art2.t.reset()
    art3.t.reset()
    art4.t.reset()
    art5.t.reset()
    art6.t.reset()
    art1.t.hideturtle()
    art2.t.hideturtle()
    art3.t.hideturtle()
    art4.t.hideturtle()
    art5.t.hideturtle()
    art6.t.hideturtle()


def draw_art1():
    reset_and_hide()
    art1.draw_art()

def draw_art2():
    reset_and_hide()
    art2.draw_art()

def draw_art3():
    reset_and_hide()
    art3.draw_art()

def draw_art4():
    reset_and_hide()
    art4.draw_art()

def draw_art5():
    reset_and_hide()
    art5.draw_art()

def draw_art6():
    reset_and_hide()
    art6.draw_art()
    
    

def run_art_generation():
    
    art1.t.write(
        "Press 1-2 for all shapes. 3-4 for rumbuses. 5-6 for rectangles."+
        " Even numbers pictures are rectanglular, odd numbers pictures are circular! (esc exits)",
        align="center",font=("Arial", 15, "normal"))

    wn.onkeypress(draw_art1, key='1')
    wn.onkeypress(draw_art2, key = "2")
    wn.onkeypress(draw_art3, key = "3")
    wn.onkeypress(draw_art4, key = "4")
    wn.onkeypress(draw_art5, key = "5")
    wn.onkeypress(draw_art6, key = "6")
    wn.onkeypress(exit, key = "Escape")
    wn.listen()
if __name__ == "__main__":

    art1 = Art(rgb_list, 500,700, (1,2))
    art2 = Art(rgb_list, 500, 600, (0,2))
    art3 = Art(rgb_list, 500, 700, (1,1))
    art4 = Art(rgb_list, 500, 600, (0,1))
    art5 = Art(rgb_list, 500, 700, (1,0))
    art6 = Art(rgb_list, 800, 800, (0,0))

    run_art_generation()

    wn.mainloop()















