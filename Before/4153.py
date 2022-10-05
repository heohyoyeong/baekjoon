while True:
    a, b, c = map(int, input().split(" "))
    k=[a,b,c]
    a1 = k.index(max(k))
    if a==0 and b==0 and c==0:
        break

    if a1 == 0:
        if k[0]*k[0]==k[1]*k[1]+k[2]*k[2]:
            print("right")
        else:
            print("wrong")
    elif a1 == 1:
        if k[1]*k[1]==k[0]*k[0]+k[2]*k[2]:
            print("right")
        else:
            print("wrong")
    else:
        if k[2]*k[2]==k[1]*k[1]+k[0]*k[0]:
            print("right")
        else:
            print("wrong")




