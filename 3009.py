x1,y1=map(int,input().split(" "))
x2,y2=map(int,input().split(" "))
x3,y3=map(int,input().split(" "))
if x1==x2:
    if y2==y3:
        y4=y1
        x4=x3
    else:
        y4=y2
        x4=x3
elif x1==x3:
    if y2==y3:
        y4=y1
        x4=x2
    else:
        y4=y3
        x4=x2
elif x3==x2:
    if y3==y1:
        y4=y2
        x4=x1
    else:
        y4=y3
        x4=x1

print("{} {}".format(x4,y4))