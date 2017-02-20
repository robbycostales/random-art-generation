from PIL import Image as Image1 
import turtle
from random import randint
import os
from datetime import datetime
from canvasvg import saveall


# this creates a list of rgb values obtained by reading every 100 pixels/

def array_of_rgb(im, xrange, yrange):
    rgb = []
    pix = im.load()
    for x in range(0,xrange,100):
        for y in range(0,yrange,100):
           rgb.append(pix[x,y])
    return rgb


# I use this list as my color pallet. Note all of the colors read appear once, 
#it is not weighted by how much a color appears. I like the randomness it creates in the art.

# this parses down the array to a list with around one of each color. 
def parse_down_array(color_list):
    rgb_list = []
    for rgb in color_list:
        if rgb not in rgb_list:
            rgb_list.append(rgb)
    return rgb_list



# this is my class art which takes care of drawing the art.

class Art:
    #color_pallet is the list of rgb values generated above. pic_size_x and pic_size_y are the sizes of the 
    #rectangular picture. The pic_size_x corresponds to the radius of the circle if the chosen shape is a circle. 
    # mode is for whether or not the picture is a circle or a rectangle and which shapes are included. it is a tuple.

    def __init__(self, color_pallet, pic_size_x, pic_size_y,mode):
        self.t = turtle.Turtle()
        self.color_list = color_pallet
        self.xbound = pic_size_x
        self.ybound = pic_size_y
        self.mode = mode

    # this function draws a square with the color, size, and starting position (x,y) specified.

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

    # this function draws a rectangle with the color, size, and starting position (x,y) specified.

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

    # this function draws a rhombus with the color, size, angle,
    #and starting position (x,y) specified.

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

    # this function draws a very very large white rectangle around the generated shapes to have the
    # final product look like a rectangle.


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

    # this function draws a very very large white circle around the generated shapes to have the
    # final product look like a circle.

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


    # this function actually draws the art.

    def draw_art(self):
        wn.tracer(0,0)
        if self.mode[1] == 2: # mode[1] = 2 draw all shapes
            for i in range(150):
                num = randint(0,3)
                size1 = randint(100,225)
                size2 = randint(100,225)
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
       
        elif self.mode[1] == 1: # mode[1] = 1 draw rhombuses only.
            for i in range(200):
                size1 = randint(10,225)
                size2 = randint(10,225)
                angle = randint(91,160)
                x_bound = randint(-(self.xbound//2),(self.xbound//2))
                y_bound = randint(-(self.ybound//2),(self.ybound//2))
                color = randint(0,(len(self.color_list)-1))
                self.draw_rhombus(self.color_list[color], x_bound, y_bound, size1, size2, angle)

        elif self.mode[1] ==0:  # mode[1] = 0 draw rectangles only.
            for i in range(200):
                size1 = randint(10,225)
                size2 = randint(10,225)
                angle = randint(91,160)
                x_bound = randint(-(self.xbound//2),(self.xbound//2))
                y_bound = randint(-(self.ybound//2),(self.ybound//2))
                color = randint(0,(len(self.color_list)-1))
                self.draw_rectangle(self.color_list[color], x_bound, y_bound, size1, size2)

        if self.mode[0] == 0:  # mode[0] = 0 draw circular perimeter
            self.clean_perimeter_circle()
       
        else: #draw rectangular perimeter
            self.clean_perimeter_rectangle()
        wn.update()




# these functions reset and hide all of the turtles so that there are no left over images from before.
def reset():
    art1.t.reset()
    art2.t.reset()
    art3.t.reset()
    art4.t.reset()
    art5.t.reset()
    art6.t.reset()
def hide():
    art1.t.hideturtle()
    art2.t.hideturtle()
    art3.t.hideturtle()
    art4.t.hideturtle()
    art5.t.hideturtle()
    art6.t.hideturtle()

# these function make the draw_art method callable by the built in turtle function onkeypress.
def draw_art1():
    reset()
    hide()
    art1.draw_art()

def draw_art2():
    reset()
    hide()
    art2.draw_art()

def draw_art3():
    reset()
    hide()
    art3.draw_art()

def draw_art4():
    reset()
    hide()
    art4.draw_art()

def draw_art5():
    reset()
    hide()
    art5.draw_art()

def draw_art6():
    reset()
    hide()
    art6.draw_art()

# this creates an html file which opens the .svg image. However most browsers can open .svg on their own.
def creat_html(filenames):
    new_filename = filenames+".svg"
    html_str ='''
    <!DOCTYPE html>
    <html>
      
      <head>
        <title>%s</title>
      </head>

      <body>
        <img src="%s" alt="%s">
      </body>

    </html>

    ''' % ("Art",new_filename,"dank memes")

    Html_file= open("art_saves/"+filenames+".html","w")
    Html_file.write(html_str)
    Html_file.close()

# this function parses down the current time so I can use it as a file name

def date_time_to_string():
    date_time = str(datetime.now())
    time_str = date_time.split(" ")
    time_str = time_str[1]
    time_str = time_str.split(".")
    time_str = "_".join(time_str)
    time_str = time_str.split(":")
    time_str = "_".join(time_str)
    return time_str

# this function saves the art generated as a .svg and includes an html file that opens the corresponding
#image.

def save_art():
    file_name = date_time_to_string()
    file_name1 = str(file_name)

    infile = "art_saves/"+file_name1
    outfile = "art_saves/"+file_name1+".png"
    
    saveall(infile+".svg", wn.getcanvas(), items=None, margin=10, tounicode=None)
    creat_html(file_name)

# this function actually runs the art generation.   

def run_art_generation():
    art1.t.write(
        "Press 1-2 for all shapes. 3-4 for rhombuses. 5-6 for rectangles."+
        " Even numbered pictures are rectangular, odd numbered pictures are circular! (esc exits) (s to save image)",
        align="center",font=("Arial", 15, "normal"))
    
    hide()

    wn.onkeypress(draw_art1, key='1') # draws all shapes in a rectangular frame
    wn.onkeypress(draw_art2, key = "2") # draws all shapes in a circular frame
    wn.onkeypress(draw_art3, key = "3") # draws rhombuses in a rectangular frame
    wn.onkeypress(draw_art4, key = "4") # draws rhombuses in a circular frame
    wn.onkeypress(draw_art5, key = "5") # draws rectangles in a rectangular frame
    wn.onkeypress(draw_art6, key = "6") # draws rectangles in a circular frame
    wn.onkeypress(exit, key = "Escape") # exits the art window and closes program
    wn.onkeypress(save_art, key = "s") # saves the current art piece as a .svg file.
    wn.listen()

if __name__ == "__main__":
    # this is the window set up.
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.colormode(255)

    # reading image size for color pallet.
    im = Image1.open("folder_of_color/read_color_pallet.png")
    im_size = im.size
    (xrange,yrange) = im_size

    # creating color pallet.
    firstpass_rgb = array_of_rgb(im, xrange, yrange)
    rgb_list = parse_down_array(firstpass_rgb)

    # I create 6 different instances of my class for the 6 different ways I generate art. 
    #(Note how mode is different for each)
    art1 = Art(rgb_list, 500,700, (1,2))
    art2 = Art(rgb_list, 500, 700, (0,2))
    art3 = Art(rgb_list, 500, 700, (1,1))
    art4 = Art(rgb_list, 500, 700, (0,1))
    art5 = Art(rgb_list, 500, 700, (1,0))
    art6 = Art(rgb_list, 800, 800, (0,0)) # here the values are larger 
    # because the rectangles were not fully filling up the circle.

    run_art_generation()

    wn.mainloop()















