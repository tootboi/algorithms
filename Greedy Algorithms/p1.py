#finds max number of non-overlapping intervals.
from heapq import heappush, heappop
import sys

def main():
    lines = None
    lines = int(sys.stdin.readline().rstrip("\n"))
    
    for x in range(lines):
        data = sys.stdin.readline().rstrip("\n")
        ptList = []
        pt = data.strip().split()
        for i in range(0,len(pt),2):
            ptList.append((int(pt[i]), int(pt[i+1])))
        
        maxNon(ptList)

def maxNon(ptList):
    sortedList = sorted(ptList, key=lambda pt: pt[1])
    setInters = set()
    lastAdded = -1
    for i in range(len(sortedList)):
        if sortedList[i][0] > lastAdded:
            setInters.add(sortedList[i])
            lastAdded = sortedList[i][1]
    print(len(setInters))

main()