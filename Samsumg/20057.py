import sys

def rotated(array,rotation):
    n = len(array)
    m = len(array[0])

    dd = [[0]* n for _ in range(m)]
    if rotation==-1:
        for i in range(n):
          for j in range(m):
              dd[m-j-1][i] = array[i][j]
    else:
        for i in range(n):
          for j in range(m):
              dd[n-j-1][n-i-1] = array[i][j]
    return dd

def sand_move(dx,dy):
    num = sand[Ly][Lx]
    alpha = num-sum([int(z*num) for z in clac])
    case1 = [0, 0, int(0.02 * num), 0, 0]
    case2 = [0, int(0.1 * num), int(0.07 * num), int(0.01 * num), 0]
    case3 = [int(0.05*num),alpha,0,0,0]

    array = [case1,case2,case3,case2,case1]

    if dx==1:
        for z in range(len(array)):
            array[z].reverse()
    if dy!=0:
        array = rotated(array,dy)
    return array

def array_fusion(array, sand, Lx,Ly):
    x_start = Lx-2
    y_start = Ly-2
    x_end = Lx+2
    y_end = Ly+2

    array_x_start = 0
    array_y_start = 0
    array_x_end = 4
    array_y_end = 4

    if x_start<0:
        array_x_start -= x_start
        x_start=0


    if y_start<0:
        array_y_start -= y_start
        y_start=0

    if x_end>n-1:
        array_x_end -= x_end-n+1
        x_end=n-1

    if y_end>n-1:
        array_y_end -= y_end-n+1
        y_end=n-1


    x_num = [y for y in range(x_start,x_end+1)]
    y_num = [y for y in range(y_start,y_end+1)]
    x_array_num = [y for y in range(array_x_start,array_x_end+1)]
    y_array_num = [y for y in range(array_y_start,array_y_end+1)]

    for i in range(len(y_num)):
        for j in range(len(x_num)):
            sand[y_num[i]][x_num[j]] +=array[y_array_num[i]][x_array_num[j]]
    return sand

clac = [0.1,0.1,0.07,0.07,0.02,0.02,0.01,0.01,0.05]

n = int(sys.stdin.readline())
sand = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total =sum([sum(z) for z in sand])
Lx, Ly = n//2, n//2

x_direction = [[-1,0],[1,0]]
y_direction = [[0,1],[0,-1]]






for i in range(n-1):
    case = i%2

    for j in range(i+1):
        Lx += x_direction[case][0]
        Ly += y_direction[case][0]
        array = sand_move(x_direction[case][0], y_direction[case][0])
        sand = array_fusion(array,sand, Lx,Ly)
        sand[Ly][Lx]=0


    for j in range(i+1):
        Lx += x_direction[case][1]
        Ly += y_direction[case][1]

        array = sand_move(x_direction[case][1], y_direction[case][1])
        sand = array_fusion(array, sand, Lx, Ly)
        sand[Ly][Lx] = 0

    if i==n-2:
        for j in range(i):
            Lx += -1
            print(Lx)
            array = sand_move(x_direction[case][0], y_direction[case][0])
            sand = array_fusion(array, sand, Lx, Ly)
            sand[Ly][Lx]=0

print(total-sum([sum(z) for z in sand]))
