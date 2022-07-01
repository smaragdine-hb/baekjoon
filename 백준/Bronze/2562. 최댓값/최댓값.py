a=[]
for i in range(9):
    a.append(int(input()))
b = a[0]
c = 0
for i in range(9):
    if b<a[i]:
        b = a[i]
        c = i
print(b)
print(c+1)