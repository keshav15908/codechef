'''take input number of test cases
for each test case, take 2 inputs named
quantity and price
kg rs/kg
100 12
total expense = 100 x 12 = 1200
if expenses>1000 then give discoúnt 10%
new expense = 1200 - (10% of 1200)
1200*(10/100)'''
t=int(input())
for i in range(t):
    quantity,price=map(int, input().split(" "))
    total = quantity*price
    if quantity > 1000:
        total = total - total*(10/100)
    print(format(total, '.6f'))

