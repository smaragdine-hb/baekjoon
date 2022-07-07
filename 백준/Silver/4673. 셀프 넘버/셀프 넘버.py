def n_self(n):
    n = n + sum(map(int, str(n)))
    return n

self_num = set()

for i in range(1, 10001):
    self_num.add(n_self(i))
for j in range(1, 10001):
    if j not in self_num:
        print(j)