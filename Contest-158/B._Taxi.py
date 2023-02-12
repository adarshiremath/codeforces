# B. Taxi
# time limit per test3 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# After the lessons n groups of schoolchildren went outside and decided to visit Polycarpus to celebrate his birthday. We know that the i-th group consists of si friends (1 ≤ si ≤ 4), and they want to go to Polycarpus together. They decided to get there by taxi. Each car can carry at most four passengers. What minimum number of cars will the children need if all members of each group should ride in the same taxi (but one taxi can take more than one group)?
#
# Input
# The first line contains integer n (1 ≤ n ≤ 105) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.
#
# Output
# Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.
#
# Examples
# inputCopy
# 5
# 1 2 4 3 3
# outputCopy
# 4
# inputCopy
# 8
# 2 3 4 4 2 1 3 1
# outputCopy
# 5
# Note
# In the first test we can sort the children into four cars like this:
#
# the third group (consisting of four children),
# the fourth group (consisting of three children),
# the fifth group (consisting of three children),
# the first and the second group (consisting of one and two children, correspondingly).
# There are other ways to sort the groups into four cars.
#



def main():
	from sys import stdin, stdout

	n = int(stdin.readline())
	s = map(int, stdin.readline().split())

	cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0

	for x in s:
		if x == 1: cnt1  += 1
		elif x == 2: cnt2  += 1
		elif x == 3: cnt3  += 1
		else: cnt4  += 1

	ans = cnt4

	ans += cnt2 // 2
	cnt2 = cnt2 % 2

	if cnt1 <= cnt3:
		ans += cnt1
		ans += cnt2
		ans += cnt3 - cnt1
	else:
		ans += cnt3
		cnt1 -= cnt3
		ans += cnt1 // 4
		cnt1 %= 4

		rem = cnt1 + cnt2 * 2
		if rem > 0:
			ans += 1 if rem <= 4 else 2

	stdout.write(str(ans) + '\n')

if __name__ == '__main__':
	main()
