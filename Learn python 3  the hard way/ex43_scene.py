from sys import exit
class Scene(object):
    """docstring fo Scene."""
    def enter(self):
        print("this scene is not yet configered")
        print("subclass is and implement the eenter method")
        exit(1)

class Death(Scene):
    """docstring fo Death."""
    def enter(self):
        print("You are DEAD")
        exit(1)

class CentralCorridor(Scene):
    """docstring for CentralCorridor"""
    def enter(self):
        print("in CentralCorridor")
        result = input("1 or 0 >")
        if result == "1":
            return("LaserWeaponArmory")
        else:
            return("Death")


class LaserWeaponArmory(Scene):
    """docstring for LaserWeaponArmory"""
    def enter(self):
        print("in LaserWeaponArmory")
        result = input("1 or 0 >")
        if result == "1":
            return("TheBridge")
        else:
            return("Death")

class TheBridge(Scene):
    """docstring for TheBridge"""
    def enter(self):
        print("in TheBridge")
        result = input("1 or 0 >")
        if result == "1":
            return("EscapePod")
        else:
            return("Death")

class EscapePod(Scene):
    """docstring for EscapePod"""
    def enter(self):
        print("You win!!1")
        exit(1)

if __name__ == '__main__':
    main()
