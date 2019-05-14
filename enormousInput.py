''' take 2 vàriable n, k as input.
run loop n time and each time, take an iñput t. if t is divisible by k then increase the count by one. after exitin thw loop, print the value of count.'''
n,k= map(int, input().split(" "))
count=0
for i in range(n):
    t = int(input())
    if t%k==0:
        count = count + 1
print(count)
