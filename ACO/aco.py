import matplotlib.pyplot as plt
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
        self.pheromone = [[1.0 if i != j else 0 for j in range(n)] for i in range(n)]
        self.city_names = [str(i + 1) for i in range(n)]
        self.lich_su_kien = []

    def xac_suat(self, i, j, chua_tham):
        if j not in chua_tham:
            return 0
        tau = self.pheromone[i][j] ** self.alpha
        eta = (1.0 / self.kc[i][j]) ** self.beta
        return tau * eta

    def xay_dung_tour(self):
        start = random.randint(0, self.n - 1)
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

    def tinh_do_dai(self, tour):
        return sum(self.kc[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    def cap_nhat_pheromone(self, tat_ca_tour, tat_ca_do_dai):
        for i in range(self.n):
            for j in range(self.n):
                self.pheromone[i][j] *= (1 - self.rho)
        for tour, do_dai in zip(tat_ca_tour, tat_ca_do_dai):
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                delta = self.Q / do_dai
                self.pheromone[a][b] += delta
                self.pheromone[b][a] += delta

    def chay(self, so_vong):
        best_tour = None
        best_do_dai = math.inf
        for v in range(so_vong):
            tat_ca_tour = []
            tat_ca_do_dai = []
            for k in range(self.m):
                tour = self.xay_dung_tour()
                do_dai = self.tinh_do_dai(tour)
                tat_ca_tour.append(tour)
                tat_ca_do_dai.append(do_dai)
                if v == 0 and k < 3:
                    self.lich_su_kien.append(tour)
                if do_dai < best_do_dai:
                    best_do_dai = do_dai
                    best_tour = tour
            self.cap_nhat_pheromone(tat_ca_tour, tat_ca_do_dai)
        return best_tour, best_do_dai

    def ve_bieu_do(self, toa_do, best_tour):
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        axes[0].set_title("Đường đi tối ưu (Best Path)")
        x = [toa_do[i][0] for i in best_tour] + [toa_do[best_tour[0]][0]]
        y = [toa_do[i][1] for i in best_tour] + [toa_do[best_tour[0]][1]]
        axes[0].plot(x, y, 'r-o', label="Đường đi tối ưu")
        start = best_tour[0]
        axes[0].plot(toa_do[start][0], toa_do[start][1], 'b*', markersize=12, label="Điểm bắt đầu")
        for i, (xx, yy) in enumerate(toa_do):
            axes[0].text(xx, yy + 0.2, f"TP {i+1}", fontsize=8, ha='center')
        axes[0].set_xlabel("Tọa độ X")
        axes[0].set_ylabel("Tọa độ Y")
        axes[0].legend()
        axes[0].grid(True)
        axes[1].set_title("3 đường đi của kiến trong vòng đầu")
        colors = ['blue', 'green', 'orange']
        markers = ['^', 's', 'D']
        for i, tour in enumerate(self.lich_su_kien):
            x = [toa_do[j][0] for j in tour] + [toa_do[tour[0]][0]]
            y = [toa_do[j][1] for j in tour] + [toa_do[tour[0]][1]]
            axes[1].plot(x, y, color=colors[i], marker='o', label=f"Kiến {i + 1}")
            start = tour[0]
            axes[1].plot(toa_do[start][0], toa_do[start][1], markers[i],
                         color=colors[i], markersize=10, label=f"Điểm bắt đầu Kiến {i + 1}")
        for i, (xx, yy) in enumerate(toa_do):
            axes[1].text(xx, yy + 0.2, f"TP {i+1}", fontsize=8, ha='center')
        axes[1].set_xlabel("Tọa độ X")
        axes[1].set_ylabel("Tọa độ Y")
        axes[1].legend()
        axes[1].grid(True)
        plt.tight_layout()
        plt.show()
