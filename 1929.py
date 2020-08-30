# import math
# def call(a,b):
#     li=int(math.sqrt(b)+1)
#     ran=[i for i in range(a,b+1)]
#     for z in range(2,li+1):
#         for zz in ran:
#             if zz%z==0:
#                 ran.remove(zz)
#                 pass
#     ran.append(2)
#     ran.append(3)
#     ran.append(5)
#     if 1 in ran:
#         ran.remove(1)
#     a=sorted(ran)
#
#     return a
#
#
# a,b=map(int,input().split(" "))
#
# for z in call(a,b):
#     print(z)

M, N = map(int, input().split())
x = [0, 0]+[1]*(N-1)
print(x)

for i in range(2, N+1):
    if x[i] and i >= M:
        print(i)
    for j in range(2*i, N+1, i):
        x[j]=0
