def f1(x):
    x[2] = 'banana'
    return


def f2(n):
    my_list[2] = 'banana'
    return


my_list = [1,2,3]
f2(my_list)
print(my_list)

# Changes inside are visible outside, function gets a reference to object, NOT a copy


def f3(x):
    return x*2


l1 = [[1,2], [3,4]]
print(f3(l1))


def func2(my_input):
    my_input = my_input + my_input


x = [[1, 2], [2, 3]]
print(x)
func2(x)
print(x)


# Gets a copy

def func(my_input):
    my_input *= 2


x = 2
func(x)
print(x)


def f(x, y=2):
    return x * y


print(f(2))
print(f(2,1))

