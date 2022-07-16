a = int(input())
b = []
c = 1
d = a
while c<=d:
    c+=1
    if a%c == 0:
        while True:
            if a%c == 0:
                b.append(c)
                a //= c
            else:
                break

for i in b:
    print(i)
