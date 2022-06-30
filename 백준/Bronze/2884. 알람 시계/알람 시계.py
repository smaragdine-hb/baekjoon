a,b = map(int, input().split())
if a == 0:
    if b<45:
        print(23,(b-45)+60)
    else:
        print(a,b-45)
else:
    if b>=45:
        print(a,b-45)
    else:
        print(a-1,(b-45+60))

