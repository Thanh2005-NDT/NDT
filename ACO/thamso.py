import math

def docfile(tenfile):
    with open(tenfile, "r") as f:
        dong = [line.strip() for line in f if line.strip()]
    n = int(dong[0])
    toado = [tuple(map(float, line.split())) for line in dong[1:]]
    kc = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                kc[i][j] = math.dist(toado[i], toado[j])
    return n, kc, toado

m = 5         # so kien
alpha = 1     # trong so pheromone
beta = 2      # trong so heuristic
rho = 0.5     # he so bay hoi
Q = 100       # hang so pheromone
vong = 20     # so vong lap
