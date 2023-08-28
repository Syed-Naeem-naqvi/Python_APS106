x = 1/4
lnx = 0
term = 1
while term < 20:
    lnx += ((-1)**(term-1)*(x-1)**term)/term
    print(lnx)
    term += 1
# print(lnx)

