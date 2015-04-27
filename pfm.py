# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:52:23 2015

@author: ragnar
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

def calcstrenght(relativex, relativey):
    return math.hypot(relativex, relativey)

def update(current_pos, current_ori, current_sen, goal):
    relativex=current_pos[0]-goal[0]
    relativey=current_pos[1]-goal[1]
    try:
        strength=calcstrenght(relativex, relativey)**2
    except OverflowError:
        strength=15**256
    resx=relativex*strength
    resy=relativey*strength    
    for i in current_sen:
        relativex=i[0]-current_pos[0]
        relativey=i[1]-current_pos[1]
        try:
                strength=calcstrenght(relativex, relativey)**-1
        except OverflowError:
            strength=15**256
        resx=resx+relativex*strength*100
        resy=resy+relativey*strength*100   
    theta=math.atan2(resy, resx)
    v=math.hypot(resx, resy)/100
    return CommandClass(v=v,theta=theta)