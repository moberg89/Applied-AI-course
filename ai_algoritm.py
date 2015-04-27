# -*- coding: utf-8 -*-
"""
AI-template
"""
import numpy as np
import math
class CommandClass:
    #Either the robot is told a trajectory or position
    def __init__(self, x=[], y=[], v=[], theta=[]):
        if v==[]:        
            self.x=x
            self.y=y
            self.v=[]        
            self.theta=[]    
        else:    
            self.x=[]
            self.y=[]
            self.v=v        
            self.theta=theta

def update(current_pos, current_ori, current_sen, goal):
    return CommandClass(x=goal[0], y=goal[1])