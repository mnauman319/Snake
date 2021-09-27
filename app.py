'''
------------------------Snake Rules------------------------

    1. Each item eaten makes the snake longer
    2. The player loses when the snake runs into the 
    end of the game board
    3. The player loses when the snake runs into itself

''' 

import tkinter
import random
from typing import List, Tuple
from snake import *

segment_size = 5
food_size = 5
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
        self.food = self.my_canvas.create_rectangle(400,200,400+food_size, 200-food_size, fill='white')
        self.recently_eaten = 0

    def end_game(self):
        print('game over')
    def touching_border(self):
        location = self.head.canvas.coords(self.head.seg)
        touching_left = location[0]+self.head.s_move_x<=0
        touching_right = location[0]+self.head.s_move_x>=1000
        touching_top = location[1]+self.head.s_move_y<=0 
        touching_bottom = location[1]+self.head.s_move_y>=800
        return touching_left or touching_right or touching_bottom or touching_top
    def generate_food(self):
        s_min_max = [[1000,0], [800, 0]] # [[x_min, x_max], [y_min, y_max]]
        f_loc = []
        # finding the max and minx for x and y from the existing snake
        for seg in self.body:
            s_loc = seg.canvas.coords(seg.seg)
            x0 = s_loc[0]
            y0 = s_loc[1]
            x1 = s_loc[2]
            y1 = s_loc[3]
            s_min_max[0][0] = x0 if x0 < s_min_max[0][0] else s_min_max[0][0]
            s_min_max[0][1] = x1 if x1 > s_min_max[0][1] else s_min_max[0][1]
            s_min_max[1][0] = y0 if y0 < s_min_max[1][0] else s_min_max[1][0]
            s_min_max[1][1] = y1 if y1 > s_min_max[1][1] else s_min_max[1][1]

        dir = random.choice(['NE', 'NW', 'SE', 'SW'])
        x = -1
        y = -1
        if dir == 'NE':
            while x%5 !=0:
                x = random.randint(2*food_size, s_min_max[0][0]) -food_size
            while y%5 !=0:
                y = random.randint(2*food_size, s_min_max[1][0]) -food_size
            f_loc = [x,y,x+food_size,y+food_size]
            self.my_canvas.coords(self.food,f_loc)
        elif dir == 'NW':
            while x%5 !=0:
                x = random.randint(s_min_max[0][1] + food_size, 1000-2*food_size)
            while y%5 !=0:
                y = random.randint(2*food_size, s_min_max[1][0]) - food_size
            f_loc = [x,y,x+food_size,y+food_size]
            self.my_canvas.coords(self.food,f_loc)
        elif dir == 'SE':
            while x%5 !=0:
                x = random.randint(2*food_size, s_min_max[0][0]) - food_size
            while y%5 !=0:
                y = random.randint(s_min_max[1][1] + food_size, 800-2*food_size)
            f_loc = [x,y,x+food_size,y+food_size]
            self.my_canvas.coords(self.food,f_loc)
        elif dir == 'SW':
            while x%5 !=0:
                x = random.randint(s_min_max[0][1] + food_size, 1000-2*food_size)
            while y%5 !=0:
                y = random.randint(s_min_max[1][1] + food_size, 800-2*food_size)
            f_loc = [x,y,x+food_size,y+food_size]
            self.my_canvas.coords(self.food,f_loc)
    def same_pos(self, pos1:List[float], pos2:List[float]):
        for i in range(4):
            if pos1[i] != pos2[i]:
                return False
        return True
    def self_collision(self):
        for seg in self.body:
            if seg == self.head: continue
            head_pos = self.my_canvas.coords(self.head.seg)
            seg_pos = self.my_canvas.coords(seg.seg)
            # if self.same_pos(head_pos, seg_pos ):
            #     return True
            head_pos = [max(head_pos[0], head_pos[2]), max(head_pos[1], head_pos[3]), min(head_pos[0], head_pos[2]), min(head_pos[1], head_pos[3])]
            seg_pos = [max(seg_pos[0], seg_pos[2]), max(seg_pos[1], seg_pos[3]), min(seg_pos[0], seg_pos[2]), min(seg_pos[1], seg_pos[3])]
            if head_pos[1] > seg_pos[3] and head_pos[3] < seg_pos[3] and head_pos[0] <= seg_pos[0] and head_pos[2] >= seg_pos[2]:
                return True
            elif head_pos[1] > seg_pos[1] and head_pos[3] < seg_pos[1] and head_pos[0] <= seg_pos[0] and head_pos[2] >= seg_pos[2]:
                return True
            elif head_pos[0] > seg_pos[2] and head_pos[2] < seg_pos[2] and head_pos[1] <= seg_pos[1] and head_pos[3] >= seg_pos[3]:
                return True
            elif head_pos[0] > seg_pos[0] and head_pos[2] < seg_pos[0] and head_pos[1] <= seg_pos[1] and head_pos[3] >= seg_pos[3]:
                return True
            
        return False
    def move_snake(self):
        
        if self.touching_border():
            self.end_game()
        elif self.self_collision():
            self.end_game()
        else:
            for seg in self.body:
                cur_pos = seg.canvas.coords(seg.seg) 
                
                if len(seg.rot_dir) > 0:
                    if (len(seg.rot_dir) > len(self.head.rot_pos) or seg==self.head) and self.same_pos(cur_pos,seg.rot_pos[0]):
                        self.rotate_snake(seg.rot_dir[0],seg.cur_dir, seg)
                        seg.cur_dir = seg.rot_dir[0]
                        seg.rot_pos.pop(0)
                        seg.rot_dir.pop(0)

                seg.canvas.move(seg.seg, seg.s_move_x, seg.s_move_y)

                #Check to see if snake head is touching food
                if seg == self.head:
                    head_loc = self.my_canvas.coords(self.head.seg)
                    food_loc = self.my_canvas.coords(self.food)
                    if (head_loc[0]==food_loc[0] and head_loc[1] == food_loc[1]) or (head_loc[2]==food_loc[2] and head_loc[3]==food_loc[3]):
                        self.grow_snake(self.body[len(self.body)-1])
                        self.generate_food()


                cur_xy = direction_from_movement(seg.cur_dir)
                seg.s_move_x = cur_xy[0]
                seg.s_move_y = cur_xy[1]
            self.root.after(movement_freq,self.move_snake)

    def grow_snake(self,seg:Segment):
        last_piece = self.body[len(self.body)-1]
        new_piece = Segment(last_piece.s_move_x, last_piece.s_move_y, segment_size, self.my_canvas, last_piece.cur_dir, self.my_canvas.coords(last_piece.seg),last_piece.rot_pos, last_piece.rot_dir)
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
        cur_pos = self.head.canvas.coords(self.head.seg)
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

        prev_direction = direction[(self.head.s_move_x,self.head.s_move_y)]
        if prev_direction == new_dir or prev_direction == axis_opposite[new_dir]:
            return
        else:
            for piece in self.body: 
                piece.add_rot(cur_pos,new_dir)

    def start(self):
        self.root.bind("<Key>", self.key_press)
        self.root.after(movement_freq, self.move_snake)
        self.root.mainloop()

my_GUI = GUI(Tk())
a = my_GUI.grow_snake(my_GUI.head)
b = my_GUI.grow_snake(a)
my_GUI.grow_snake(b)
my_GUI.start()




