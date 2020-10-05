while True:
	if int(input()) < 1:
		break
	p = input().split()
	max = c = 0
	min = None
	while c < len(p):
		t = int(p[c]) + int(p.pop())
		try:
			if max < t:
				max = t
			if min > t:
				min = t
		except TypeError:
			min = t
		c += 1
	print(max,min)
			

			
				