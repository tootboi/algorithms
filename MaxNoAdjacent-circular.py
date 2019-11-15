#dynamic programming
import sys
import math

def main():
    data = None
    neckList = []
    #preprocessing
    while(data != ""):
            data = sys.stdin.readline().rstrip("\n")
            if data != "":
                jewel = [int(i) for i in data.strip().split()]
                neckList.append(jewel)
    for neck in neckList:
        totalJwl = sum(neck)
        i0Daughter0, i0ID = start0(neck)
        i1Daughter0, i1ID = start1(neck)
        if i0Daughter0 > i1Daughter0:
            print(i0Daughter0, totalJwl - i0Daughter0)
        else:
            print(i1Daughter0, totalJwl - i1Daughter0)

#index 0 to n-2
def start0(neck):
    neckLen = len(neck)
    trimmedList = [None] * neckLen
    largest = -math.inf

    if neckLen == 0:
        return 0, "i0"
    elif neckLen == 1:
        return neck[0], "i0"

    #make trimmedList
    for i in range(neckLen - 1):
        jwl = neck[i]
        if largest < jwl:
            largest = jwl
        trimmedList[i] = jwl
    
    for i in range(2, neckLen - 1):
        if (neck[i] + trimmedList[i-2]) > trimmedList[i-1]:
            trimmedList[i] = (neck[i] + trimmedList[i-2])
        else:
            trimmedList[i] = trimmedList[i-1]
        if largest < trimmedList[i]:
            largest = trimmedList[i]
    return largest, "i0"

#index 1 to n-1
def start1(neck):
    neckLen = len(neck)
    trimmedList = [None] * neckLen
    largest = -math.inf

    if neckLen == 0:
        return 0, "i1"
    elif neckLen == 1:
        return neck[0], "i1"

    #make trimmedList
    for i in range(1, neckLen):
        jwl = neck[i]
        if largest < jwl:
            largest = jwl
        trimmedList[i] = jwl
    
    for i in range(3, neckLen):
        if (neck[i] + trimmedList[i-2]) > trimmedList[i-1]:
            trimmedList[i] = (neck[i] + trimmedList[i-2])
        else:
            trimmedList[i] = trimmedList[i-1]
        if largest < trimmedList[i]:
            largest = trimmedList[i]
    return largest, "i1"

main()