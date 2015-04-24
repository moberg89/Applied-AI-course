#Sugestion by ragnar based on Ericks idea
import robot
import world
import ai_algoritm
import matplotlib.pyplot as plt

poslogx=[]
poslogy=[]
#while 1:
for j in range(220):
    current_pos = robot.get_pos()    
    current_ori = robot.get_ori()
    poslogx.append(current_pos[0])
    poslogy.append(current_pos[1])
    current_sen = world.read_sensors(current_pos, current_ori)
 
    #The ai-algoritmh output an instance of the CommandClass
    command = ai_algoritm.update(current_pos, current_ori, current_sen)    
    #The robot can both act acording to a position command or trajectory command
    robot.move(command)

    plt.plot(poslogx, poslogy)
#    print() # so we can see what is happening
