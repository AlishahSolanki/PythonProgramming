r = float(input('Enter interest rate as a percent: '))
r /= 100

n = int(input('Enter number of compounding periods per year: '))

eff_yield = pow((1 + r/n), n) - 1
eff_yield *= 100

print('{:.3f}% interest with {} compounding periods has an Effective Yield of {:.3f}%'.format(r*100, n, eff_yield))
