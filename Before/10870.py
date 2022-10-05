# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.


b=int(input())
a = [0, 1]
def start(b):
    if b==0:
        print(0)
    elif b==1:
        print(1)
    else:
        k=1
        d=call(b,k)
        print(d)
def call(b,k):
    if k<b:
        a.append(a[k]+a[k-1])
        k+=1
        return call(b,k)
    else:
        return a[b]

start(b)
