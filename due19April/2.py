import numpy as np

NumberList = list(map(int,input().split()))
Min = min(NumberList)
print('Min: ', Min);
Max = max(NumberList)
print('Max: ', Max);
sum = 0
for  num in NumberList:
    sum+= num

Mean = np.mean(NumberList)
print('Mean: ', Mean)
Std = np.std(NumberList)
print('Std: ', Std)
Var  =np.var(NumberList)
print('Var: ', Var)
