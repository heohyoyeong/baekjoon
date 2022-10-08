## 청소년 상어
import sys


def FindIndex(fish,num):
    FlattenList =[]
    for i in range(4):
        for j in range(4):
            FlattenList.append(fish[i][j])
    data = FlattenList.index(num)
    return data%4, data//4

def Findfish(IsFish,startx,starty,direction_num, direction_x,direction_y):
    chance = 0
    direction = direction_num[starty][startx]
    while chance < 8:
        x = startx + direction_x[direction]
        y = starty + direction_y[direction]
        if 0<= x <4 and 0<= y <4:
            if IsFish[x][y]==True:
                return True, x, y, direction
        chance+=1
        direction +=1
        direction = direction%8
    return False, x, y, direction

def Movefish(IsFish,fish,fishsurvive,direction_num,direction_x,direction_y):
    for idx in fishsurvive:
        x, y = FindIndex(fish, idx)
        ok, newx, newy, newdirection= Findfish(IsFish, x, y, direction_num, direction_x, direction_y)
        if ok ==True:
            fish[y][x], fish[newy][newx] =  fish[newy][newx], fish[y][x]
            direction_num[y][x] = newdirection
            direction_num[y][x], direction_num[newy][newx] = direction_num[newy][newx], direction_num[y][x]

    return fish, direction_num












map = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

fish = [ [map[i][j] for j in range(0,8,2)] for i in range(4)]
direction_num = [[map[i][j]-1 for j in range(1,8,2)] for i in range(4)]
fishsurvive = [i for i in range(1,17)]

Lx = 0
Ly = 0
shark = 0

direction_x = [0,-1,-1,-1,0,1,1,1]
direction_y = [-1,-1,0,1,1,1,0,-1]
IsFish = [[True]*4 for i in range(4)]


while True:
    shark += fish[Ly][Lx]
    IsFish[Ly][Lx] = False
    fishsurvive.remove(fish[Ly][Lx])
    Lx, Ly = Lx + direction_x[direction_num[Ly][Lx]], Ly +direction_y[direction_num[Ly][Lx]]




    print(shark)