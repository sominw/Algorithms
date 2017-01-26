t1, t2, n = map(int, input().strip().split())
k = [t1, t2]
while len(k) != n:
    x = k[-2] + (k[-1]**2)
    k.append(x)
print (k[-1])
