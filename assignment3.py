#Find Captain Room Number
# GITHUB-LINK->https://github.com/yashNarodia/PIP_Assignments.git

k = int(input())
roomNumberList = list(map(int,input().split()))
roomNumberSet = set(roomNumberList)
print(((sum(roomNumberSet)*k)-(sum(roomNumberList)))//(k-1))
