#LAPINDROME
# GITHUB-LINK->https://github.com/yashNarodia/PIP_Assignments.git

def Lapindrome(str):
    strlen = len(str)
    print(strlen)
    if(strlen%2==0):
        a = str[:(strlen//2)]
        b = str[(strlen//2):]
    else: 
        a = str[:(strlen//2)]
        b = str[(strlen//2)+1:]
        print(b)
    la = list(a)
    la.sort()
    print(la)
    lb = list(b)
    lb.sort()
    print(lb)
    if (la==lb):
        print("YES")
    else:
        print("NO")

t = int(input())

for i in range(t):
    txt =  input()
    Lapindrome(txt)