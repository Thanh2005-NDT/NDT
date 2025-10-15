import random
import math

class ACO:
    def __init__(self, n, m, alpha, beta, rho, Q, kc):
        self.n = n
        self.m = m
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.kc = kc
        # Khởi tạo pheromone = 2, đường chéo = 0
        self.pheromone = [[2.0 if i != j else 0 for j in range(n)] for i in range(n)]

        self.city_names = [chr(65 + i) for i in range(n)]

    # === BƯỚC 2: TÍNH XÁC SUẤT CHỌN THÀNH PHỐ TIẾP THEO ===
    def xac_suat(self, i, j, chua_tham):
        if j not in chua_tham:
            return 0
        tau = self.pheromone[i][j] ** self.alpha
        eta = (1.0 / self.kc[i][j]) ** self.beta
        return tau * eta

    # === BƯỚC 2: XÂY DỰNG TOUR CHO 1 KIẾN ===
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

    # === BƯỚC 3: TÍNH ĐỘ DÀI TOUR ===
    def tinh_do_dai(self, tour):
        return sum(self.kc[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    # === BƯỚC 4: CẬP NHẬT PHEROMONE ===
    def cap_nhat_pheromone(self, tat_ca_tour, tat_ca_do_dai):
        # Bay hơi
        for i in range(self.n):
            for j in range(self.n):
                self.pheromone[i][j] *= (1 - self.rho)

        # Cập nhật pheromone
        for tour, do_dai in zip(tat_ca_tour, tat_ca_do_dai):
            delta = self.Q / do_dai
            for i in range(len(tour)-1):
                a, b = tour[i], tour[i+1]
                self.pheromone[a][b] += delta
                self.pheromone[b][a] += delta

    # In ma trận pheromone
    def in_ma_tran_pheromone(self):
        print("\nMa trận pheromone:")
        for row in self.pheromone:
            print([round(x, 2) for x in row])

    # === BƯỚC 5: VÒNG LẶP CHÍNH ===
    def chay(self, so_vong):
        best_tour = None
        best_do_dai = math.inf

        for v in range(so_vong):
            tat_ca_tour = []
            tat_ca_do_dai = []

            print(f"\n=== Vòng {v+1} ===")

            for k in range(self.m):
                start = k % self.n
                tour = self.xay_dung_tour(start)
                do_dai = self.tinh_do_dai(tour)
                tat_ca_tour.append(tour)
                tat_ca_do_dai.append(do_dai)

                # In tour trong 2 vòng đầu
                if v < 2:
                    tour_chu = [self.city_names[i] for i in tour]
                    print(f"Kiến {k+1}: tour = {tour_chu}, độ dài = {do_dai}")

                if do_dai < best_do_dai:
                    best_tour = tour
                    best_do_dai = do_dai

            self.cap_nhat_pheromone(tat_ca_tour, tat_ca_do_dai)

            best_tour_chu = [self.city_names[i] for i in best_tour]
            print(f"Tour tốt nhất hiện tại = {best_tour_chu}, độ dài = {best_do_dai}")
            self.in_ma_tran_pheromone()

        return best_tour, best_do_dai


# ===========================
# CHẠY THỬ VỚI 5 THÀNH PHỐ A-E
# ===========================
if __name__ == "__main__":
    kc = [
        [0, 6,10, 8, 5],
        [6, 0, 8, 10, 5],
        [10, 8, 0, 6, 5],
        [8, 10, 6, 0, 5],
        [5, 5, 5, 5, 0]
    ]

    aco = ACO(n=5, m=5, alpha=1, beta=1, rho=0.5, Q=100, kc=kc)
    tour, do_dai = aco.chay(so_vong=20)

    print("\nKẾT QUẢ CUỐI CÙNG:")
    tour_chu = [aco.city_names[i] for i in tour]
    print("Tour tốt nhất:", tour_chu)
    print("Độ dài:", do_dai)
