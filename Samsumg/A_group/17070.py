import sys

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

Lx, Ly = 1, 0


position = ["x","y","d"]
count = 0
dx = [1,0,1]
dy = [0,1,1]
pos = position[0]

def dfs(Ly, Lx, pos):
    global count

    if Ly == n - 1 and Lx == n - 1:
        count += 1

    if pos == "x" or pos == "d":
        if Lx + 1 < n and array[Ly][Lx + 1] == 0:
            dfs(Ly, Lx + 1, "x")


    if pos == "y" or pos == "d":
        if Ly + 1 < n and array[Ly +1][Lx] == 0:
            dfs(Ly+1, Lx, "y")

    if Lx + 1 < n and Ly + 1 < n:
        if array[Ly + 1][Lx] + array[Ly][Lx + 1] + array[Ly + 1][Lx + 1] ==0:
            dfs(Ly+1, Lx+1, "d")

dfs(Ly,Lx,"x")
print(count)