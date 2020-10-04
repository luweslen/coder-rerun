qtd = int(input())
end = 0

while end < qtd:
    k = int(input())

    coef = 0
    e = 1

    while e < 100000:
        coef += 24*e
        e *= 10

    k = k/coef

    if not float(k).is_integer():
        print("impossivel")
        continue

    digitos = [3, 2, 1, 0]

    finish = False
    index = 0
    print(k)
    while not finish:
        soma = 0
        for d in digitos:
            soma += d

        print(k - soma)
        if k - soma < 10:
            digitos.append(int(k - soma))
            if(digitos[0] != digitos[1] != digitos[2] != digitos[3] != digitos[4]):
                digitos.sort()
                print(str(digitos).replace('[', '{').replace(']', '}'))
                finish = True
                break
        else:
            if(digitos[0] < 9 and digitos[1] == 2 and digitos[2] == 1 and digitos[3] == 0):
                digitos[0] += 1
            if(digitos[0] == 9 and digitos[1] < 8 and digitos[2] == 1 and digitos[3] == 0):
                digitos[1] += 1
            if(digitos[0] == 9 and digitos[1] == 8 and digitos[2] < 7 and digitos[3] == 0):
                digitos[2] += 1
            if(digitos[0] == 9 and digitos[1] == 8 and digitos[2] == 7 and digitos[3] < 6):
                digitos[3] += 1
