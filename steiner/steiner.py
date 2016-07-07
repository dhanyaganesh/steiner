from prim_mst import *
import copy

##Steps:
##	1. Get Hunan Points
##	2. Add points that reduce most cost
##	3. If degree <= 2 delete the point

def steiner(points):
	smallest_mst = mst(points)
	
	steiner_points = []

	# this keeps points U steiner_points till date
	union_of_points = copy.deepcopy(points)
	hanan_grid = []
	max_x = max(points,key=lambda x: x.getX()).getX()
	min_x = min(points,key=lambda x: x.getX()).getX()
	max_y = max(points,key=lambda x: x.getY()).getY()
	min_y = min(points,key=lambda x: x.getY()).getY()
	for x in range(min_x,max_x+1):
		for y in range(min_y,max_y+1):
			hanan_grid.append(Position(x,y))

	for point in points:
		hanan_grid.remove(point)

	min_length = wirelength(smallest_mst)

	while True:
		steiner_candidates = []
		for point in hanan_grid:
			union_of_points.append(point)
			difference = wirelength(mst(union_of_points))-min_length
			steiner_candidates.append([point,difference])
			union_of_points.pop()

		steiner_candidates.sort(key=lambda x:x[1])
		min_point,difference = steiner_candidates[0]
		if difference < 0:
			steiner_points.append(min_point)
			hanan_grid.remove(min_point)
			union_of_points.append(min_point)
			smallest_mst = mst(union_of_points)
			min_length = wirelength(mst(union_of_points))
		else:
			break
	
	return smallest_mst
