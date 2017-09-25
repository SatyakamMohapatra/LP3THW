class Room(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.paths={}

    def go(self, direction):
        return self.paths.get(direction,None)

    def app_paths(self,paths):
        return self.paths.update(paths)
