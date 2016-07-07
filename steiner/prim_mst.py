from position import Position

def mst(points):
	
	#keep a list of traversed vertices
	bucket = []
	bucket.append(points[-1])

	#list with distances to unconnected vertices
	shortest_dist = []

	for point in points:
		if point not in bucket:
			shortest_dist.append([[point,points[-1]],points[-1].rect_dist(point)])

	shortest_dist.sort(key=lambda x: x[1],reverse=True)
	mst_weight = 0 #total path length of mst
	mst = []

	while len(bucket) != len(points):
		path,weight = shortest_dist.pop()
		mst.append(path)
		point,_ = path
		bucket.append(point)

		# update shortest_dist based on point
		for dist in shortest_dist:
			[dist_point,_],dist_weight = dist
			new_weight = point.rect_dist(dist_point)
			if new_weight < dist_weight:
				dist[0] = [dist_point,point]
				dist[1] = new_weight

		shortest_dist.sort(key=lambda x: x[1],reverse=True)

	return mst

def wirelength(tree):
	wire = 0
	for path in tree:
		wire += path[0].rect_dist(path[1])
	return wire
