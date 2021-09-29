import tkinter
from tkinter import *
from typing import List
class Segment:
    def __init__(self, s_move_x:int, s_move_y:int, segment_size, canvas:Canvas, cur_dir:str = 'Right', prev_seg:List[float] = [0], rot_pos = [], rot_dir = []):
        self.s_move_x = s_move_x
        self.s_move_y = s_move_y
        self.canvas = canvas
        '''
        The rot_dir is the rotation direction that still need to occur for each segment. The are kept as 'Right', 'Left', 'Up', or 'Down'.
        The rot_pos is the rotation postion or coordinates that the segment needs to be in to make the rotation.
        
        When a segment is initiated both the rot_dir and rot_pos are populated with the segment before its rot_dir and rot_pos.
        An empty array is added to the passed in arrays because this creates a unique copy of the previous segments arrays. 
        Otherwise, any change to one array would affect each segment.
        '''
        self.rot_pos = rot_pos + []
        self.rot_dir = rot_dir + []
        self.cur_dir = cur_dir
        #If the segment before this is the head the position is already decided
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

    def add_rot(self, pos, dir):
        if len(self.rot_dir) == 0 or (len(self.rot_dir) > 0 and self.rot_dir[-1] != dir):
            self.rot_dir.append(dir)
            self.rot_pos.append(pos)
        

    
    def __str__(self):
        return f'segment# - {self.seg}\ndirection - {self.cur_dir}\nrot_pos - {self.rot_pos}\nrot_dir - {self.rot_dir}'
