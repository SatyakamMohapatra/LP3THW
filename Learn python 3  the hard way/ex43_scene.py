from sys import exit
class Scene(object):
    """docstring fo Scene."""
    def enter(self):
        print("this scene is not yet configered")
        print("subclass is and implement the eenter method")
        exit(1)

class Death(Scene):
    """docstring fo Death."""
    pass

class CentralCorridor(Scene):
    """docstring for CentralCorridor"""
    pass

class LaserWeaponArmory(Scene):
    """docstring for LaserWeaponArmory"""
    pass

class TheBridge(Scene):
    """docstring for TheBridge"""
    pass

class EscapePod(Scene):
    """docstring for EscapePod"""
    pass

if __name__ == '__main__':
    main()
