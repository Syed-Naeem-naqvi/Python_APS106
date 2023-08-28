import random as r

x = 1/4
lnx = 0
term = 1
while term < 20:
    lnx += ((-1)**(term-1)*(x-1)**term)/term
    print(lnx)
    term += 1
# print(lnx)


def estimate_h_tan_inv(x, eps):

    """ (float, float) -> float
    Given some x: (-1<x<1), and some epsilon > 0, Returns the sum of
    the series representation of the inverse hyperbolic tan function when
    change from adding the next term is less than epsilon
    """

    # Power value
    n = 1

    if x >= 1 or x <= -1:
        x = float(input("Please pick another x: "))

    # sum to next term
    next_t = 0
    less_than_eps = False

    # Run two series simultaneously, one ahead by one term
    while not less_than_eps:
        next_t += x**n/n
        cur_t = next_t - x**n/n
        n += 2
        term_diff = abs(cur_t-next_t)
        if term_diff < eps:
            less_than_eps = True

    return cur_t


# Inputs
x_c = 2
eps_c = 0.000001
# print(estimate_h_tan_inv(x_c, eps_c))


# What is the ratio of the number of times the dice roll the same number over the number of trials?

sames = 0
count = 0
while count < 1000:
    dice_1 = r.randint(1, 6)
    dice_2 = r.randint(1, 6)
    if dice_1 == dice_2:
        sames += 1
    count += 1
sames_ratio = sames / count
# print(sames_ratio)


def fib_seq_and_term_ratios(n):
    """ (int) -> int
    Prints the first n terms of the
    fibonacci sequence. n > 2.
    0, 1, 1, 2, 3, 5, 8, 11, 21
    """
    tn_1 = 0
    tn_2 = 1
    start = 1
    series = '0, '
    term_ratio_str = ''
    while start < n:
        tn_2copy = tn_2
        tn_2 = tn_2 + tn_1
        tn_1 = tn_2copy
        series += str(tn_1) + ', '
        term_ratio_str += str(round((tn_2/tn_1),4)) + ', '
        start += 1

    print(series)
    print(term_ratio_str)


fib_seq_and_term_ratios(6)









