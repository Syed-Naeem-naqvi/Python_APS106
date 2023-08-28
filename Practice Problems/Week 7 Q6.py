box_score = [["MTL", [1,0,0,1]], ["TOR", [1,0,1,2]], "TOR"]
goal_sum = False
correct_winner = False

for i in range(len(box_score)-1):
    print(box_score[i][1])
    if box_score[i][1][0] + box_score[i][1][1] + box_score[i][1][2] == box_score[i][1][3]:
        goal_sum = True
    else:
        goal_sum = False

print(goal_sum)

winning_team = ''
if box_score[0][1][3] > box_score[1][1][3]:
    winning_team = box_score[0][0]
elif box_score[0][1][3] < box_score[1][1][3]:
    winning_team = box_score[1][0]
else:
    winning_team = 'Tie'

if winning_team == box_score[2]:
    correct_winner = True
else:
    correct_winner = False
print(correct_winner)

check_result = goal_sum and correct_winner
print(check_result)



