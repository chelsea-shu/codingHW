from math import pi


class Cylinder:

    """Write code here to define a class Cylinder

    Define a class Cylinder with the following features:

    1.  a function to initialize. this should accept a radius and
        a height. If not specified, both should default to 1.

    """
    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    """    
    3.  an accessor function to get the radius, and one for the height.
        eg: get_radius(self) or getRadius(self)
    """
    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

    """
    4.  a mutator function to change the radius, and one for the height.
        eg: set_height(self, h) or setHeight(self, h)
    """
    def set_radius(self, r):
        self.radius = r

    def set_height(self, h):
        self.height = h

    """     
    5.  a function to get the surface area of one of the bases using
        the formula pi * r ^ 2
    """
    def get_surface_area(self):
        return pi * self.radius ** 2

    """
    6.  a function to get the curved surface area using the formula
        2 * pi * r * h
    """
    def get_curved_surface_area(self):
        return 2 * pi * self.radius * self.height

    """
    7.  a function to get the total surface area that calls functions
        in points 5 and 6 with the formula
        total surface area = curved surface area + 2 * base area
    """
    def get_total_sa(self):
        return self.get_curved_surface_area() + 2 * self.get_surface_area() # You can call the other arguments by just
                                                                                # saying self.function()
    def __str__(self):

        """This function is used to print details about the cylinder.
        This returns the radius and height when print(Cylinder()) is
        called.
        """

        return 'Cylinder with Radius = {}, ' \
               'and Height =  {}'.format(self.radius, self.height)
