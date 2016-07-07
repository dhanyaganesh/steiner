from nose.tools import *
from steiner.steiner import steiner
from steiner.prim_mst import *

def test_stein():
	zero = Position(0,0)
	one = Position(1,1)
	two = Position(2,-2)
	three = Position(3,-1)
	
	assert_equal(wirelength(steiner([zero,one,two,three])),6)
