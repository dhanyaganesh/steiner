from reduced_steiner import *
from prim_mst import *
import matplotlib.pyplot as plt
from random import randint

points = []
for i in range(20):
	point = Position(randint(0,20),randint(0,20))
	if point not in points:
		points.append(point)

tree = reduced_steiner(points)
for path in  tree:
	src = path[0]
	des = path[1]
	plt.plot([src.getX(),src.getX()],[src.getY(),des.getY()],color='black',marker='o')
	plt.plot([src.getX(),des.getX()],[des.getY(),des.getY()],color='black',marker='o')

plt.title("Steiner Tree")
plt.axis([-5,25,-5,25])
plt.show()
