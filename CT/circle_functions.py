import math

r  = float(input(f"Please enter the radius of your circle: "))

def calculate_circumference(r:float)->float:
    c = math.pi * (r)*2
    return c

def calculate_area(r:float)->float:
    a = math.pi*(r**2)
    return a

def print_c_and_a_(r:float)->float:
    c=(calculate_circumference(r))
    print(f"Circumference: {c:.2f}")
    a=(calculate_area(r))
    print(f"Area: {a:.2f}")

print_c_and_a_(r)
