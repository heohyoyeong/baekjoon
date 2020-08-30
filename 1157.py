x=input().upper()
x1=sorted(list(set(x)))
d=list()

for z in x1:
    b=x.count(z)
    d.append(b)

if d.count(max(d))==1:
    print(x1[d.index(max(d))])
else:
    print("?")
