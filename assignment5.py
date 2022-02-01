#Swap Case
# GITHUB-LINK->https://github.com/yashNarodia/PIP_Assignments.git
def CaseSwap(str):
    strOut = ''
    for char in str:
        if(char.isupper()==True):
            strOut += char.lower()
        elif(char.islower()==True):
            strOut += char.upper()
        else: 
            strOut += char
    return strOut

s = input()
print(CaseSwap(s))