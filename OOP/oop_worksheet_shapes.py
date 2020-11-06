class Shape():
    def __init__(self, my_colour_fill, my_colour_outline):
        self.colour_fill = my_colour_fill
        self.colour_outline = my_colour_outline
    #endprocedure

    def calculate_area(self,my_side):
        self.area = my_side ** 2
    #end procedure

#endclass

class Rectangle(Shape):
    def __init__(self, my_colour_fill, my_colour_outline, my_height, my_width):
        super().__init__(my_colour_fill,my_colour_outline)
        self.height = my_height
        self.width = my_width
    #end procedure

    def calculate_area(self):
        self.area = self.height*self.width
    #end procedure

#end class

class Circle(Shape):
    def __init__(self, my_colour_fill, my_colour_outline, my_diameter):
        super().__init__(my_colour_fill,my_colour_outline)
        self.diameter = my_diameter
    #end procedure

    def calculate_area(self):
        self.area = 3.1415 * (self.diameter / 2) ** 2
    #end procedure

#end class

rectangle1 = Rectangle("white","black",5,6)
circle1 = Circle("blue","orange",3)
rectangle1.calculate_area()
circle1.calculate_area()
print(rectangle1.area)
print(circle1.area)
