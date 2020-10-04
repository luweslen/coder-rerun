numberMovements = int(input())
cupInitial = input().upper()

cups = [False, False, False]
nameCups = 'ABC'
cups[nameCups.find(cupInitial)] = True

end = 0

while end < numberMovements:
    move = int(input())
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

    end += 1

print(nameCups[cups.index(True)])
