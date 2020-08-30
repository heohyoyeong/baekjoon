import math

x=int(input())
for _ in range(x):
    a,b=map(int,input().split(" "))
    k=b-a
    a=int(math.sqrt(k))
    if a*a==k:
        print(2*a-1)
    elif a*(a+1)>=k:
        print(2*a)
    else:
        print(2*a+1)

