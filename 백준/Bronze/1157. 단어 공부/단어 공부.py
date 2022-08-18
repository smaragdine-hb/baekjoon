b = input()
c = {}
for i in range(len(b)):
    if b[i].upper() in c:
        c[b[i].upper()] += 1
    else:
        c[b[i].upper()] = 1
a = 0
for key,value in c.items():
    if a<value:
        a = value
        result = key
    elif a == value:
        result = "?"
print(result)