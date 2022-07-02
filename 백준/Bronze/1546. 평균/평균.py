a = int(input())
b = list(map(int, input().split()))
c = float()
d = []
for i in range(a):
    d.append(b[i]/max(b)*100)

for i in range(a):
    c += d[i]

print(c/a)