'''
------------------------Snake Rules------------------------

    1. Each item eaten makes the snake longer
    2. The player loses when the snake runs into the 
    end of the game board
    3. The player loses when the snake runs into itself

''' 

from tkinter import *
import tkinter
from snake import *
segment_size = 5
speed = 5
movement_freq = 500
direction = {
    (-speed,0): 'Left',
    (speed,0): 'Right',
    (0,speed): 'Down',
    (0,-speed): 'Up'
}
class GUI:
    def __init__ (self, s_move_x:int, s_move_y:int, root:tkinter):
        
        self.s_move_x = s_move_x
        self.s_move_y = s_move_y
        self.root = root
        self.root.title("Snake")
        self.root.geometry('1000x800')
        self.my_canvas = Canvas(self.root,width=1000, height=800,  bg='black')
        self.my_canvas.pack()
        self.head = Segment(speed,0, segment_size, self.my_canvas)
        # self.body = self.my_canvas.create_rectangle(300,200,300-2*segment_size,200-segment_size, fill='white')
        self.body = [self.head]
        print(self.body[0])

    def end_game(self):
        print('game over')
    def move_snake(self):
        if(self.head.canvas.coords(self.head.seg)[0]+self.head.s_move_x==0 or self.head.canvas.coords(self.head.seg)[1]+self.head.s_move_y==0):
            self.end_game()
        else:
            for seg in self.body:
                seg.canvas.move(seg.seg, seg.s_move_x, seg.s_move_y)
                print(self.my_canvas.coords(seg.seg))
            self.root.after(movement_freq,self.move_snake)

    def grow_snake(self,seg:Segment):
        self.body.append(Segment(speed, 0, segment_size, self.my_canvas,direction[(seg.s_move_x,seg.s_move_y)],seg.canvas.coords(seg.seg)))
        return
    def rotate_snake(self, new_dir, prev_dir):
        body_coords = self.my_canvas.coords(self.body)
        cur_x0 = body_coords[0]
        cur_y0 = body_coords[1]
        cur_x1 = body_coords[2]
        cur_y1 = body_coords[3]
        if new_dir == 'Up':
            if prev_dir == 'Left':
                body_coords = [cur_x0+segment_size, cur_y0-segment_size, cur_x0+2*segment_size, cur_y1]
                self.my_canvas.coords(self.body,body_coords)
            elif prev_dir == 'Right':
                body_coords = [cur_x0, cur_y0-segment_size, cur_x0+segment_size, cur_y1]
                self.my_canvas.coords(self.body,body_coords)
        elif new_dir == 'Down':
            if prev_dir == 'Left':
                body_coords = [cur_x0+segment_size, cur_y0, cur_x0+2*segment_size, cur_y1+segment_size]
                self.my_canvas.coords(self.body,body_coords)
            elif prev_dir == 'Right':
                body_coords = [cur_x0, cur_y0, cur_x0+segment_size, cur_y1+segment_size]
                self.my_canvas.coords(self.body,body_coords)
        elif new_dir == 'Left':
            if prev_dir == 'Up':
                body_coords = [cur_x0+segment_size, cur_y0+segment_size, cur_x0-segment_size, cur_y0+2*segment_size]
                self.my_canvas.coords(self.body,body_coords)
            elif prev_dir == 'Down':
                body_coords = [cur_x0+segment_size, cur_y0, cur_x0-segment_size, cur_y0+segment_size]
                self.my_canvas.coords(self.body,body_coords)
        elif new_dir == 'Right':
            if prev_dir == 'Up':
                body_coords = [cur_x0, cur_y0+segment_size, cur_x0+2*segment_size, cur_y0+2*segment_size]
                self.my_canvas.coords(self.body,body_coords)
            elif prev_dir == 'Down':
                body_coords = [cur_x0, cur_y0, cur_x0+2*segment_size, cur_y0+segment_size]
                self.my_canvas.coords(self.body,body_coords)

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
        prev_direction = direction[(self.s_move_x,self.s_move_y)]
        if prev_direction == 'Down' or prev_direction == 'Up':
            return
        self.s_move_x = 0
        self.s_move_y = -speed
        self.rotate_snake('Up', prev_direction)

    def keydown(self,e:Event):
        prev_direction = direction[(self.s_move_x,self.s_move_y)]
        if prev_direction == 'Up' or prev_direction == 'Down': 
            return
        self.s_move_x = 0
        self.s_move_y = speed
        self.rotate_snake('Down', prev_direction)
    def keyleft(self,e:Event):
        prev_direction = direction[(self.s_move_x,self.s_move_y)]
        if prev_direction == 'Right' or prev_direction == 'Left': 
            return
        self.s_move_x = -speed
        self.s_move_y = 0
        self.rotate_snake('Left', prev_direction)
    def keyright(self,e:Event):
        prev_direction = direction[(self.s_move_x,self.s_move_y)]
        if prev_direction == 'Left' or prev_direction == 'Right': 
            return
        self.s_move_x = speed
        self.s_move_y = 0
        self.rotate_snake('Right', prev_direction)
    def start(self):
        self.root.bind("<Key>", self.key_press)
        self.root.after(movement_freq, self.move_snake)
        self.root.mainloop()

my_GUI = GUI(speed,0,Tk())
my_GUI.grow_snake(my_GUI.head)
my_GUI.start()




