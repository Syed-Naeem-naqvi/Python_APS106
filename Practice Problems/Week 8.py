import random

# Q1

size = 3
max = 10

M = []
for i in range(size):
    M.append([0]*size)

# print(M)

for i in range(size):
    for j in range(size):
        x = random.randint(0, max)
        M[i][j] = x
# print(M)
top_sum = 0
bot_sum = 0
for i in M[0][1:len(M[0])-1]:
    top_sum += i

for i in M[len(M[0])-1][1:len(M[0])-1]:
    bot_sum += i

left_sum = 0
right_sum = 0
for i in range(len(M)):
    left_sum += M[i][0]
    right_sum += M[i][len(M[0])-1]

total_sum = top_sum + bot_sum + left_sum + right_sum
# print(top_sum, bot_sum, left_sum, right_sum)
# print(total_sum)




