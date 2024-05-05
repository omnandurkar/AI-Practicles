# 2. Implement A star Algorithm for any game search problem.

import heapq
import copy

N = 3

class Node:
    def __init__(self, mat, x, y, newX, newY, level, parent):
        self.parent = parent
        self.mat = copy.deepcopy(mat)
        self.mat[x][y], self.mat[newX][newY] = self.mat[newX][newY], self.mat[x][y]
        self.cost = float('inf')
        self.level = level
        self.x = newX
        self.y = newY

    def __lt__(self, other):
        return (self.cost + self.level) < (other.cost + other.level)

def printMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=' ')
        print()

def calculateCost(initial, final):
    count = 0
    for i in range(N):
        for j in range(N):
            if initial[i][j] and initial[i][j] != final[i][j]:
                count += 1
    return count

def isSafe(x, y):
    return 0 <= x < N and 0 <= y < N

def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mat)
    print(f'hscore: {root.cost}\ngscore: {root.level}\nfscore: {root.cost + root.level}\n')
    print()

def solve(initial, x, y, final):
    pq = []
    root = Node(initial, x, y, x, y, 0, None)
    root.cost = calculateCost(initial, final)
    heapq.heappush(pq, root)
    
    while pq:
        min_node = heapq.heappop(pq)
        if min_node.cost == 0:
            printPath(min_node)
            return
        for i in range(4):
            if isSafe(min_node.x + row[i], min_node.y + col[i]):
                child = Node(min_node.mat, min_node.x, min_node.y, min_node.x + row[i], min_node.y + col[i], min_node.level + 1, min_node)
                child.cost = calculateCost(child.mat, final)
                heapq.heappush(pq, child)

row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

if __name__ == "__main__":
    initial = [[0] * N for _ in range(N)]
    x, y = None, None

    print("Enter Initial Block Structure\nEnter 0 for blank space:")
    for i in range(N):
        for j in range(N):
            initial[i][j] = int(input(f"Row {i + 1} Column {j + 1} Element = "))
            if initial[i][j] == 0:
                x, y = i, j

    final = [[0] * N for _ in range(N)]

    print("\n\nEnter Final Block Structure\nEnter 0 for blank space:")
    for i in range(N):
        for j in range(N):
            final[i][j] = int(input(f"Row {i + 1} Column {j + 1} Element = "))

    print("\n\nThis is the solution using A* Algorithm:\n")
    solve(initial, x, y, final)