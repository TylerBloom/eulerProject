#! /usr/bin/python

a = []

digits = ['0','1','2','3','4','5','6','7','8','9']

for i in digits:
	for n in digits:
		if i == n:
			continue
		for p in ['0','2','4','6','8']:
			if p == i or p == n:
				continue
			a.append(i+n+p)

b = []
for p in range(len(a)):
	for q in digits:
		if q in a[p]:
			continue
		s = a[p][1:3] + q
		n = int(s)
		if 3*(n/3) == n:
			b.append(a[p] + q)

c = []
for p in range(len(b)):
	zero = '0' in b[p]
	five = '5' in b[p]
	if not zero:
		c.append(b[p] + "0")
	if not five:
		c.append(b[p] + "5")

d = []
for p in range(len(c)):
	for q in digits:
		if q in c[p]:
			continue
		s = c[p][3:5] + q
		n = int(s)
		if 7*(n/7) == n:
			d.append(c[p] + q)

e = []
for p in range(len(d)):
	for q in digits:
		if q in d[p]:
			continue
		s = d[p][4:6] + q
		n = int(s)
		if 11*(n/11) == n:
			e.append(d[p] + q)

f = []
for p in range(len(e)):
	for q in digits:
		if q in e[p]:
			continue
		s = e[p][5:7] + q
		n = int(s)
		if 13*(n/13) == n:
			f.append(e[p] + q)

g = []
for p in range(len(f)):
	for q in digits:
		if q in f[p]:
			continue
		s = f[p][6:8] + q
		n = int(s)
		if 17*(n/17) == n:
			g.append(f[p] + q)

answer = 0
for p in range(len(g)):
	for q in digits:
		if not q in g[p]:
			answer += int(q + g[p])

print answer

