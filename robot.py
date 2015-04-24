# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:39:04 2015

@author: ragnar
"""
import numpy

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

def __init__(self, x=0, y=0, theta=0, v=0):
    posx=x
    posy=y
    postheta=theta
    velocity=v

def get_pos(self):
    return x,y    
        
def get_ori(self):
    return theta
    
def move(command):
    if command.v=[]:
        xycontrol(command.x, command.y)
    else:
        polarcontrol(command.theta, command.v)
    
def xycontrol(x,y):
    pass

def polarcontrol(theta,v):
    pass
