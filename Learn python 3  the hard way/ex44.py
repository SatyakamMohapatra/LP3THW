class Parent(object):
    """docstring for Parent."""
    def Impl(self):
        print("Parent Object")

class Child(Parent):
    """docstring for Child."""
    def Impl(self):
        print("Child Object")


class ForeWheelr(Parent,Child):
    """docstring for Parent."""


pent = ForeWheelr().Impl()
