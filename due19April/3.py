def maxArea(A) :
    area = 0
    for i in range(len(A)) :
        for j in range(i + 1, len(A)) :
            area = max(area, min(A[j], A[i]) * (j - i))
    return area

a = list(map(int,input().split()))

print(maxArea(a))
