import tkinter
from tkinter import *
from typing import List
class Segment:
    def __init__(self, s_move_x:int, s_move_y:int, segment_size, canvas:Canvas, cur_dir:str = 'Right', prev_seg:List[float] = [0]):
        self.s_move_x = s_move_x
        self.s_move_y = s_move_y
        self.canvas = canvas
        self.rotating = False
        self.cur_dir = cur_dir
        
        if prev_seg == [0]:
            self.seg = self.canvas.create_rectangle(300,200,300-2*segment_size,200-segment_size, fill='white')
        else:
            if cur_dir == 'Right':
                self.seg = self.canvas.create_rectangle(prev_seg[2]-10,prev_seg[1], prev_seg[2]-20,prev_seg[3], fill='white')
            elif cur_dir == 'Left':
                self.seg = self.canvas.create_rectangle(prev_seg[0]+10,prev_seg[1], prev_seg[0]+20,prev_seg[3], fill="white")
            elif cur_dir == 'Up':
                self.seg = self.canvas.create_rectangle(prev_seg[0],prev_seg[1]+10, prev_seg[2],prev_seg[3]+10, fill="white")
            elif cur_dir == 'Down':
                self.seg = self.canvas.create_rectangle(prev_seg[0],prev_seg[1]-10, prev_seg[2],prev_seg[3]-10, fill="white")