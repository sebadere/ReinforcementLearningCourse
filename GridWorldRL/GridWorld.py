from __future__ import print_function, division
from builtins import range

import numpy as np

class Grid:
    def __init__(self,rows,cols,start):
        self.rows = rows
        self.cols = cols
        self.i = start[0]
        self.j = start[1]
    
    def set(self,rewards,actions):
        self.rewards = rewards
        self.actions = actions
    

    def set_state(self,s):
        self.i = s[0]
        self.j = s[1]

    def current_state(self):
        return(self.i, self.j)

    def is_terminal(self,s):
        return s not in self.actions
    
    def get_next_state(self, s,a):
        i, j = s[0], s[1]
        if a in self.actions[(i,j)]:
            if a == 'U':
                i -= 1
            elif a == 'D':
                i += 1
            elif a == 'R':
                j += 1
            elif a == 'L':
                j -= 1
        return i, j

    def move(self, action):
        if action in self.actions[(self.i,self.j)]:
            if action == 'U':
                self.i -= 1
            elif action == 'D':
                self.i += 1
            elif action == 'R':
                self.j += 1
            elif action == 'L':
                self.j -= 1
        return self.rewards.get((self.i,self.j),0)

    def undo_move(self, action):
        if action == 'U':
            self.i += 1
        if action == 'D':
            self.i -= 1
        if action == 'R':
            self.j -= 1
        if action == 'L':
            self.j += 1
        assert(self.current_state() in self.all_states())
    
    def game_over(self):
        return(self.i, self.j) not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())


    

def standard_grid():
    g = Grid(3,4,(2,0))
    rewards = {(0,3): 1 , (1,3): -1}
    actions = {
        (0,0) : {'D','R'},
        (0,1) : {'L','R'},
        (0,2) : {'L','D','R'},
        (1,0) : {'U','D'},
        (1,2) : {'U','D' ,'R'},
        (2,0) : {'U','R'},
        (2,1) : {'L','R'},
        (2,2) : {'L','R','U'},
        (2,3) : {'L','U'},
    }
    g.set(rewards,actions)
    return g


g = standard_grid()

