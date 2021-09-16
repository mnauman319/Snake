'''
------------------------Snake Rules------------------------

    1. Each item eaten makes the snake longer
    2. The player loses when the snake runs into the 
    end of the game board
    3. The player loses when the snake runs into itself

''' 

from tkinter import *
import tkinter
from typing import List, Tuple
from snake import *
segment_size = 5
speed = 10
movement_freq = 300
direction = {
    (-speed,0): 'Left',
    (speed,0): 'Right',
    (0,speed): 'Down',
    (0,-speed): 'Up'
}
axis_opposite = {
    'Right': 'Left',
    'Left': 'Right',
    'Up': 'Down',
    'Down': 'Up',
}

def direction_from_movement(value:str):
    keys = list(direction.keys())
    values = list(direction.values())
    return keys[values.index(value)]
class GUI:
    def __init__ (self, root:tkinter):
        
        self.root = root
        self.root.title("Snake")
        self.root.geometry('1000x800')
        self.my_canvas = Canvas(self.root,width=1000, height=800,  bg='black')
        self.my_canvas.pack()
        self.head = Segment(speed,0, segment_size, self.my_canvas)
        self.body = List[Segment]
        self.body = [self.head]
        # self.food = Canvas(self.my_canvas, width=100, height=100).pack()
        self.recently_eaten = 0

    def end_game(self):
        print('game over')
    def create_food(self):
        print('created food')
    def move_snake(self):
        seg_being_rotated = 0
        location = self.head.canvas.coords(self.head.seg)
        touching_left = location[0]+self.head.s_move_x<=0
        touching_right = location[0]+self.head.s_move_x>=1000
        touching_top = location[1]+self.head.s_move_y<=0 
        touching_bottom = location[1]+self.head.s_move_y>=800
        if(touching_left or touching_right or touching_bottom or touching_top):
            self.end_game()
        else:
            for seg in self.body:
                if seg.seg > 1:
                    last_piece = self.body[seg.seg-2]
                    if last_piece.rotating:
                        seg_being_rotated = seg.seg
                        self.rotate_snake(last_piece.cur_dir,seg.cur_dir, seg)
                        seg.cur_dir = last_piece.cur_dir
                        last_piece.rotating = False
                        if seg == self.body[len(self.body)-1]:
                            seg.rotating = False
                        # print(f'seg = {seg.seg} is rotating = {seg.rotating}')

                seg.canvas.move(seg.seg, seg.s_move_x, seg.s_move_y)
                location = self.head.canvas.coords(self.head.seg)
                cur_xy = direction_from_movement(seg.cur_dir)
                seg.s_move_x = cur_xy[0]
                seg.s_move_y = cur_xy[1]
            self.root.after(movement_freq,self.move_snake)
            if seg_being_rotated > 0 and seg_being_rotated <= len(self.body):
                seg = self.body[seg_being_rotated-1]
                seg.rotating = True

    def grow_snake(self,seg:Segment):
        last_piece = self.body[len(self.body)-1]
        new_piece = Segment(last_piece.s_move_x, last_piece.s_move_y, segment_size, self.my_canvas, last_piece.cur_dir, self.my_canvas.coords(last_piece.seg))
        self.body.append(new_piece)
        return new_piece
    def rotate_snake(self, new_dir:str, prev_dir:str, piece:Segment):
        piece.cur_dir = new_dir
        body_coords = piece.canvas.coords(piece.seg)
        cur_x0 = body_coords[0]
        cur_y0 = body_coords[1]
        cur_x1 = body_coords[2]
        cur_y1 = body_coords[3]
        if new_dir == 'Up':
            if prev_dir == 'Left':
                body_coords = [cur_x0+segment_size, cur_y0-segment_size, cur_x0+2*segment_size, cur_y1]
                piece.canvas.coords(piece.seg,body_coords)
            elif prev_dir == 'Right':
                body_coords = [cur_x0, cur_y0-segment_size, cur_x0+segment_size, cur_y1]
                piece.canvas.coords(piece.seg,body_coords)
        elif new_dir == 'Down':
            if prev_dir == 'Left':
                body_coords = [cur_x0+segment_size, cur_y0, cur_x0+2*segment_size, cur_y1+segment_size]
                piece.canvas.coords(piece.seg,body_coords)
            elif prev_dir == 'Right':
                body_coords = [cur_x0, cur_y0, cur_x0+segment_size, cur_y1+segment_size]
                piece.canvas.coords(piece.seg,body_coords)
        elif new_dir == 'Left':
            if prev_dir == 'Up':
                body_coords = [cur_x0+segment_size, cur_y0+segment_size, cur_x0-segment_size, cur_y0+2*segment_size]
                piece.canvas.coords(piece.seg,body_coords)
            elif prev_dir == 'Down':
                body_coords = [cur_x0+segment_size, cur_y0, cur_x0-segment_size, cur_y0+segment_size]
                piece.canvas.coords(piece.seg,body_coords)
        elif new_dir == 'Right':
            if prev_dir == 'Up':
                body_coords = [cur_x0, cur_y0+segment_size, cur_x0+2*segment_size, cur_y0+2*segment_size]
                piece.canvas.coords(piece.seg,body_coords)
            elif prev_dir == 'Down':
                body_coords = [cur_x0, cur_y0, cur_x0+2*segment_size, cur_y0+segment_size]
                piece.canvas.coords(piece.seg,body_coords)

    def key_press(self,e:tkinter.Event):
        key_pressed = str(e.char)
        new_dir = ""
        if key_pressed == 'w' or e.keysym=="Up":
            new_dir = 'Up'
        elif key_pressed == 's' or e.keysym=="Down":
            new_dir = 'Down'
        elif key_pressed == 'a' or e.keysym=="Left":
            new_dir = 'Left'
        elif key_pressed == 'd' or e.keysym=="Right":
            new_dir = 'Right'

        counter = 1
        for piece in self.body:
            prev_direction = direction[(piece.s_move_x,piece.s_move_y)]
            if prev_direction == new_dir or prev_direction == axis_opposite[new_dir]:
                continue
            if counter == 1:
                self.rotate_snake(new_dir, prev_direction, piece)
                movement = direction_from_movement(new_dir)
                piece.s_move_x = movement[0]
                piece.s_move_y = movement[1]
                piece.rotating = True
                piece.cur_dir = new_dir
            counter += 1

    def start(self):
        self.root.bind("<Key>", self.key_press)
        self.root.after(movement_freq, self.move_snake)
        self.root.mainloop()

my_GUI = GUI(Tk())
a = my_GUI.grow_snake(my_GUI.head)
b = my_GUI.grow_snake(a)
my_GUI.grow_snake(b)
my_GUI.start()




