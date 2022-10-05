
def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

result = []
for i in range(1, 10000):
    if is_prime(i):
        result.append(i)

x=int(input())
y=int(input())
kk=[i for i in range(x,y+1)]
k1=[]
for z in kk:
    if int(z) in result:
        k1.append(int(z))

if k1==[]:
    print(-1)
else:
    print(sum(k1))
    print(min(k1))

