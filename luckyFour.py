T = int(input())
for i in range(T):
    x = input()
    count = 0
    for j in range(len(x)):
        if x[j]=='4':
            count = count + 1
    print(count)
