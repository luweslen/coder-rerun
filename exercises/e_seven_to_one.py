n = int(input())
e = 1
s = 0
total = ""
while e <= n:
    total += str(e)
    print(total)
    e += 1

for t in total:
    if(t == "1" or t == "7"):
        s += 1

print(s)
