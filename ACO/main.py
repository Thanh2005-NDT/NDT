import time
from thamso import *
from aco import ACO

if __name__ == "__main__":
    n, kc, td = docfile("test.txt")

    bd = time.time()
    aco = ACO(n=n, m=m, alpha=alpha, beta=beta, rho=rho, Q=Q, kc=kc)
    besttour, bestdai = aco.chay(vong=vong)
    kt = time.time()

    tentp = [aco.tp[i] for i in besttour]
    print(" Duong di toi uu:", " → ".join(tentp))
    print(" Do dai:", round(bestdai, 4))
    print("Thoi gian chay:", round(kt - bd, 4), "giay")

    aco.ve(td, besttour)
