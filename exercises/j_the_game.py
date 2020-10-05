
perdas = 'JOGO','PERDI'
n = int(input())
while n > 0:
	n -= 1
	t = input().upper()
	m = 0
	while len(t) > 0:
		c = len(t)
		g = 0
		for p in perdas:
			try:
				r = t.index(p) + len(p)
				if r < c:
					c = r
			except ValueError:
				pass
		l = c
		while c > 0:
			c -= 1
			g += t[c].isalpha()
		if g > m:
			m = g
		t = t[l:]
	print(m)
		