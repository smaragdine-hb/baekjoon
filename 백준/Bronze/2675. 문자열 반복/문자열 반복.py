a = int(input())
for i in range(a):
    d=""
    b,c = map(str,input().split())
    for f in range(len(c)):
        d += (int(b)*c[f])
    print(d)