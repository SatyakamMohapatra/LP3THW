class Lexicon(object):

    def __init__(self):
        self.paths={}

    def scan(self,direction):
        return self.get_path_tuple(direction)

    def get_path_tuple(self,direction):
        direction_array = direction.split()
        temp_array = []
        map_path = self.find_element_map(direction_array)
        for item in direction_array:
            if item in map_path.keys():
                v = map_path.get(item)
                temp_array.append((v,item))
            elif self.is_int(item):
                temp_array.append(('number',int(item)))
            else:
                temp_array.append(('error',item))
        return temp_array

    def get_lexicon_map(self):
        way_array = ['north','south','east','west']
        verb_array = ['go','kill','eat']
        stop_array = ['the', 'in', 'of']
        noun_array = ['bear', 'princess']
        lexicon_map = {'direction':way_array,
                       'verb':verb_array,
                       'stop':stop_array,
                       'noun':noun_array}
        return lexicon_map;

    def find_element_map(self,direction_array):
        element_map = self.get_lexicon_map();
        paths_map = {}
        for k,v in element_map.items():
            for item in v:
                if item in direction_array:
                    paths_map.update({item:k})
        return paths_map

    def is_int(self,item):
        bull = True
        try:
            int(item)
        except Exception as e:
            bull = False
        return bull;
