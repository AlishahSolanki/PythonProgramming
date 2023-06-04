class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        ''' clock arithmetic initializer '''
        self.seconds  = seconds % 60
        total_minutes = minutes + (seconds // 60)
        self.minutes  = total_minutes % 60
        self.hours    = (hours + (total_minutes // 60)) % 24

    def print_clock(self):
        '''
        leading 0 in format statement puts a 0 in each element if
        necessary so that every field is 2 decimals wide
        '''
        print('{:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds))

    def add_clocks(self, clock2):
        '''
        no change to self on clock2, return a new Clock instance
        no checks on attribute sums, the __init__ will handle it
        '''
        seconds = self.seconds + clock2.seconds
        minutes = self.minutes + clock2.minutes
        hours   = self.hours   + clock2.hours
        return Clock(hours, minutes, seconds) # return new Clock instance with new values

my_clock = Clock()  # calls the constructor
print('My clock is: ', my_clock)
print('Type is:', type(my_clock))
print(dir(my_clock))

new_clock = Clock(10, 15, 30)
# print(new_clock.hours, new_clock.minutes, new_clock.seconds)
new_clock.print_clock()

tst_clock = Clock(23, 59, 60)
# print(tst_clock.hours, tst_clock.minutes, tst_clock.seconds)
tst_clock.print_clock()

c1 = Clock(10, 59, 59)
c2 = Clock (1, 1, 1)
c3 = c1.add_clocks(c2)
c1.print_clock()
c2.print_clock()
c3.print_clock()
