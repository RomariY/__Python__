from math import pi, radians

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def check_fun(self):
        if len(self.coor1) == 2 and len(self.coor2) == 2:
            return True
        else:
            raise NotImplementedError("input error")

    def distance(self):
        if self.check_fun():
            result = ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**(1/2)
            result = round(result, 2)
            return result
    
    def slope(self):
        if self.check_fun():
            result = (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
            result = round(result, 2)
            return result

# Coordinates
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())



class Cylinder():
    pi = pi
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = self.pi * self.radius**2 * self.height
        volume = round(volume, 2)
        return volume

    def surface_area(self):
        area = (2 * self.pi * self.radius * self.height) + (2 * self.pi * self.radius**2)
        area = round(area, 2)
        return area

# Cylinder
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
