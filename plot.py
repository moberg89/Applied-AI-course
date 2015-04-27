import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.close('all')
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

def addobstacles(obstacles):
    for i in obstacles:
        ax1.add_patch(
            patches.Circle(
                i,   # (x,y)
                0.01,          # radius
            )
        )

        
def plotall(poslogx, poslogy):        
        ax1.plot(poslogx, poslogy)
        fig1.show()
#fig1.savefig('circle1.png', dpi=90, bbox_inches='tight')