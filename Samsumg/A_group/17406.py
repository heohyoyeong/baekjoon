import sys
import copy
def perm(arr,n):
    result = []
    if n ==0:
        return [[]]

    for i in range(len(arr)):
        #시작지점
        elem = arr[i]
        for rest in perm(arr[:i]+arr[i+1:],n-1):
            result.append([elem]+rest)
    return result

def rotation(input):
    N = len(input)
    ret = [[0] * N for _ in range(N)]
    cen = N//2
    for i in range(0,cen):
        for x in range(N-1-i*2):
            ## 아래 이동
            ret[N-i-1][N-x-2-i] = input[N-i-1][N-x-1-i]
            # ## 위 이동
            ret[i][x+i+1] = input[i][x+i]

        for y in range(N-1-i*2):
        #     print(y)
            ## 왼쪽 이동
            ret[y+1+i][N-i-1]= input[y+i][N-i-1]
            # ## 오른쪽 이동
            ret[N-y-2-i][i] = input[N-y-1-i][i]

    ret[cen][cen] = input[cen][cen]
    return ret


input_array = list(map(int, sys.stdin.readline().split()))
N, M, K = input_array[0], input_array[1], input_array[2]
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1,-1,0.0]
dy = [0,0,1,-1]


perm_array = []

for _ in range(K):
    rotation_array = list(map(int, sys.stdin.readline().split()))
    r, c, s = rotation_array[0], rotation_array[1], rotation_array[2]
    perm_array.append([r,c,s])

perm_array = perm(perm_array,K)

final_result = []

for idx in range(len(perm_array)):
    test_array = copy.deepcopy(array)
    b=1
    for alpha in perm_array[idx]:
        r, c, s = alpha[0], alpha[1], alpha[2]
        LTX, LTY = c-s-1, r-s-1
        RBX, RBY = c+s, r+s
        crop = [z[LTX:RBX] for z in test_array[LTY:RBY]]
        crop = rotation(crop)
        for y in range(len(crop)):
            for x in range(len(crop)):
                test_array[LTY+y][LTX+x] = crop[y][x]
    final_result.append(min([sum(z) for z in test_array]))

print(min(final_result))



