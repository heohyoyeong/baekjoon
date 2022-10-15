def comb(arr, n):
    """ 조합을 손으로 짠 것 """

    result = []

    if n> len(arr):
        return result

    if n==1:
        for i in arr:
            result.append([i])

    elif n>1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:], n -1):
                result.append([arr[i]]+j)

    return result


def perm(arr,n):
    result = []
    if n ==0:
        return [[]]

    for i in range(len(arr)):
        #시작지점
        elem = arr[i]
        for rest in perm(arr[:i]+arr[i+1:],n-1):
            result.append([elem]+rest)
    return result

arr =[0,1,2,3]

print(comb(arr,4))
print(permutation(arr,4))