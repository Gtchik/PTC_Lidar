from math import cos, pi, sin
from hough import *
from data import data

xy=[]
for point in data:
    x=point[2]*sin(point[1]*pi/180)
    y=point[2]*cos(point[1]*pi/180)
    xy.append([x, y])
# print(xy)
x = []
y = []
for i in range (len(xy)):
    x.append(xy[i][0])
    y.append(xy[i][1])
plt.plot(x,y, "o")

plt.show()
fctHoughTchik(xy)


