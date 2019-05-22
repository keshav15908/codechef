n = int(input("give me your number buddy: ")
reverse=0
while (n > 0):
    dig = n % 10
    reverse= reverse * 10 + dig
    m=n//10
print(" reverse of the number: ", reverse)
