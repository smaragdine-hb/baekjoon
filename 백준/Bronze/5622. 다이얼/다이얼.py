a = [["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
b = input()
b = list(b)
c = 0
for i in range(len(b)):
    for f in range(len(a)):
        if b[i] in a[f]:
            c += (f+3)
print(c) 
