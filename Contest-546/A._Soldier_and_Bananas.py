# A. Soldier and Bananas
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).
#
# He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?
#
# Input
# The first line contains three positive integers k, n, w (1  ≤  k, w  ≤  1000, 0 ≤ n ≤ 109), the cost of the first banana, initial number of dollars the soldier has and number of bananas he wants.
#
# Output
# Output one integer — the amount of dollars that the soldier must borrow from his friend. If he doesn't have to borrow money, output 0.
#
# Examples
# inputCopy
# 3 17 4
# outputCopy
# 13



line = input().strip().split()
k, n, w = int(line[0]), int(line[1]), int(line[2])
val = (w*(w+1)*k)//2-n
print(val if val>=0 else 0)
