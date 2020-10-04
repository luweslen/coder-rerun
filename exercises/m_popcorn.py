import math

data = input()
newData = []
qtdPipoca = input()
newQtdPipoca = []

data = data.split()

for d in data:
    newData.append(int(d))

qtdPipoca = qtdPipoca.split()

for p in qtdPipoca:
    newQtdPipoca.append(int(p))

m = max(newQtdPipoca)
x = math.pow(2, int(math.ceil(math.log2(m/newData[2]))))
mi = x/2

sa = 0
cont = 0
aux = 1
ret = 0
v = False

while (aux != 0):
    i = 0
    while i < newData[0]:
        if(math.ceil(newQtdPipoca[i]*1.0/newData[2]) > x or cont == newData[1]):
            cont = newData[1] + 1
            break
        if(math.ceil(float((sa + newQtdPipoca[i])/(newData[2] * 1.0))) <= x):
            sa += newQtdPipoca[i]
        else:
            cont += cont
            sa = newQtdPipoca[i]

        i += 1

    cont += cont

    aux = (x-mi) / 2

    if (cont <= newData[1]):
        ret = x
        v = True
        x -= aux
    elif(v):
        mi = x
        x += aux
    else:
        aux = 1
        mi = x
        x = x*2

print(ret)
