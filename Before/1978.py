
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
for i in range(1, 1001):
    if is_prime(i):
        result.append(i)

a=0
x=int(input())
y=input().split(" ")

for z in y:
    if int(z) in result:
        a+=1



print(a)