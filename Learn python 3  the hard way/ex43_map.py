import ex43_scene
class Map(object):
    """docstring for map_scene."""
    Scene ={
    "CentralCorridor":ex43_scene.CentralCorridor(),
    "LaserWeaponArmory":ex43_scene.LaserWeaponArmory(),
    "TheBridge":ex43_scene.TheBridge(),
    "EscapePod":ex43_scene.EscapePod(),
    "Death":ex43_scene.Death()
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,next_scene):
        var = self.Scene.get(next_scene)
        return var

    def opening_scene(self):
        return self.next_scene(self.start_scene)

if __name__ == '__main__':
    main()
