pr = []
while n > 0:
    n -= 1
    pr.append(input(''))
n = int(input(''))
while n > 0:
    n -= 1
    p = input('')
    qtd = max = 0
    for c in pr:
        if c.find(p) == 0:
            qtd += 1
            l = len(c)
            if l > max:
                max = l
    if qtd == 0:
        print(-1)
    else:
        print(qtd, max)
