import math
from heapq import heappush, heappop

class node:
    def __init__(self, num, weight, adj, start, goal):
        self.num = num
        self.weight = weight
        self.adj = adj
        self.start = start
        self.goal = goal

    def __gt__(self, node2):
        return self.weight > node2.weight

    def __lt__(self, node2):
        return self.weight < node2.weight

    def __eq__(self, node2):
        return self.weight == node2.weight

    def __repr__(self):
        return str(self.num)

def main():
    nNm = None
    weightList = []
    while nNm != "0 0":
        nNm = input()
        #preprocessing
        new = [int(x) for x in nNm.strip().split()]
        #extract row and col num from nNm
        rows = new[0]
        cols = new[1]
        if rows ==1 and cols == 1:
                total = input()
                print(int(total))
        elif rows != 0 and cols != 0:
            #pass num of rows to function, which calls input() that many times
            weightList = makeWeightList(rows, cols)
            #call djikstra
            djikstra(weightList, rows, cols)

#creates list of weights in order (left to right--repeat for all rows)
def makeWeightList(rows, cols):
    #list of weights
    weightList = []

    #loop num of rows and call input()
    for x in range(rows):
        currRow = [int(x) for x in input().strip().split()]
        weightList.extend(currRow)
    return weightList

#creates adj lists for nodes
def makeAdj(num, rows, cols):
    adjList = []
    #excludes leftest col
    if((num) % cols != 0):
        #west
        adjList.append(num - 1)
        #excludes top row
        if(num >= cols):
            #north west
            adjList.append(num - (cols + 1))
        #excludes bottom row
        if(num < (cols * (rows - 1))):
            #south west
            adjList.append(num + (cols - 1))
    #excludes top row
    if(num >= cols):
        #north
        adjList.append(num - cols)
    #excludes rightest col
    if((num + 1) % cols != 0):
        #excludes top row
        if(num >= cols):
            #north east
            adjList.append(num - (cols - 1))
        #east
        adjList.append(num + 1)
        #excludes bottom row
        if(num < (cols * (rows - 1))):
            #south east
            adjList.append(num + cols + 1)
    #excludes bottom row
    if(num < (cols * (rows - 1))):
        #south
        adjList.append(num + cols)
    return adjList

#creates nodes -- adds its name, weight and adjacency info
def makeNodes(weightList, rows, cols):
    nodeList = []
    #loop for all nodes
    for x in range(rows * cols):
        #check if node is start node
        if(x == (cols * (rows - 1))):
            nodeList.append(node(x, weightList[x], makeAdj(x, rows, cols), True, False))
        #check if node is goal node
        elif(x == (cols - 1)):
            nodeList.append(node(x, math.inf, makeAdj(x, rows, cols), False, True))
        else:
            nodeList.append(node(x, math.inf, makeAdj(x, rows, cols), False, False))
    return nodeList
        

#does the heavy lifting
def djikstra(weightList, rows, cols):
    #seen nodes
    seen = set()
    goalReached = False
    weightHeap = []
    #make nodes -- call function
    nodeList = makeNodes(weightList, rows, cols)
    #starting with start node. update neoghbours' weight via loop
    for neighbourNum in nodeList[(cols * (rows - 1))].adj:
        #check if weight summed is lower than current neighbour weight
        if((nodeList[(cols * (rows - 1))].weight + weightList[neighbourNum]) < nodeList[neighbourNum].weight) and goalReached == False:
            #update neighbour weight
            nodeList[neighbourNum].weight = (nodeList[(cols * (rows - 1))].weight + weightList[neighbourNum])
            #heappush neighbour node to weightHeap
            heappush(weightHeap, nodeList[neighbourNum])
            #check if updated neighbour is goal
            if nodeList[neighbourNum].goal == True:
                goalReached = True
    #append start node to seen list
    seen.add(cols * (rows - 1))

    while goalReached == False:
        #heappop
        leastWeight = heappop(weightHeap)
        #if node not in seen list -- update this node's neighbours' weight
        if(leastWeight.num not in seen):
            #loop through neighbours
            for neighbourNum in leastWeight.adj:
                totalWeight = leastWeight.weight + weightList[neighbourNum]
                neighNode = nodeList[neighbourNum]
                #check if weight summed is lower than current neighbour weight
                if (totalWeight < neighNode.weight) and goalReached == False:
                    #update neighbour weight
                    neighNode.weight = totalWeight
                    #heappush neighbour node to weightHeap
                    heappush(weightHeap, neighNode)
                    #check if updated neighbour is goal
                    if neighNode.goal == True:
                        goalReached = True
            #append this node to seen list
            seen.add(leastWeight.num)
    print(nodeList[(cols - 1)].weight)

main()

