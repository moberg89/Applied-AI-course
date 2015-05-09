# -*- coding: utf-8 -*-
"""
Created on Thu May 07 11:10:46 2015

@author: SP
"""

import AStar
import random

class Proad(AStar.PathFinder):
    def buildmap(self,ymin,ymax,xmin,xmax,density):
        lis = []
        c = density
        invalids =0
        while c < density:
            x = random.randint(xmin,xmax)
            y = random.randint(ymin,ymax)
            nval = (x,y)
            if lis.count(nval) > 0:
                invalids+=1
                continue
            lis.append(nval)
            c+=1
        print "Done! double hits:" + str(invalids)
            
p = Proad()
p.buildmap(0,1,0,10,100)