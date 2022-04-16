from itertools import combinations

NumberList = list(map(int,input().split()))
K = int(input())
NumberList.sort()
count = 0
for i in range(len(NumberList)+1):
    com = list(set(combinations(NumberList, i)))
    for comb in com :
        if sum(comb) ==K:
            count+=1

print(count)