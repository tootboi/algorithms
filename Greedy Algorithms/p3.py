#compute largest contiguos interval obtained by taking union of some input intervals
import sys

def main():
    lines = None
    lines = int(sys.stdin.readline().rstrip("\n"))
    
    for x in range(lines):
        data = sys.stdin.readline().rstrip("\n")
        ptList = []
        pt = data.strip().split()
        for i in range(0,len(pt),2):
            #( start, end )
            ptList.append((int(pt[i]), int(pt[i+1])))

        maxUnion(ptList)

def maxUnion(ptList):
    sortedList = sorted(ptList, key=lambda pt: pt[0])
    interUnion = set()
    currInter = sortedList[0]
    for i in range(1, len(sortedList)):
        if sortedList[i][0] - currInter[1] >= 1:
            length = currInter[1] - currInter[0]
            interUnion.add(length)
            currInter = sortedList[i]
        else:
            if sortedList[i][1] > currInter[1]:
                newTup = (currInter[0], sortedList[i][1])
                currInter = newTup
    final = currInter[1] - currInter[0]
    interUnion.add(final)

    print(max(interUnion))


main()