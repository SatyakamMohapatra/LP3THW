import ex43_map
class Engine(object):
    """docstring for Engine"""

    def __init__(self,map_scene):
        self.map_scene = map_scene

    def play(self):
        current_scene = self.map_scene.opening_scene()
        final_scene = self.map_scene.next_scene("EscapePod")

        while current_scene != final_scene:
            next_scene = current_scene.enter()
            current_scene = self.map_scene.next_scene(next_scene)
            #current_scene.enter()

        final_scene.enter()

if __name__ == '__main__':
    main()
