a = list(map(int,input().split()))
c = [0,0]
for i in range(len(a)):
    a[i] = list(str(a[i]))
for i in range(len(a)):
    for f in range(len(a[i])):
        a[i][f] = int(a[i][f])
for i in range(len(a)):
    for f in range(len(a[i])):
        b = 0
        b += a[i][f]*(10**(f))
        c[i] += b
if c[0]>c[1]:
    print(c[0])
else:
    print(c[1])

