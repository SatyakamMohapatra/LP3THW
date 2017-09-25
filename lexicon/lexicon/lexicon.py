class Lexicon(object):

    def __init__(self):
        self.paths={}

    def scan(self,direction):
        return self.get_path_tuple(direction)

    def add_paths(self,paths):
        self.paths.update(paths)

    def get_path_tuple(self,direction):
        direction_array = direction.split()
        temp_array = []
        temp_array.append([('direction',direc) for direc in direction_array if direc in ])
        temp_array = [('direction',direc) for direc in direction_array if direc in verb_array]
        return temp_array

    def get_lexicon_map():
        way_array = ['north','south','east','west']
        verb_array = ['go','kill','eat']
        lexicon_map = {'direction':way_array,
                       'verb':verb_array}
        return lexicon_map;

    def find_element_map =(direction_array):
        element_map = get_lexicon_map();
        for k,v in element_map.items():
