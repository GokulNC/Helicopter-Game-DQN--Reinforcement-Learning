## Inspiration: https://pythonprogramming.net/live-graphs-matplotlib-tutorial/

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from shutil import copyfile

FILENAME = 'dumps.txt'
avg_over = 10

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#ax2 = fig.add_subplot(1,1,1)

def animate(i):
    global avg_over
    dest_file = "/tmp/" + FILENAME
    copyfile(FILENAME, dest_file)
    graph_data = open(dest_file, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    ys_sum = 0.0
    #zs_sum = 0.0
    #zs = []
    j = 0
    for line in lines:
        if len(line) > 1:
            try:
                x, y, z = line.split(',')
                ys_sum += float(y)
                #zs_sum += float(z)
                j += 1
                if j % avg_over == 0:
                    xs.append(float(x))
                    ys.append(ys_sum/float(avg_over))
                    #zs.append(zs_sum/float(avg_over))
                    ys_sum = 0.0
                    #zs_sum = 0
            except:
                continue
    ax1.clear()
    #ax2.clear()
    ax1.plot(xs, ys)
    #ax2.plot(xs, zs)

ani = animation.FuncAnimation(fig, animate, interval=10000000)
plt.show()
