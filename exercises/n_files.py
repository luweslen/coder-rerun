while True:
	f = int(input())
	if f == 0:
		break
	arq = []
	chaves = set()
	c = 0
	while f > c:
		arq.append(input())
		c += 1
	print(arq)
	for c in arq:
		i = len(c)
		while i > 0:
			f = i
			while f > 0:
				f -= 1
				p = True
				t = c[f:i]
				for d in arq:
					p = p and (t in d)
					if not p: break;
				if p:
					chaves.add(t)
				else:
					f = 0
			i -= 1
	print(len(chaves))