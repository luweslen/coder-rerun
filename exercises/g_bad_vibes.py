n = int(input('').split()[0])
pr= []
while n > 0:
    n -= 1
    for m in input('').split():
        pr.append((m[1],m[0],m))
pr.sort()
for m in pr[::-1]:
    print(m[2])