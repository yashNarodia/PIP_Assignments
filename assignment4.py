#Find runner-up from given list
# GITHUB-LINK->https://github.com/yashNarodia/PIP_Assignments.git

from os import scandir
from traceback import print_tb


# k = int(input())
ScoreList = list(map(int,input().split()))
ScoreSet = set(ScoreList)
ScoreList = list(ScoreSet)
ScoreList.sort()
print(ScoreList[-2])