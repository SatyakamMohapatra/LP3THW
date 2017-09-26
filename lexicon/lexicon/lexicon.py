class Lexicon(object):

    def scan(self,direction):
        direction_array = [i.lower() for i in direction.split()]
        temp_array = []
        map_path = self.find_element_map(direction_array)
        for item in direction_array:
            if item in map_path.keys():
                temp_array.append((map_path.get(item),item))
            elif self.is_int(item):
                temp_array.append(('number',int(item)))
            else:
                temp_array.append(('error',item))
        return temp_array

    def get_lexicon_map(self):
        lexicon_map = {'direction':['north','south','east','west'],
                       'verb'     :['go','kill','eat'],
                       'stop'     :['the', 'in', 'of'],
                       'noun'     :['bear', 'princess']}
        return lexicon_map;

    def find_element_map(self,direction_array):
        paths_map = {}
        for k,v in self.get_lexicon_map().items():
            for item in v:
                if item.lower() in direction_array:
                    paths_map.update({item:k})
        return paths_map

    def is_int(self,item):
        try:
            int(item)
        except Exception as e:
            return False
        return True;
