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

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split()))for _ in range(N)]

    # 종료시간으로 정렬후 차근차근 겹치는 시간이 없도록 비교해본다.

    # 종료시간을 기준으로 정렬을 할것이다.
    sorted_info = sorted(info, key=lambda x: x[1])
    # 카운트 횟수
    cnt = 0
    # 현재 종료시간
    now = 0
    # 돌면서 검사
    for i in range(N):
        # 시작시간정의
        s = sorted_info[i][0]
        # 종료시간 정의
        e = sorted_info[i][1]
        # 만약 작업시간이 안겹친다면, 즉 종료시간보다 크거나 같다면
        if now <= s:
            # 할수있음
            cnt += 1
            # 종료 예정시간 갱신
            now = e


    print("#{} {}".format(tc, cnt ))
