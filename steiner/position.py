import math

class Position:
	"""
	A class to express position in a cartesian plane
	"""
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def __eq__(self,other):
		if self.x==other.x and self.y==other.y:
			return True
		else:
			return False

	def rect_dist(self,other):
		# defines the function to get rectangular distance between points	
		return (abs(self.getX()-other.getX())+abs(self.getY()-other.getY()))

	def man_dist(self,other):
		# defines the function to get manhattan distance between points
		return math.sqrt((self.getX()-other.getX())**2+(self.getY()-other.getY())**2)

	
