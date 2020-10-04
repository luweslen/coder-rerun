numberMovements = int(input())
cupStart = input().upper()
end = 0
cups = [False, False, False]
copos = 'ABC'
cups[copos.find(cupStart)] = True

while end < numberMovements:
    move = int(input())
    end += 1
    if(move == 1):
        temp = cups[0]
        cups[0] = cups[1]
        cups[1] = temp

    if(move == 2):
        temp = cups[1]
        cups[1] = cups[2]
        cups[2] = temp

    if(move == 3):
        temp = cups[0]
        cups[0] = cups[2]
        cups[2] = temp

print(copos[cups.index(True)])
