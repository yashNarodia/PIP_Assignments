str = input()
dicts = {}
for char in str:
    if char in dicts:
        dicts[char] +=1
    else:
        dicts[char] = 1
sorted = reversed(sorted(dicts.values()))
sortedDict ={}

for i in sorted:
    for k in dicts.keys():
        if dicts[k] == i:
            sortedDict[k] = dicts[k]
            break
for k,v in sortedDict.items():
    print(k,v)

