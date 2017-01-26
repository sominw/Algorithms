n,m = map(int, input().strip().split())
c = list(map(int, input().split()))


table = [[0 for x in range(m)] for x in range(n+1)]
for i in range(m):
	table[0][i] = 1;

for i in range(1,n+1):
	for j in range(m):
		x = table[i - c[j]][j] if i-c[j] >= 0 else 0
		y = table[i][j-1] if j >= 1 else 0

		table[i][j] = x + y;
print(table[n][m-1])
