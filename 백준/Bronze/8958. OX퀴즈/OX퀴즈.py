a = int(input())
b = []
for i in range(a):
    b = str(input())
    c = 0
    d = 0
    for i in range(len(b)):
        if b[i] == 'O':
            c += 1
            d += c
        else:
            c = 0
    print(d)
