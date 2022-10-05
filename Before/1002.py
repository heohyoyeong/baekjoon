import math
a=int(input())
for _ in range(0,a):
    x1,y1,r1,x2,y2,r2=map(int,input().split(" "))
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    r=r1+r2
    if x1==x2 and y1==y2 and r1==r2:
        print("-1")
    elif d+r1<r2 or d+r2<r1:
        print("0")
    elif d+r1==r2 or d+r2==r1:
        print("1")
    else:
        if d<r:
            print("2")
        elif d==r:
            print("1")
        elif d>r:
            print("0")