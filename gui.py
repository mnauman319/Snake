from tkinter import *
import tkinter

root = Tk()
root.title("Snake")
root.geometry('1000x800')
frame = Frame(root, height=800, width=1000, bg='black')
frame.pack()



def key_press(e:tkinter.Event):
    key_pressed = str(e.char)
    if key_pressed == 'w' or e.keysym=="Up":
        keyup(e)
    elif key_pressed == 's' or e.keysym=="Down":
        keydown(e)
    elif key_pressed == 'a' or e.keysym=="Left":
        keyleft(e)
    elif key_pressed == 'd' or e.keysym=="Right":
        keyright(e)

def keyup(e):
    print("up")
def keydown(e):
    print("down")
def keyleft(e):
    print("left")
def keyright(e):
    print("right")


root.bind("<Key>", key_press)
root.mainloop()