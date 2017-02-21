from tkinter import Tk, Canvas, Frame, BOTH
import random

class Abstract(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Kazemir Malkevich")
        self.pack(fill=BOTH)

        canvas = Canvas(self)
        x = random.randrange(120)
        x_2 = random.randrange(20)
        y = random.randrange(320)
        y_2 = random.randrange(40)
        for i in range (10):
            canvas.create_rectangle(x_2, x, y_2, y,
                                    outline='medium violet red', fill='medium violet red')
            canvas.create_rectangle(150, 10, 240, 80,
                                    outline='DarkGoldenrod2', fill='DarkGoldenrod2')
            canvas.create_rectangle(270, 10, 370, 80,
                                    outline="black", fill="black")
            canvas.pack(fill=BOTH)


def main():
    root = Tk()
    ex = Abstract(root)
    root.geometry("800x900+400+600")
    root.mainloop()

if __name__ == '__main__':
    main()