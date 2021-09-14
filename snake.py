import tkinter
from tkinter import *
class Segment:
    def __init__(self, s_move_x:int, s_move_y:int, segment_size, canvas:Canvas, cur_dir = 0, prev_seg = [0]):
        self.s_move_x = s_move_x
        self.s_move_y = s_move_y
        self.canvas = canvas
        if prev_seg == [0]:
            self.seg = self.canvas.create_rectangle(300,200,300-2*segment_size,200-segment_size, fill='white')
        else:
            if cur_dir == 'Right':
                self.seg = self.canvas.create_rectangle(prev_seg[2]-1,prev_seg[1], prev_seg[2]-6,prev_seg[3])
            elif cur_dir == 'Left':
                self.seg = self.canvas.create_rectangle(prev_seg[0]+1,prev_seg[1], prev_seg[0]+6,prev_seg[3])
    def do_something(self):
        print('something was done')