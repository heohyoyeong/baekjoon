
def call(n):
    if n==1:
        return 1
    else:
        return n*call(n-1)

def start(a):
    if a==1 or a==0:
        print(1)
    else:
        b=call(a)
        print(b)

x=input().split("!")
a=int(x[0])

start(a)