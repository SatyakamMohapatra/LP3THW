from nose.tools import *
from lexicon.lexicon import Lexicon


def test_directions():
	lexicon=Lexicon()
	assert_equal(lexicon.scan("north"),[('direction','north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])

def test_verbs():
	pass
