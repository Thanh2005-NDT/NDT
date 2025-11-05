import math

def docfile(tenfile):
    f = open(tenfile, "r")
    dong = [x.strip() for x in f if x.strip()]
    f.close()

    n = int(dong[0])
    td = []
    for i in range(1, len(dong)):
        x, y = map(float, dong[i].split())
        td.append((x, y))

    kc = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                kc[i][j] = math.dist(td[i], td[j])
    return n, kc, td

m = 5
alpha = 1
beta = 2
rho = 0.5
Q = 100
vong = 20






