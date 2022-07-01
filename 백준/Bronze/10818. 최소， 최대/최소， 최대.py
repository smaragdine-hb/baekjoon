a = int(input())
b = list(map(int, input().split()))
c = b[0]
d = b[0]
for i in range(a):
    if c>b[i]:
        c = b[i]
    elif d<b[i]:
        d = b[i]
print(c,d)