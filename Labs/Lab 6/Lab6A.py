import math

def calc_hex_area(a):
    return (3 * math.sqrt(3) * pow(a, 2))

def calc_side_area(a, h):
    return (6 * a * h)

def display_surface_area(hex_area, side_area):
    print('The total surface area is {:.3f} square feet'.format(hex_area + side_area))

h = float(input('Enter height of hexagonal prism in feet: '))
a = float(input('Enter length of the base edge in feet  : '))

hex_area = calc_hex_area(a)
print('Surface area of hexagonal faces is {:.3f} square feet'.format(hex_area))

side_area = calc_side_area(a, h)
print('Surface area of rectangular sides is {:.3f} square feet'.format(side_area))

display_surface_area(hex_area, side_area)

