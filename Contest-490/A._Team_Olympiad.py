# A. Team Olympiad
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# The School №0 of the capital of Berland has n children studying in it. All the children in this school are gifted: some of them are good at programming, some are good at maths, others are good at PE (Physical Education). Hence, for each child we know value ti:

# ti = 1, if the i-th child is good at programming,
# ti = 2, if the i-th child is good at maths,
# ti = 3, if the i-th child is good at PE
# Each child happens to be good at exactly one of these three subjects.

# The Team Scientific Decathlon Olympias requires teams of three students. The school teachers decided that the teams will be composed of three children that are good at different subjects. That is, each team must have one mathematician, one programmer and one sportsman. Of course, each child can be a member of no more than one team.

# What is the maximum number of teams that the school will be able to present at the Olympiad? How should the teams be formed for that?

# Input
# The first line contains integer n (1 ≤ n ≤ 5000) — the number of children in the school. The second line contains n integers t1, t2, ..., tn (1 ≤ ti ≤ 3), where ti describes the skill of the i-th child.

# Output
# In the first line output integer w — the largest possible number of teams.

# Then print w lines, containing three numbers in each line. Each triple represents the indexes of the children forming the team. You can print both the teams, and the numbers in the triplets in any order. The children are numbered from 1 to n in the order of their appearance in the input. Each child must participate in no more than one team. If there are several solutions, print any of them.

# If no teams can be compiled, print the only line with value w equal to 0.

# Examples
# inputCopy
# 7
# 1 3 1 3 2 1 2
# outputCopy
# 2
# 3 5 2
# 6 7 4
# inputCopy
# 4
# 2 1 1 2
# outputCopy
# 0



import sys
n = int(input().strip())

stud = list(map(int, input().strip().split()))

if len(set(stud)) != 3:
	print(0)
	sys.exit()

dit = dict()
s_1, s_2, s_3 = [], [], []

for i in range(n):
	if stud[i] in dit:
		dit[stud[i]] += 1
	else:
		dit[stud[i]] = 1
	if(stud[i] == 1): s_1.append(i+1)
	elif(stud[i] == 2): s_2.append(i+1)
	elif(stud[i] == 3): s_3.append(i+1)

w = min(dit.values())
res = []
for x, y, z in zip(s_1[:w], s_2[:w], s_3[:w]):
	res.append([x,y,z])

print(w)
for i in res: print(" ".join([str(a) for a in i]))

