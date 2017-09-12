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
        print(start_scene)
        return self.Scene.get("start_scene")

    def next_scene(self,next_scene):
        pass

    def opening_scene(self):
        pass

if __name__ == '__main__':
    main()
