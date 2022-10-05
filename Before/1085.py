x,y,w,h=map(int,input().split(" "))

a=w/2
b=h/2
k= list()

if int(x) > a:
    k.append(w-x)
else:
    k.append(x)
if int(y) > b:
    k.append(h-y)
else:
    k.append(y)

print(min(k))