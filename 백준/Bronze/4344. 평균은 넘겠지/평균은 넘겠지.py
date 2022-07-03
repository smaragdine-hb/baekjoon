a = int(input())
b = []
for i in range(a):
    c = 0
    d = 0
    b = list(map(int, input().split()))
    for i in range(1,len(b)):
        c += b[i]
    c /=b[0]
    
    for i in range(1,len(b)):
        if b[i]>c:
            d += 1
    print("{:.3f}%".format(d/b[0]*100))