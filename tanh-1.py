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
print(estimate_h_tan_inv(x_c, eps_c))











