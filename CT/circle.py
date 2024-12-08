from math import pi
class Circle:
    def __init__(self,center:list[int],radius:float) -> None:
        self.center=center
        self.radius=radius

    def compute_area(self)->float:
        self.area = self.radius**2*pi
        return self.area
    
    def print_area(self)->None:
        print(f"Der Kreis hat eine Fläche von {self.area} Quadratpixeln")

if __name__ == "__main__":
    circle = Circle(center=[0, 0], radius=0.5)
    circle.compute_area()  # Compute the area
    circle.print_area()  # Print the area