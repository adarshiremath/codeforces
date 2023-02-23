# A. Cut Ribbon
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:

# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.

# Input
# The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.

# Output
# Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.

# Examples
# inputCopy
# 5 5 3 2
# outputCopy
# 2
# inputCopy
# 7 5 5 2
# outputCopy
# 2
# Note
# In the first example Polycarpus can cut the ribbon in such way: the first piece has length 2, the second piece has length 3.

# In the second example Polycarpus can cut the ribbon in such way: the first piece has length 5, the second piece has length 2.

import sys

n, a, b, c = list(map(int, input().strip().split()))
ans = 0
i = 1
a,b,c  = sorted([a,b,c], reverse=True)
j = 1
while(i*a <= n):
	j = 0
	while(i*a + j*b <= n):
		rem = n - (i*a + j*b)
		if(rem%c == 0):
			k = rem/c
			ans = max(ans, i+j+k)
			print(int(ans))
			sys.exit()
		j+=1
	i+=1


