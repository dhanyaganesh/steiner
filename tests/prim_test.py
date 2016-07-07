from nose.tools import *
from steiner.prim_mst import *

def test_single_point():
	zero = Position(0,0)
	#mst of a single point is null
	assert_equal(wirelength(mst([[zero]])),0)

def test_straight_line():
	zero = Position(0,0)
	one = Position(1,0)
	two = Position(2,0)
	result = [[one,zero],[two,one]]
	assert_equal(wirelength(mst([zero,one,two])),2)

def test_four_points():
	zero = Position(0,0)
	one = Position(1,0)
	two = Position(0,-3)
	ten = Position(10,5)
	result = [[one,zero],[two,zero],[ten,one]]
	assert_equal(wirelength(mst([zero,one,two,ten])),1+3+14)
