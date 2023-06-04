import random

class RandomError(Exception):
    """A custom exception for this code block"""
    pass

def random_errors(p_error):
    if random.random() <= p_error:
        raise RandomError('Error raised with {:0.2f} likelihood'.format(p_error))

try:
    random_errors(0.5)
    print('No errors occurred!')
except RandomError as errmsg:
    print('RandomError:', errmsg)
finally:
    print('This runs no matter what!')

