T = int(input())
for t in range(T):
    n = int(input())
    answer = 1
    for i in range(1, n+1):
        answer = answer*i
        print(answer)
