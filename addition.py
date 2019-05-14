##print("hów many test cases do you want?")
T = int(input())
##T = map(int, input())
for i in range(T):
    ##print("enter values of A and B")
    A, B = map(int, input().split(" "))
    SUM = A + B
    print(SUM)
