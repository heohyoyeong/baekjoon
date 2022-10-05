

def call(x):
    y=len(x)
    a=list()
    for z in range(0,y):
        k=x[z]
        if k == 'a' or k == 'b' or k == 'c':
            d = 3
        elif k == 'd' or k == 'e' or k == 'f':
            d = 4
        elif k == 'g' or k == 'h' or k == 'i':
            d = 5
        elif k == 'j' or k == 'k' or k == 'l':
            d = 6
        elif k == 'm' or k == 'n' or k == 'o':
            d = 7
        elif k == 'p' or k == 'q' or k == 'r' or k=='s':
            d = 8
        elif k == 't' or k == 'u' or k == 'v':
            d = 9
        elif k == 'w' or k == 'x' or k == 'y' or k == 'z':
            d = 10
        else:
            d = 2
        a.append(d)
    d=sum(a)
    return d


x=input().lower()

print(call(x))