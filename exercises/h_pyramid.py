try:
	while True:
		v = input('').split()
		x = len(v)
		while x > 0:
			x -= 1
			v[x] = float(v[x])
		x = ((v[0]/2) + v[1])*v[2]/v[3]
		print('%.05f'%x)
except ZeroDivisionError:
	pass
