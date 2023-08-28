speeds = [20, 50, 80, 110, 40, 50]
count = 0
for speed in speeds:
    if speed > 60:
        print('Speeding: ', speed)
        count += 1

perc = 100*(count/len(speeds))
print('Speeding', round(perc,3), '% of the time')

L = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(L)//2):
    print(L[i])

print('_______')

for i in range(len(L)//2, len(L)):
    print(L[i])


# first = L[0]
# for i in range(len(L)-1):
#     L[i] = L[i+1]
#     L[-1] = first
#
# print(L)

for i in range(10,13):
    for j in range(1,5):
        print(i, j)

L = [[70,70,70],[80,80,80],[90,90,90]]
avgs = []
for i in range(len(L)):
    for j in i:

print(avgs)




