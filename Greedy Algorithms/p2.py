#find max number of intervals that overlap at single point.
import sys
from heapq import heappush, heappop, heapify

def main():
    lines = None
    lines = int(sys.stdin.readline().rstrip("\n"))
    
    for x in range(lines):
        data = sys.stdin.readline().rstrip("\n")
        ptList = []
        pt = data.strip().split()
        for i in range(0,len(pt),2):
            #( end, start )
            ptList.append((int(pt[i+1]), int(pt[i])))

        maxDepth(ptList)

def maxDepth(ptList):
    sortedList = sorted(ptList, key=lambda pt: pt[1])
    interHeap = []
    for i in range(len(sortedList)):
        if len(interHeap) == 0:
            heappush(interHeap, sortedList[i])
        #    start               end
        elif sortedList[i][1] <= interHeap[0][0]:
            heappush(interHeap, sortedList[i])
        else:
            heappop(interHeap)
            heappush(interHeap, sortedList[i])
    print(len(interHeap))

main()