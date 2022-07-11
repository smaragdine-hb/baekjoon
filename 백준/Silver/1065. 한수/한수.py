def a(b):
    c = 0
    for i in range(1,b+1):
        d = list(map(int,str(i)))
        if i<100:
            c+=1
        else:
            if d[0] - d[1] == d[1] - d[2]:
                c+=1
    print(c)       


b = int(input())
a(b)