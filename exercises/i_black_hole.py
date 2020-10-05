n = int(input())
i = 0
while i < n:
	i += 1
	j = 0
	pos = []
	sis = []
	while j < 4:
		j += 1
		x,y = input().split()
		pos.append((eval(x),eval(y)))
		try:
			a = -(pos[j+2][0] - pos[j][0])/(pos[j+2][1] - pos[j][1])
			b = ((pos[j+2][1] + pos[j][1])/2) - a*(pos[j+2][0] + pos[j][0])/2
			sis.append((a,b))
		except IndexError:
			continue
		except ZeroDivisionError:
			sis.append((pos[j][0] + pos[j+2][0])/2)
	a1 = b1 = x1 = a2 = b2 = x2 = None
	try:
		a1,b1 = sis[0]
	except Exception:
		x1 = sis[0]
	try:
		a2,b2 = sis[1]
	except Exception:
		x2 = sis[1]
	if x2 
	print('Caso #%d: %.02f %.02f'%(i,2,3.5))