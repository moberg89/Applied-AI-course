# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
import sys


             
             





class Node(object):
    def __init__(self,walkable=True):
        self.neighbours = []
        self.inopen = False
        self.inclosed = False
        self.position = np.array([0,0])
        self.walkable = walkable
        self.herustic = sys.float_info.max
        self.distance = sys.float_info.max
        self.parent = None
        
        #raise  NotImplementedError()
        
    def AddNeighbour(self,other):
        self.neighbours.append(other)
        
    def ClearNeighbours(self):
        self.neighbours =[]
        
    def GetPosition(self):
        return self.position
    
    def SetPosition(self,npos):
        self.position = npos
        
    def LinkNodes(self,other):
        self.neighbours.append(other)
        other.neighbours.append(self)
        
    def __herustic__(self):
        return self.herustic
        
    def __n__(self):
        print("Current node:" + str(self.position))
        print("Neighbours:")
        for n in self.neighbours:
            print(str(n.position))
        print("--------")
        

class PathFinder(object):
    def __init__(self):
        self.nodes = []
        
    @staticmethod
    def Herustic(n1,n2):
        return math.sqrt((n1.position[0] - n2.position[0]) **2 + (n1.position[1] - n2.position[1]) **2)
        
    def HerusticCompare(self,n1,n2):
            return n1.herustic - n2.herustic
    
    def AddNode(self,nod):
        self.nodes.append(nod)
        
    def FindPath(self,start,goal):
        if start==goal:
            return self.FinalizePath(start,goal)
        self.ResetNodes()
        
        openlist = []
        closedlist = []
        
        openlist.append(start)
        
        while len(openlist)>0:
            active = openlist.pop()
            closedlist.append(active)
            active.inopen = False
            active.inclosed = True
            
            print("Current Node:"+str(active.position[0])+","+str(active.position[1]))
            if (active is goal):
                return self.FinalizePath(start,goal)
              
            templist = []
            for n in active.neighbours:
                if n.walkable == True and not n.inclosed:
                    templist.append(n)
            if len(templist) == 0:
                continue
            
            for n in templist:
                n.herustic = self.Herustic(n,goal)
            templist.sort(key=lambda b: b.__herustic__(),reverse=True)
            for n in templist:
                if n.inopen:
                    continue
                else:
                    n.inopen = True
                    n.parent = active
                    openlist.append(n)
            for n in openlist:
                print(n.herustic)
            print("----------")
        #No path could be found    
        print("No path found!")
        return None
        
    def Setup(self,arr):
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if arr[x][y] is 0:
                    arr[x][y] = Node(True)
                else:
                    arr[x][y] = Node(False)
                arr[x][y].position = np.array([x,y])
                self.nodes.append(arr[x][y])
        
        for y in range(len(arr)):
            for x in range(len(arr[y])):
                n = arr[y][x]
                sy = max(0,y-1)
                ey = min(len(arr),y+2)
                sx = max(0,x-1)
                ex = min(len(arr[y]),x+2)
                print("Current Node: " + str(n.position))
                print(sy,ey,sx,ex)
                for iy in range(sy,ey):              
                    for ix in range (sx,ex):
                        a = arr[iy][ix]
                        if(a is n or a in n.neighbours):
                            continue
                        n.neighbours.append(a)
                                
        #raise NotImplementedError()
                    
            
    def FinalizePath(self,start,goal):
        print("Path found, finalizing")
        nodelist = []
        currentnode = goal
        while currentnode is not start:
            nodelist.append((currentnode.position[0],currentnode.position[1]))
            currentnode = currentnode.parent
        nodelist.append((start.position[0],start.position[1]))
        nodelist.reverse()
        return nodelist
    
    def ResetNodes(self):
        for n in self.nodes:
            n.herustic = sys.float_info.max
            n.distance = sys.float_info.max
            n.inClosed = False
            n.inOpen = False
            n.parent = None
                
"""
import matplotlib.pyplot as plot
import plot as p


def test(arr):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print(y,x)          
            #for n in templist:
             #   n.Herustic = self.Herustic(n,goal)
            #temp2 =(templist,cmp=HerusticCompare)
X = 'X'
omap = np.array([
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,X,X,X,X,0],
             [0,X,0,0,X,0],
             [0,X,0,0,X,0],
             [0,0,0,0,0,0]],dtype=object)
             
omap2 = np.array([
                 [0,X,0],
                 [0,0,0]],dtype=object)

omap3 = np.array([  [0,0,0],
                    [0,X,X],
                    [0,0,0],
                    [X,0,0]],dtype=object)
                    
omap4 = np.array([[0,0,0,0,0,0,0,0,0,0]],dtype=object)


m = omap3

pf = PathFinder()
pf.Setup(m)

start = m[0][2]
goal = m[3][2]
xlog = []
ylog = []

path = pf.FindPath(start,goal)

for z in path:
    xlog.append(z[1])
    ylog.append(z[0])
path
p.plotall(xlog,ylog)
"""    