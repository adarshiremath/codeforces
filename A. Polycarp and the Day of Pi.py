T =  input()
arr = []
for _ in range(int(T)):
        val = input()
        arr.append(val)
for i in arr:
    l = len(i)
    pi =  '314159265358979323846264338327'[:l]
    count = 0
    for x,y in zip(i, pi):
        if(int(x) != int(y)):
            break
        else:
            count += 1
    print(count)