x=list()
for _ in range(0,9):
    a=int(input())
    x.append(a)

xsum=sum(x)

d=[0,0]
for i in range(0,9):
    a=x[i]
    for j in range(0,9):
        b=x[j]
        if xsum-a-b==100 and i!=j:
            d[0]=a
            d[1]=b

x.remove(d[0])
x.remove(d[1])
x.sort()
for z in range(len(x)):
    print(x[z])