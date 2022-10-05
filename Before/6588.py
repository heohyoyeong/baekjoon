import sys
a=1000000
x = [0, 0]+[1]*(a-1)

for i in range(2, a+1):
    for j in range(2*i, 1000001, i):
        x[j]=0

while True:
    a=int(sys.stdin.readline())
    k=int(a/2)+1
    if a==0:
        break
    for z in range(3,a//2+1):
        if x[a-z]==1:
            if x[z]==1:
                print("{0} = {1} + {2}".format(a,z,a-z))
                break

