# import math
# def call(a,b):
#     li=int(math.sqrt(b)+1)
#     ran=[i for i in range(a,b+1)]
#     for z in range(2,li+1):
#         for zz in ran:
#             if zz%z==0:
#                 ran.remove(zz)
#                 pass
#     if 1 in ran:
#         ran.remove(1)
#     a=len(ran)
#
#     return a
#
#


def calls():
    N=246912
    M=1
    b = [0, 0]+[1]*(N-1)
    a= list()
    for i in range(2, N+1):
        if b[i] and i >= M:
            a.append(i)
        for j in range(2*i, N+1, i):
            b[j]=0
    return a
a=calls()

while True:
    x=int(input())
    c=[i for i in range(x+1,2*x+1)]
    d=list()
    if x==0:
        break
    else:
        for z in c:
            if z in a:
                d.append(z)
    print(len(d))