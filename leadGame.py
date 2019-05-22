N = int(input())

scorecard = []
for i in range(N):
    score = list(map(int , input().split(" ")))
    scorecard.append(score)
# scorecard = [[140,82],[89,134],[90,110],[112,106],[88,90]]

commanscorecard = [[scorecard[0][0],scorecard[0][1]]]
for i in range(1,N):
    player1 = scorecard[i][0] + commanscorecard[i-1][0]
    player2 = scorecard[i][1] + commanscorecard[i-1][1]
    entry = [player1 , player2 ]
#commanscorecard = [[140,82],[229 216],[319,326],[431,432],[519,522]]
maxLead = [0,0]
for i in range (N):
    newLead = abs(commanscorecard[i][0] - commanscorecard[i][1])
    if newLead>maxLead[1]:
        maxLead[0] = i + 1
        maxLead[1] = newLead
print(maxLead[0], maxLead[1])




