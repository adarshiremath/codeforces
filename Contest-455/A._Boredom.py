# A. Boredom
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Alex doesn't like boredom. That's why whenever he gets bored, he comes up with games. One long winter evening he came up with a game and decided to play it.

# Given a sequence a consisting of n integers. The player can make several steps. In a single step he can choose an element of the sequence (let's denote it ak) and delete it, at that all elements equal to ak + 1 and ak - 1 also must be deleted from the sequence. That step brings ak points to the player.

# Alex is a perfectionist, so he decided to get as many points as possible. Help him.

# Input
# The first line contains integer n (1 ≤ n ≤ 105) that shows how many numbers are in Alex's sequence.

# The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105).

# Output
# Print a single integer — the maximum number of points that Alex can earn.

# Examples
# inputCopy
# 2
# 1 2
# outputCopy
# 2
# inputCopy
# 3
# 1 2 3
# outputCopy
# 4
# inputCopy
# 9
# 1 2 1 3 2 2 2 2 3
# outputCopy
# 10
# Note
# Consider the third test example. At first step we need to choose any element equal to 2. After that step our sequence looks like this [2, 2, 2, 2]. Then we do 4 steps, on each step we choose any element equals to 2. In total we earn 10 points.




n = int(input().strip())

a = list(map(int, input().strip().split()))


dit = dict()
for i in a:
	if i in dit:
		dit[i] += i
	else:
		dit[i] = i

count = 0
print(dit)
while(len(dit)>0):
	maxk = -1
	maxv = -1
	for key,values in dit.items():
		if values > maxv:
			maxk = key
			maxv = values
	count += maxv
	dit.pop(maxk)
	dit.pop(maxk + 1, None)
	dit.pop(maxk - 1, None)
	print(dit)

print(count)