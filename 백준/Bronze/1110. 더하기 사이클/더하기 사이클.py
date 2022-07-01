a = int(input())
b = 0
c = 0
d = a
while True:
    c = (a//10 + a%10)%10
    a = c + a%10*10
    b += 1
    if a == d:
        break
print(b)