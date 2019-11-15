#divide and conquer
import math
from heapq import heappush, heappop
import time

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, point2):
        return self.x > point2.x

    def __lt__(self, point2):
        return self.x < point2.x

    def __eq__(self, point2):
        return self.x == point2.x

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def main():
    data = None
    ptList = []
    #preprocessing
    while data != "":
        data = input()
        if data != "":
            pt = [int(x) for x in data.strip().split()]
            ptList.append(pt)
    orderedList = preprocess(ptList)
    #find L
    xL = None
    if (len(orderedList) / 2) % 2 == 0:
        xL = (orderedList[int(len(orderedList) / 2)].x + orderedList[int(len(orderedList) / 2) - 1].x) / 2
    else:
        xL = orderedList[math.floor(len(orderedList) / 2)].x

    leftList = orderedList[:int(len(orderedList) / 2)]
    rightList = orderedList[int(len(orderedList) / 2):]

    #find closest pair for left
    leftMin = closestPair(leftList)

    #find closest pair for right
    rightMin = closestPair(rightList)

    currentMin = min(leftMin, rightMin)

    #find closest pair in xL boundary
    leftBound = xL - currentMin
    rightBound = xL + currentMin
    boundList = []
    for pt in orderedList:
        if pt.x > leftBound and pt.x < rightBound:
            boundList.append(pt)

    boundMin = closestBoundPair(sorted(boundList, key=lambda point: point.y), currentMin)
    #final output
    print(min(leftMin, rightMin, boundMin))

#make point objects and sort them by value of x
def preprocess(ptList):
    orderedList = []
    for pt in ptList:
        orderedList.append(point(pt[0], pt[1]))
    orderedList.sort()
    return orderedList

#finds closest pair in given list
def closestPair(ptList):
    minDis = math.inf
    if len(ptList) != 1:
        for i in range(len(ptList) - 1, -1, -1):
            for pt2 in ptList:
                if ptList[i].x != pt2.x or ptList[i].y != pt2.y:
                    eulDis = (ptList[i].x - pt2.x)**2 + (ptList[i].y - pt2.y)**2
                    if eulDis < minDis:
                        minDis = eulDis
            ptList.pop(i)
    return minDis

#checks closest pairs in boundary between two lists
def closestBoundPair(ptList, currentMin):
    minDis = math.inf
    if len(ptList) != 1:
        for pt1 in ptList:
            for pt2 in ptList:
                if pt1.x != pt2.x or pt1.y != pt2.y:
                    #check if pt2 is within pt1's boundary
                    if pt2.y <= pt1.y + currentMin:
                        eulDis = (pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2
                        if eulDis < minDis:
                            minDis = eulDis
    return minDis

main()