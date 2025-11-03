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
        self.phero = [[1.0 if i != j else 0 for j in range(n)] for i in range(n)]
        self.tp = [str(i + 1) for i in range(n)]
        self.lichsu = []

    def xs(self, i, j, chua):
        if j not in chua:
            return 0
        tau = self.phero[i][j] ** self.alpha
        eta = (1.0 / self.kc[i][j]) ** self.beta
        return tau * eta

    def xaytour(self):
        start = random.randint(0, self.n - 1)
        tour = [start]
        chua = set(range(self.n))
        chua.remove(start)
        htai = start
        while chua:
            xs = [self.xs(htai, j, chua) for j in range(self.n)]
            tong = sum(xs)
            if tong == 0:
                ktiep = random.choice(list(chua))
            else:
                xs = [x / tong for x in xs]
                ktiep = random.choices(range(self.n), weights=xs)[0]
            tour.append(ktiep)
            chua.remove(ktiep)
            htai = ktiep
        tour.append(start)
        return tour

    def dodai(self, tour):
        return sum(self.kc[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    def capnhat(self, dstour, dsdai):
        for i in range(self.n):
            for j in range(self.n):
                self.phero[i][j] *= (1 - self.rho)
        for tour, dai in zip(dstour, dsdai):
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                delta = self.Q / dai
                self.phero[a][b] += delta
                self.phero[b][a] += delta

    def chay(self, vong):
        besttour = None
        bestdai = math.inf
        vbest = 0


        for v in range(vong):
            dstour = []
            dsdai = []
            for k in range(self.m):
                tour = self.xaytour()
                dai = self.dodai(tour)
                dstour.append(tour)
                dsdai.append(dai)
                if v == 0 and k < 5:
                    self.lichsu.append(tour)
                    print(f"\nKien {k + 1} vong dau:")
                    print(" -> ".join([f"TP{t + 1}" for t in tour]))
                    print(f"Do dai: {dai:.2f}\n")
                if dai < bestdai:
                    bestdai = dai
                    besttour = tour
                    vbest = v + 1

        print(f"\n Ket qua toi uu dat tai vong: {vbest}")
        return besttour, bestdai

    def ve(self, td, best):
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))

        ax[0].set_title("Duong di toi uu")
        x = [td[i][0] for i in best] + [td[best[0]][0]]
        y = [td[i][1] for i in best] + [td[best[0]][1]]
        ax[0].plot(x, y, 'r-o', label="Best Path")
        start = best[0]
        ax[0].plot(td[start][0], td[start][1], 'b*', markersize=12, label="Start")
        for i, (xx, yy) in enumerate(td):
            ax[0].text(xx, yy + 0.2, f"TP {i+1}", fontsize=8, ha='center')
        ax[0].legend()
        ax[0].grid(True)

        ax[1].set_title("5 kien vong dau")
        mau = ['blue', 'green', 'orange', 'purple', 'brown']
        for i, tour in enumerate(self.lichsu[:5]):
            x = [td[j][0] for j in tour] + [td[tour[0]][0]]
            y = [td[j][1] for j in tour] + [td[tour[0]][1]]
            ax[1].plot(x, y, color=mau[i], marker='o', label=f"Kien {i+1}")
        for i, (xx, yy) in enumerate(td):
            ax[1].text(xx, yy + 0.2, f"TP {i+1}", fontsize=8, ha='center')
        ax[1].legend()
        ax[1].grid(True)

        plt.tight_layout()
        plt.show()
