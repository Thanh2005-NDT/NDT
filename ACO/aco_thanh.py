import random, math, matplotlib.pyplot as plt

class ACO:
    def __init__(self, n, m, alpha, beta, rho, Q, kc):
        self.n = n
        self.m = m
        self.a = alpha
        self.b = beta
        self.r = rho
        self.Q = Q
        self.kc = kc
        self.phero = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
        self.ten = [str(i+1) for i in range(n)]
        self.tour5 = []

    def xs(self, i, j, chua):
        if j not in chua:
            return 0
        tau = self.phero[i][j] ** self.a
        eta = (1 / self.kc[i][j]) ** self.b
        return tau * eta

    def ddi(self):
        start = random.randint(0, self.n-1)
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
                xs = [x/tong for x in xs]
                ktiep = random.choices(range(self.n), weights=xs)[0]
            tour.append(ktiep)
            chua.remove(ktiep)
            htai = ktiep

        tour.append(start)
        return tour

    def dodai(self, tour):
        return sum(self.kc[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    def capnhat(self, ds, dsdai):
        for i in range(self.n):
            for j in range(self.n):
                self.phero[i][j] *= (1 - self.r)

        for tour, dai in zip(ds, dsdai):
            for i in range(len(tour)-1):
                a, b = tour[i], tour[i+1]
                d = self.Q / dai
                self.phero[a][b] += d
                self.phero[b][a] += d

    def chay(self, vong):
        tot = math.inf
        tourtot = []
        vtot = 0

        for v in range(vong):
            ds = []
            dsdai = []
            for k in range(self.m):
                tour = self.ddi()
                dai = self.dodai(tour)
                ds.append(tour)
                dsdai.append(dai)

                if v == 0 and k < 5:
                    self.tour5.append(tour)
                    print("\nKien", k+1, "vong dau:")
                    print(" -> ".join(["TP"+str(t+1) for t in tour]))
                    print("Do dai:", round(dai, 2))

                if dai < tot:
                    tot = dai
                    tourtot = tour
                    vtot = v + 1

            self.capnhat(ds, dsdai)
        print("\nToi uu dat o vong:", vtot)
        return tourtot, tot

    def ve(self, td, best):
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.title("Duong di toi uu")
        x = [td[i][0] for i in best] + [td[best[0]][0]]
        y = [td[i][1] for i in best] + [td[best[0]][1]]
        plt.plot(x, y, 'r-o', linewidth=2, label="Duong toi uu")
        plt.plot(td[best[0]][0], td[best[0]][1], 'b*', markersize=12, label="Diem bat dau")
        for i, (xx, yy) in enumerate(td):
            plt.text(xx, yy+0.2, f"TP{i+1}", fontsize=8, ha='center')
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.title("5 kien vong dau")
        mau = ['blue','green','orange','purple','brown']
        for i, tour in enumerate(self.tour5[:5]):
            x = [td[j][0] for j in tour] + [td[tour[0]][0]]
            y = [td[j][1] for j in tour] + [td[tour[0]][1]]
            plt.plot(x, y, color=mau[i], marker='o', linestyle='--', label=f"Kien {i+1}")
        for i, (xx, yy) in enumerate(td):
            plt.text(xx, yy+0.2, f"TP{i+1}", fontsize=8, ha='center')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()
