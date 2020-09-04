# import math
# x=int(input())
# a=int(math.log(x,3))
#
# def start(a):
#     if a==1:
#         c = ['***', '* *', '***']
#         for i in c:
#             print(i)
#     else:
#         d=1
#         c = ['***', '* *', '***']
#         call(a,d,c)
#
# def call(a,d,c):
#
#     if d<a:
#         b1=[c,c,c]
#         b2=[c,"",c]
#         b3=[c,c,c]
#         c=[b1,b2,b3]
#         d+=1
#         return call(a,d,c)
#
#     else:
#         a1=c[0]
#         a2=c[1]
#         a3=c[2]
#         for i in a1:
#             for z in i:
#                 print(z)
#         for i in a2:
#             for z in i:
#                 print(z)
#         for i in a3:
#             for z in i:
#                 print(z)
#
# start(a)


def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return (list(matrix))


star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)