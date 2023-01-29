# B. Spreadsheets
# time limit per test10 seconds
# memory limit per test64 megabytes
# inputstandard input
# outputstandard output
# In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.
#
# The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23.
#
# Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.
#
# Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.
#
# Input
# The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .
#
# Output
# Write n lines, each line should contain a cell coordinates in the other numeration system.
#
# Examples
# inputCopy
# 2
# R23C55
# BC23
# outputCopy
# BC23
# R23C55


def convert(n):
    s = ''
    z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while n>0:
        if n%26==0:
            n = n//26 - 1
            s+='Z'
        else:
            k = n%26
            n = n//26
            s+=z[k-1]
    return s[::-1]

def sconvert(s):
	z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	i = 0
	for l in s:
		k = z.index(l)+1
		i = i*26+k
	return i

t = int(input())


for i in range(t):
	s = input()
	n = len(s)
	ans = ''
	digits = False
	if 'R' in s and 'C' in s:
		m = s.index('R')
		q = s.index('C')
		k = m+1
		while m<q:
			if s[m].isdigit():
				digits = True
			else:
				digits = False
			m+=1
	if 'R' in s and 'C' in s and digits:
		rin = s.index('R')
		cin = s.index('C')
		row = int(s[rin+1:cin])
		col = int(s[cin+1:])
		ans = convert(col)+str(row)
	else:
		col = ''
		j = 0
		while j<n and not s[j].isdigit():
			col+=s[j]
			j+=1
		col = sconvert(col)
		row = int(s[j:])
		ans = 'R'+str(row)+'C'+str(col)
	print(ans)
