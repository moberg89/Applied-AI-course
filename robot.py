# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:39:04 2015

@author: ragnar
"""
import math

#def __init__(self, x=0, y=0, theta=0, v=0):
#    self.posx=x
#    self.posy=y
#    self.postheta=theta
#    self.velocity=v
#    #Private variables
#    self.error_theta=0
#    self.error_velocity=0
#    self.deltaxy=1
#    self.deltatheta=1

posx=0
posy=0
postheta=1
velocity=1
#Private variables
error_theta=0
error_velocity=0
deltaxy=0.1
deltatheta=0.1

def get_pos():
    return [posx, posy]    
        
def get_ori():
    return postheta
    
def move(command):
    if command.v==[]:
        xycontrol(command.x, command.y)
    else:
        polarcontrol(command.theta, command.v)
    updaterobot()
    
#Following code will be made private    
def xycontrol(x,y):
    relativex=posx-x
    relativey=posy-y
    theta=math.atan2(relativey, relativex)
    v=math.hypot(relativex, relativey) #TODO improve
    polarcontrol(theta,v) #Lazy shit that will be replaced later
    
def polarcontrol(theta,v):
    global error_theta
    global error_velocity    
    error_theta=postheta-theta    
    error_velocity=velocity-v
    
def updaterobot():
    global postheta
    global posx
    global posy
    postheta=postheta-error_theta*deltatheta
    posx=posx-math.cos(postheta)*deltaxy*velocity
    posy=posy-math.sin(postheta)*deltaxy*velocity
    
    
