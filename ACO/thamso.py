import math
def doc_file(ten_file):
    with open(ten_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    toa_do = [tuple(map(float, line.split())) for line in lines[1:]]
    kc = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                kc[i][j] = math.dist(toa_do[i], toa_do[j])
    return n, kc, toa_do


# kc = [
#     [0, 6, 10, 8, 5],
#     [6, 0, 8, 10, 5],
#     [10, 8, 0, 6, 5],
#     [8, 10, 6, 0, 5],
#     [5, 5, 5, 5, 0]
# ]

# Các tham số của ACO
n = 5          # số thành phố
m = 5          # số kiến
alpha = 1      # trọng số pheromone
beta = 2       # trọng số heuristic
rho = 0.5      # hệ số bay hơi pheromone
Q = 100        # lượng pheromone gửi về
so_vong = 20   # số vòng lặp
