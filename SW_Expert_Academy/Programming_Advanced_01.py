### problem 1
T = int(input())

for test_case in range(1, T + 1):
    a = input().split()
    b=bin(int('0x'+a[1] ,16))[2:]
    if len(b) < int(a[0])*4:
        b = '0'+b
    print(f"#{test_case} {b}")

### problem 2
def test(num):
    result = []
    n=1
    while num != 0:
        if num >= 2**(-1*n):
            num -=2**(-1*n)
            result.append(str(1))
        else:
            result.append(str(0))
        n+=1
        if num==0 or n>13:
            break
    if num!=0 or len(result)>13:
        return "overflow"
    else:
        return "".join(result)

T = int(input())
for test_case in range(1, T + 1):
    a = float(input())
    result = test(a)
    print(f"#{test_case} {result}")


