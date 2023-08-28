import math as m


# e^x = x^n/n!

true_value = m.sqrt(m.e)

sum_ = 0
n = 0
x = 1/2
while n < 20:
    sum_ += 1/2 ** n / m.factorial(n)
    n += 1


E = true_value - sum_
print("The approximation:", sum_, '\n ', 'The true value:', true_value)
print("The Error is: ", E)


