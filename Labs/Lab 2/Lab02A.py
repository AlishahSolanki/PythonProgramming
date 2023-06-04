PI = 3.14159

print('Enter the radius of the cylinder in inches:', end=' ')
radius = float(input())

height = float(input('Enter the height of the cylinder in inches: '))

surface_area = 2 * PI * radius * (radius + height)

print('The surface area of the cylinder is', surface_area, 'square inches')
