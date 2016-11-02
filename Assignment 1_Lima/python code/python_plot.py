import numpy as nump
import random as rand
import matplotlib.pyplot as plot

x=set()
for m in range(0,10):
	x.add(rand.randint(0,90))
x=sorted(x)
m=list(x)

ySin = nump.sin(m)
yCos = nump.cos(m)

#Set title and plot the graph, set green color for Sin and Red for Cos
plot.title('Sin and Cos functions')
plot.plot(x, ySin,'g' ,x,yCos,'r')

# Get plot axis and change y axis limits
x1,x2,y1,y2 = plot.axis()
plot.axis((x1,x2,-3,3))

#Add labels, legend and show the graph
plot.xlabel('X - Axis')
plot.ylabel('Y - Axis')
plot.legend(['Sine', 'Cosine'])
plot.show()