import random
import math
import time
import matplotlib.pyplot as plt

class ACO:
    def __init__(self, n, m, alpha, beta, rho, Q, kc):
        # --- Bước 1: Khởi tạo tham số ---
        self.n = n
        self.m = m
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.kc = kc

        # Khởi tạo pheromone ban đầu
        self.pheromone = [[1.0 if i != j else 0 for j in range(n)] for i in range(n)]

    # Bước 2.1: Tính xác suất chọn thành phố tiếp theo
    def xac_suat(self, i, j, chua_tham):
        if j not in chua_tham:
            return 0
        tau = self.pheromone[i][j] ** self.alpha
        eta = (1.0 / self.kc[i][j]) ** self.beta
        return tau * eta

    # Bước 2.2: Xây dựng tour cho mỗi kiến
    def xay_dung_tour(self, start):
        tour = [start]
        chua_tham = set(range(self.n))
        chua_tham.remove(start)
        hien_tai = start
        while chua_tham:
            xs = [self.xac_suat(hien_tai, j, chua_tham) for j in range(self.n)]
            tong = sum(xs)
            if tong == 0:
                ke_tiep = random.choice(list(chua_tham))
            else:
                xs = [x / tong for x in xs]
                ke_tiep = random.choices(range(self.n), weights=xs)[0]
            tour.append(ke_tiep)
            chua_tham.remove(ke_tiep)
            hien_tai = ke_tiep
        tour.append(start)
        return tour

    # Bước 3: Tính độ dài tour
    def tinh_do_dai(self, tour):
        return sum(self.kc[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    # Bước 4: Cập nhật pheromone
    def cap_nhat_pheromone(self, tat_ca_tour, tat_ca_do_dai):
        # Bay hơi pheromone
        for i in range(self.n):
            for j in range(self.n):
                self.pheromone[i][j] *= (1 - self.rho)
        # Mỗi kiến thải pheromone lên đường đi
        for tour, do_dai in zip(tat_ca_tour, tat_ca_do_dai):
            delta = self.Q / do_dai
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                self.pheromone[a][b] += delta
                self.pheromone[b][a] += delta

    # Bước 5: Vòng lặp chính
    def chay(self, so_vong):
        best_tour = None
        best_do_dai = math.inf
        for v in range(so_vong):
            print(f"\n=== VÒNG {v+1} ===")
            tat_ca_tour = []
            tat_ca_do_dai = []
            for k in range(self.m):
                start = k % self.n
                tour = self.xay_dung_tour(start)
                do_dai = self.tinh_do_dai(tour)
                tat_ca_tour.append(tour)
                tat_ca_do_dai.append(do_dai)

                # 🔹 In tour của các kiến trong vòng 1 và 2
                if v < 2:
                    print(f"  Kiến {k+1}: tour = {[i+1 for i in tour]}, độ dài = {round(do_dai,2)}")

                if do_dai < best_do_dai:
                    best_tour = tour
                    best_do_dai = do_dai

            self.cap_nhat_pheromone(tat_ca_tour, tat_ca_do_dai)
            print(f"--> Tốt nhất sau vòng {v+1}: độ dài = {round(best_do_dai,2)}")
        return best_tour, best_do_dai

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


files = ["25.txt", "50.txt", "100.txt"]
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for idx, ten in enumerate(files):
    print(f"\n========== CHẠY FILE {ten} ==========")
    n, kc, coords = doc_file(ten)

    start = time.time()
    aco = ACO(n=n, m=10, alpha=1, beta=2, rho=0.5, Q=100, kc=kc)
    best_tour, best_len = aco.chay(so_vong=20)
    end = time.time()
    tg = round(end - start, 3)

    print(f"\nKẾT QUẢ CUỐI CÙNG:")
    print(f"Tour tốt nhất: {[i+1 for i in best_tour]}")
    print(f"Độ dài: {round(best_len, 2)}")
    print(f"Thời gian chạy: {tg} giây")

    # --- Vẽ vào subplot ---
    x = [coords[i][0] for i in best_tour]
    y = [coords[i][1] for i in best_tour]
    axs[idx].plot(x, y, "-o", color="blue")

    for i, (xi, yi) in enumerate(coords):
        axs[idx].text(xi + 1, yi + 1, str(i + 1), fontsize=8, color="red")

    axs[idx].set_title(f"{ten}\nĐộ dài={round(best_len,2)}, Thời gian={tg}s")
    axs[idx].set_xlabel("X")
    axs[idx].set_ylabel("Y")
    axs[idx].grid(True)

plt.suptitle("Đường đi tốt nhất của 3 bộ dữ liệu", fontsize=14)
plt.tight_layout()
plt.show()
