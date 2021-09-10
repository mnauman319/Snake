from os import name
from tkinter import *
import tkinter

class GUI:
    def __init__ (self, x:int, y:int, root:tkinter):
        
        self.x = x
        self.y = y
        self.root = root
        self.root.title("Snake")
        self.root.geometry('1000x800')
        self.my_canvas = Canvas(self.root, height=800, width=1000, bg='black')
        self.my_canvas.pack()
        self.body = self.my_canvas.create_rectangle(300,200,290,195, fill='white')
        


    def move_snake(self):
        self.my_canvas.move(self.body, self.x, self.y)
        self.root.after(1000,self.move_snake)

    def grow_snake(self):
        return
    def rotate_snake(self, plane, prev_dir):
        body_coords = self.my_canvas.coords(self.body)
        cur_x0 = body_coords[0]
        cur_y0 = body_coords[1]
        cur_x1 = body_coords[2]
        cur_y1 = body_coords[3]

        width = abs(cur_x1 - cur_x0)
        height = abs(cur_y1-cur_y1)
        if plane == 'up':
            if prev_dir == 'left':
                body_coords = [cur_x0-5, cur_y0-5, cur_x0, cur_y1+5]
                self.my_canvas.coords(self.body,body_coords)
        #     elif prev_dir == 'right':
        # elif plane == 'horizontal':
        # return
    def key_press(self,e:tkinter.Event):
        key_pressed = str(e.char)
        if key_pressed == 'w' or e.keysym=="Up":
            self.keyup(e)
        elif key_pressed == 's' or e.keysym=="Down":
            self.keydown(e)
        elif key_pressed == 'a' or e.keysym=="Left":
            self.keyleft(e)
        elif key_pressed == 'd' or e.keysym=="Right":
            self.keyright(e)

    def keyup(self,e:Event):
        
        prev_direction = 'left' if self.x == -5 else 'right'
        self.x = 0
        self.y = -5
        
        self.rotate_snake('up', prev_direction)
    def keydown(self,e:Event):
        self.x = 0
        self.y = 5
    def keyleft(self,e:Event):
        self.x = -5
        self.y = 0
    def keyright(self,e:Event):
        self.x = 5
        self.y = 0

    def start(self):
        self.root.bind("<Key>", self.key_press)
        self.root.after(1000, self.move_snake)
        self.root.mainloop()
my_GUI = GUI(5,0,Tk())
my_GUI.start()