x=int(input())

for _ in range(0,x):
    a=int(input()) #층
    b=int(input()) #호
    k = [i for i in range(1, b + 1)]
    for __ in range(a):

        for j in range(1,b):

            k[j] += k[j-1]
    print(k[-1])