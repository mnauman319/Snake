from tkinter import *

root = Tk()
root.title("Snake")
root.geometry('1000x800')
frame = Frame(root, height=800, width=1000, bg='black')
frame.pack()



def key_press(e):
    key_pressed = str(e.char)
    if key_pressed == 'w':
        keyup(e)
    elif key_pressed == 's':
        keydown(e)
    elif key_pressed == 'a':
        keyleft(e)
    elif key_pressed == 'd':
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