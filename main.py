#Sugestion by ragnar based on Ericks idea
import robot
import world
import ai_algoritm

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
  
while (1)
    current_pos = robot.get_pos()    
    current_ori = robot.get_ori()

    current_sen = world.read_sensors(current_pos, current_ori)
 
    #The ai-algoritmh output an instance of the CommandClass
    command = ai_algorithm.update(current_pos, current_ori, current_sen)    
    #The robot can both act acording to a position command or trajectory command
    robot.move(command)

    print() # so we can see what is happening
