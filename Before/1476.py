a, b, c = map(int, input().split(" "))
e=1
s=1
m=1
year=1

while True:
    if e==a and s==b and m==c:
        print(year)
        break
    e+=1
    s+=1
    m+=1
    if e ==16:
        e=1
    if s ==29:
        s=1
    if m ==20:
        m=1
    year+=1
