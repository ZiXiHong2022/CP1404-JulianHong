for i in range(1, 21, 2):
    print(i, end=' ')
print()
for y in range(0,101,10):
    print(y, end=' ')
print()

for a in range(20,0,-1):
    print(a, end=' ')
print()

num_star = int(input('number of star:'))
print(num_star * "*")
number1 = int (input('number :'))
for i in range(number1):
    print(i * "*",end="")
    for b in range(num_star):
        print(b * '*')
        break
