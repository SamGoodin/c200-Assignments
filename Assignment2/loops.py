#Asterisk pyramid
for i in range(11, 0, -2):
    print(' '*int((12-i)/2) + "*"*i, end="")
    print()

#Sum of nums
sum = 0
step = 3
num = 1
while(num <= 100):
    sum += num
    num += step
    step += 2
print(sum)

#Donations
donations = [10.00, 12.00, 0.75, 5.23, 25.35, 14.53, 15.99, 8.00, 8.01, 0.25]
total = 0
for num in donations:
    total += num
if total > 100:
    print("Exceeded $100!!! Time to double $" + str(total) + "!")
    total *= 2
print(total)


'''For testing above code; please ignore below lines.
l = []
num = 1
step = 3
while(num <= 100):
    l.append(num)
    num += step
    step += 2
print(l)

ans = 0
for n in l:
    ans += n
print(ans)
'''