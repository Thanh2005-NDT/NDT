import time
from thamso_thanh import *
from aco_thanh import ACO

if __name__ == "__main__":
    n, kc, td = docfile("test.txt")

    bd = time.time()
    aco = ACO(n, m, alpha, beta, rho, Q, kc)
    best, dai = aco.chay(vong)
    kt = time.time()

    print("\nKET QUA ")
    print("Duong di:", " -> ".join(["TP"+str(i+1) for i in best]))
    print("Do dai:", round(dai, 3))
    print("Thoi gian:", round(kt-bd, 3), "giay")

    aco.ve(td, best)
