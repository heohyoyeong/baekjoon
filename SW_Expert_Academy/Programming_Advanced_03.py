# ### problem 1
# from collections import deque
# T = int(input())
#
# for test_case in range(1, T + 1):
#     first = list(map(int,input().split()))
#     N, M = first[0], first[1]
#     container = list(map(int, input().split()))
#     container.sort(reverse=True)
#     container = deque(container)
#     truck = list(map(int, input().split()))
#     truck.sort(reverse=True)
#     truck = deque(truck)
#     a=0
#     for i in range(M):
#
#         if len(container)==0:
#             break
#         else:
#             find_container = True
#             new_truck = truck.popleft()
#             while find_container:
#                 new_container = container.popleft()
#                 if new_truck>=new_container:
#                     a+=new_container
#                     find_container = False
#
#                 if len(container)==0:
#                     break
#
#
#     print(f"#{test_case} {a}")


### problem 2

def dfs(num,idx):
    num+=1
    while idx<24:
        if total_array[idx]!=0:
            idx = total_array[idx][1]
            num+=1
        else:
            idx+=1
    return num

T = int(input())

for test_case in range(1, T + 1):
    nums = int(input())
    total_array=[0]*24
    array = [list(map(int, input().split())) for _ in range(nums)]
    array.sort()
    start = 0

    while True:
        if start == len(array)-1:
            break
        if array[start][0] == array[start+1][0]:
            array.remove(array[start+1])
        else:
            start +=1

    for i in range(len(array)):
        total_array[array[i][0]]=array[i]

    result=0

    for i in range(24):
        b=0
        if total_array[i]==0:
            pass
        else:
            calc = dfs(b, total_array[i][1])
            if result<calc:
                result = calc

    print(f"#{test_case} {result}")
