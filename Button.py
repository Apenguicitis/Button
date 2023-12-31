from tkinter import *
from tkinter import ttk
import time
count = 0


def counter():
    global count
    count += 1

    if count == 5:
        the_button_object.config(text="You've pressed it 5 times, you're tenacious")
    elif count == 10:
        the_button_object.config(text="Do you have anything better to do?")
    elif count == 20:
        the_button_object.config(text="Buddy you have a problem")
    elif count == 30:
        the_button_object.config(text="If you press this one more time, we're done")

    elif count == 31:
        the_button_object.config(state=DISABLED)
        the_button_object.config(text="I told you")
        time.sleep(3)
        the_button_object.config(state=NORMAL, text="Okay I lied, but one more press and we're really done")

    elif count == 32:
        root.destroy()


root = Tk()
button_presses = 0
root.title("Click this funny Button")
root.geometry('320x240')
the_button_object = Button(root, text='Click Me!', bd='5', command=counter)
the_button_object.pack(side='top')
the_button_object.pack(padx=8, pady=80)


root.mainloop()