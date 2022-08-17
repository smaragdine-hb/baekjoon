a = int(input())
b = int(input())
c = 0
d = 0
f = 0
for i in range(b):
    c,d = map(int,input().split())
    f +=(c*d)
if f==a:
    print("Yes")
else:
    print("No")