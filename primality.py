T = int(input())
for i in range(T):
    N = int(input())
    for j in range(2, N//2+1):
        if (N%j==0):
            print("no")
            break
        elif (j==N//2):
            print("yes")
