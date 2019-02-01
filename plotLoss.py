import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

FILENAME = 'dumps.txt'

style.use('fivethirtyeight')

fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open(FILENAME,'r').read()
    lines = graph_data.split('\n')
    xs = []
    #ys = []
    zs = []
    for line in lines:
        if len(line) > 1:
            x, y, z = line.split(',')
            xs.append(float(x))
            #ys.append(float(y))
            zs.append(float(z))
    #ax1.clear()
    ax2.clear()
    #ax1.plot(xs, ys)
    ax2.plot(xs, zs)

ani = animation.FuncAnimation(fig, animate, interval=10000000)
plt.show()
