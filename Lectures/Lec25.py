# Lec25

# different variables pointing to the same location in memory: aliasing
# Aliases refer to the same object

# += -> change in place

# l = l + ['Hi'] -> using concat creates a new value
# l += ['Hi'] -> Augmented ones change in place
# pass mutable to function: we pass a reference, so the changes can appear outside the function, unintentionally

def reverse(lst):
    new_l = lst
    lst_len = len(lst)
    for x in range(lst_len):
        new_l[x] = (lst[lst_len-1-x])
    return new_l


def reverse2(lst):
    new_l = lst.copy()
    lst_len = len(lst)
    for x in range(lst_len):
        new_l[x] = (lst[lst_len-1-x])
    return new_l


l = ['a','b','c']
# mylist and lst point to the same thing. whatever changes made to the variable are visible outside the function aswell
# Make a copy of the mutable value

# lose the first two elements, were screwed

print(reverse2(l))
# keyword args come last

# positional or keyword: param1, param2
# positional only: param3=

# use args and kwargs

# for variable number of arguments

# * and / introduce list of parameters
# m, n = positional as they dont have default values


def func(m, n):
    for i in range(m):
        i+=i
    return i*n


def func2(m, n=1):
    k = 0
    for i in range(m):
        k += i
    return k*n


print(func2(5))

# put * before ** parameters
# *args -> variable of type tuple
# **kwargs -> variable of type dict, can use var.items() on it
# named and keyword attributes go at the end var=x

# my_sum_any_w_start_value can be called without a start vale, or with a different one


























