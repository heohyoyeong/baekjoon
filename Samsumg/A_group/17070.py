import sys

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
array[0][0], array[0][1] = 1, 1

Lx, Ly = 1, 0


position = ["x","y","d"]
count = 0
dx = [1,0,1]
dy = [0,1,1]
pos = position[0]

def move_possible(Ly, Lx, pos):
    result = []
    # if pos == "x":
    #     case = [0,2]
    #     for idx in case:
    #         if Ly+dy[idx]<n and Lx+dx[idx]<n and array[Ly+dy[idx]][Lx+dx[idx]]==0:
    #             result.append([Ly+dy[idx],Lx+dx[idx],position[idx]])
    #
    # elif pos == "y":
    #     case = [1,2]
    #     for idx in case:
    #         if Ly+dy[idx]<n and Lx+dx[idx]<n and array[Ly+dy[idx]][Lx+dx[idx]]==0:
    #             result.append([Ly+dy[idx],Lx+dx[idx],position[idx]])
    #
    # elif pos == "d":
    #     case = [0,1,2]
    #     for idx in case:
    #         if Ly+dy[idx]<n and Lx+dx[idx]<n and array[Ly+dy[idx]][Lx+dx[idx]]==0:
    #             result.append([Ly+dy[idx],Lx+dx[idx],position[idx]])

    if pos == "x":
        case = [0,2]
    elif pos == "y":
        case = [1,2]
    elif pos == "d":
        case = [0,1,2]

    for idx in case:
        if Ly + dy[idx] < n and Lx + dx[idx] < n and array[Ly + dy[idx]][Lx + dx[idx]] == 0:
            if idx == 2:
                if array[Ly + 1][Lx] + array[Ly][Lx + 1] + array[Ly + 1][Lx + 1] ==0:
                    result.append([Ly + dy[idx], Lx + dx[idx], position[idx]])
            else:
                result.append([Ly + dy[idx], Lx + dx[idx], position[idx]])
    return result

def dfs(y, x, result):
    global count
    if x==n-1 and y==n-1:
        count +=1

    for i in result:
        next_y = i[0]
        next_x = i[1]
        next_pos = i[2]
        next_result = move_possible(next_y, next_x, next_pos)
        dfs(next_y,next_x,next_result)



def function():

    first = move_possible(Ly, Lx, pos)
    if len(first)==0:
        print(count)

    else:
        dfs(Ly, Lx, first)
        print(count)




function()