from max_bill import MaxBill
import turtle
from Zoe_art_module import run_art_generation
from naol import main


wn = turtle.Screen()

artist = int(input("which artist do you want to display? 1 for Max Bill, 2 for Bryce Hudson, and 3 for Kazemir Malkevich:  "))

if artist == 1:
    for _ in range(10):
        for i in (wn.turtles()): # this is here becasue there was a random visible turtle that I could not find.
            if i.isvisible() is True:
                i.ht()
        a = MaxBill()
        a.create_painting()


elif artist == 2:

    run_art_generation()
    wn.mainloop()

elif artist == 3:
    main()


else:
    print("Incorrect input, try again!")
