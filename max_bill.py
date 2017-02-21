import turtle
import random
import time

c_size = 400  # Is the length of "radius" of rotated square

wn = turtle.Screen()
wn.tracer(0, 0)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()        # 1-4 are dark colored turtles
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()        # 5-8 are the matching bright colored turtles

TList = [t1, t2, t3, t4, t5, t6, t7, t8]

for i in [t1, t2, t3, t4, t5, t6, t7, t8]:
    i.ht()
    i.speed(0)

bg = turtle.Turtle()    # bg color turtle
bg.shape("square")
bg.turtlesize(80)
bg.ht()
bg.penup()
bg.speed(0)

fr = turtle.Turtle()      # framing turtle
fr.shape("circle")
fr.color("DarkGray")
fr.penup()
fr.ht()
fr.speed(0)


def draw_rectangle(t, height, width):    # draws a rectangle at tip of turtle
    t.penup()
    t.right(90)
    t.backward(width / 2)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(width / 2)
    t.left(90)


class MaxBill(object):
    def __init__(self):
        self.type = random.choice(["S45SmRect", "S45DiagRect", "TiltSquare"])
        self.bright_c = random.sample(["yellow", "crimson", "lime", "coral", "DeepSkyBlue", "magenta", "white"], 4)
        random.shuffle(self.bright_c)
        self.dark_c = random.sample(["steel blue", "LimeGreen", "gold", "red", "DarkOrange", "purple", "black"], 4)
        random.shuffle(self.dark_c)
        self.bg = ["yellow", "crimson", "lime", "coral", "DeepSkyBlue", "magenta", "steel blue",
                                 "LimeGreen", "gold", "red", "DarkOrange", "purple"]
        random.shuffle(self.bg)
        self.b_w = random.choice(["black", "white"])

    def create_painting(self):
        for i in TList:
            i.setpos(0,0)
            i.setheading(0)
        fr.setheading(0)
        bg.st()
        bg.color(self.bg[0])   # Sets bg color
        bg.pendown()
        bg.stamp()         # Creates background color from random choice of the self.bg list
        bg.ht()
        if self.type == "S45SmRect":       # 45 degree square with rectangles inside tips
            c_scheme = random.choice(["4Sym", "2Sym", "NoSym"])     # Chooses color scheme
            if c_scheme == "4Sym":
                for i in [t1, t2, t3, t4]:
                    i.color(self.dark_c[0])
                for i in [t5, t6, t7, t8]:
                    i.color(self.bright_c[0])
            elif c_scheme == "2Sym":
                for i in [t1, t3]:
                    i.color(self.dark_c[0])
                for i in [t2, t4]:
                    i.color(self.dark_c[1])
                for i in [t5, t7]:
                    i.color(self.bright_c[0])
                for i in [t6, t8]:
                    i.color(self.bright_c[1])
            elif c_scheme == "NoSym":
                for i in range(4):
                    TList[i].color(self.dark_c[i])
                for i in range(4):
                    TList[i+4].color(self.bright_c[i])
            else:
                print("color scheme error")

            t1.setheading(0)
            t5.setheading(0)
            t2.setheading(90)
            t6.setheading(90)
            t3.setheading(180)
            t7.setheading(180)
            t4.setheading(270)
            t8.setheading(270)

            if random.choice([1, 2]) == 1:
                bar_1 = random.randint(c_size//2, int(c_size*(2/3)))
                bar_2 = random.randint(int(c_size*(2/3)), int(c_size*(7/8)))
                for i in ([(t1, t5), (t2, t6), (t3, t7), (t4, t8)]):
                    i[0].penup()
                    i[1].penup()
                    i[0].forward(random.choice([c_size/2, bar_1, bar_1]))
                    i[1].forward(bar_2)
                    draw_rectangle(i[0], c_size, c_size)
                    draw_rectangle(i[1], c_size, c_size)
            else:
                bar_1 = random.randint(c_size // 2, int(c_size * (2 / 3)))
                bar_2 = random.randint(int(c_size * (2 / 3)), int(c_size * (7 / 8)))
                bar_1a = random.randint(c_size // 2, int(c_size * (2 / 3)))
                bar_2a = random.randint(int(c_size * (2 / 3)), int(c_size * (7 / 8)))
                for i in ([(t1, t5), (t2, t6), (t3, t7), (t4, t8)]):
                    i[0].penup()
                    i[1].penup()
                    i[0].forward(random.choice([c_size / 2, bar_1, bar_1a]))
                    i[1].forward(random.choice([bar_2a, bar_2]))
                    draw_rectangle(i[0], c_size, c_size)
                    draw_rectangle(i[1], c_size, c_size)

        elif self.type == "S45DiagRect":
            c_scheme = random.choice([1, 2])  # Chooses color scheme

            angle = random.randint(-8, 8)
            big_slant_rect = random.randint(1, c_size // 2)
            no_slant_rect = big_slant_rect - random.randint(10, 20)
            lil_slant_rect = no_slant_rect - random.randint(10, 30)

            if c_scheme == 2:
                t1.setpos(0, 0)
                t1.setheading(0)
                t1.color(self.bg[1])
                draw_rectangle(t1, c_size*2, c_size*2)

            t2.penup()
            t2.setpos(0, 0)
            t2.setheading(90+angle)
            t2.color(self.bright_c[0])
            draw_rectangle(t2, c_size * 2, big_slant_rect)
            t2.right(180)
            draw_rectangle(t2, c_size * 2, big_slant_rect)

            t3.penup()
            t3.setpos(0, -c_size-10)
            t3.setheading(90)
            t3.color(self.dark_c[0])
            draw_rectangle(t3, c_size * 3, no_slant_rect)

            t4.penup()
            t4.setpos(0, 0)
            t4.setheading(90 + angle)
            t4.color(self.bright_c[1])
            draw_rectangle(t4, c_size * 2, lil_slant_rect)
            t4.right(180)
            draw_rectangle(t4, c_size * 2, lil_slant_rect)

        elif self.type == "TiltSquare":  # ## WORK IN PROGRESS ## #
            bg.st()
            bg.color(self.bright_c[0])  # Sets bg color
            bg.pendown()
            bg.stamp()  # Creates background color from random choice of the self.bg list
            bg.ht()
            t1.color(self.dark_c[0])
            t1.penup()
            t1.setheading(random.randint(10, 340))
            t1.backward(random.randint(-250, c_size*1.5))
            draw_rectangle(t1, random.randint(c_size//1.5, int(c_size*1.8)), random.randint(c_size//1.5, int(c_size*1.8)))

        elif self.type == "Checker":  # ## WORK IN PROGRESS ## #
            if random.choice(["hor", "ver"]) == "hor":
                t1.setpos(-(2**(1/2))*c_size/2, (2**(1/2)*3*c_size/8))
                t2.setpos(-(2 ** (1 / 2)) * c_size / 2, (2 ** (1 / 2) * 3 * c_size / 8))
                t3.setpos(-(2 ** (1 / 2)) * c_size / 2, (2 ** (1 / 2) * 3 * c_size / 8))
                t4.setpos(-(2 ** (1 / 2)) * c_size / 2, (2 ** (1 / 2) * 3 * c_size / 8))

            bg.st()
            bg.color(self.bright_c[0])  # Sets bg color
            bg.pendown()
            bg.stamp()  # Creates background color from random choice of the self.bg list
            bg.ht()
            t1.color(self.dark_c[0])
            t1.penup()
            t1.setheading(random.randint(10, 340))
            t1.backward(random.randint(-250, c_size*1.5))
            draw_rectangle(t1, random.randint(c_size//1.5, int(c_size*1.8)), random.randint(c_size//1.5, int(c_size*1.8)))

        else:
            print("type error")

        if self.type != "Checker":
            fr.setheading(0)
            fr.forward(c_size)
            fr.left(135)
            fr.pendown()
            for i in range(4):
                fr.forward(c_size*(2**(1/2)))
                fr.left(90)
            fr.penup()
            fr.setpos(0, 0)
            fr.setheading(45)
            for i in range(4):
                fr.forward(c_size/2*(2**(1/2)))
                draw_rectangle(fr, 1200, 1200)
                fr.backward(c_size/2*(2**(1/2)))
                fr.left(90)
            fr.penup()

        else:
            fr.setheading(0)
            fr.right(45)
            fr.forward(c_size)
            fr.left(135)
            fr.pendown()
            for i in range(4):
                fr.forward(c_size*(2**(1/2)))
                fr.left(90)
            fr.penup()
            fr.setpos(0, 0)
            fr.setheading(45)
            for i in range(4):
                fr.forward(c_size/2*(2**(1/2)))
                draw_rectangle(fr, 1200, 1200)
                fr.backward(c_size/2*(2**(1/2)))
                fr.left(90)
            fr.penup()

        wn.update()         # Updates drawing and waits 5 seconds
        time.sleep(5)

for _ in range(10):
    a = MaxBill()
    a.create_painting()

