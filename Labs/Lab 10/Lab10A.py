from math import sqrt

print('Let\'s solve a quadratic equation a*x**2 + b*x + c = 0')
done = False
while not done:
    try:
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))

        discriminant = b**2 - 4*a*c
        root_of_discriminant = sqrt(discriminant)
        roots = ((-b - root_of_discriminant)/(2*a), (-b + root_of_discriminant)/(2*a))
        print('The roots are %g and %g' % roots)
        done = True # so we can exit the loop
    except ZeroDivisionError as errmsg:
        print('ZeroDivisionError:', errmsg)
        print('The first coefficient cannot be zero!')
    except ValueError as errmsg:
        print('ValueError:', errmsg)
    except Exception as errmsg:
        print('The exception message is:', errmsg)
        print('Please try again')
print('Hope you enjoyed this program')

