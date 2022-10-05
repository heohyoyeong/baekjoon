x=int(input())

for _ in range(x):
    ans = 0
    a=int(input())
    for z1 in range(1,4):
        if z1==a:
            ans+=1
        for z2 in range(1, 4):
            if z1+z2 == a:
                ans += 1
            for z3 in range(1, 4):
                if z1+z2+z3 == a:
                    ans += 1
                for z4 in range(1, 4):
                    if z1+z2+z3+z4 == a:
                        ans += 1
                    for z5 in range(1, 4):
                        if z5+z1 + z2 + z3 + z4 == a:
                            ans += 1
                        for z6 in range(1, 4):
                            if z6+z5+z1 + z2 + z3 + z4 == a:
                                ans += 1
                            for z7 in range(1, 4):
                                if z7+z6 + z5 + z1 + z2 + z3 + z4 == a:
                                    ans += 1
                                for z8 in range(1, 4):
                                    if z7+z8+z6 + z5 + z1 + z2 + z3 + z4 == a:
                                        ans += 1
                                    for z9 in range(1, 4):
                                        if z9+z7 + z8 + z6 + z5 + z1 + z2 + z3 + z4 == a:
                                            ans += 1
                                        for z10 in range(1, 4):
                                            if z9+z10+z7 + z8 + z6 + z5 + z1 + z2 + z3 + z4 == a:
                                                ans += 1
    print(ans)

