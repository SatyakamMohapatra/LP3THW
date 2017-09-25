from nose.tools import *
from ex47.game import Room

def test_room():
	gold = Room("GoldRoom","""This room has Gold
						inside it""")
	assert_equals(gold.name,"GoldRoom")
	assert_equals(gold.paths,{})

def test_room_path():
	center = Room("Center","This is center Room")
	north = Room("Center","This is north Room")
	center.app_paths({"center":center,"north":north})
	assert_equals(center.go("center"),center)
	assert_equals(center.go("north"),north)
