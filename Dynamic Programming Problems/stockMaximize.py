def maximumProfit(l):
	n = len(l)
	bestAvailableStock = l[n-1]
	currProfit = 0;
	for i in range(n-2,-1,-1):
		if (l[i] > bestAvailableStock):
			bestAvailableStock = l[i]
		else:
			currProfit += (bestAvailableStock - l[i])
	return currProfit

t = int(input())
list = []
for i in range(t):
	N = int(input())
	list.append([int(x) for x in input().split()])
for l in list:
	print (maximumProfit(l))
