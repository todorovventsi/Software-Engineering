class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.diameter / 2

    def calculate_area(self):
        return Circle.__pi * (self.diameter / 2) ** 2

    def calculate_area_of_sector(self, angle):
        r_angle = angle * Circle.__pi / 180
        return ((self.diameter / 2) ** 2) * r_angle / 2


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")