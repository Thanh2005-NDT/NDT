import time
from thamso import *
from aco import ACO

if __name__ == "__main__":
    n, kc, toa_do = doc_file("25.txt")

    start_time = time.time()

    aco = ACO(n=n, m=m, alpha=alpha, beta=beta, rho=rho, Q=Q, kc=kc)
    best_tour, best_do_dai = aco.chay(so_vong=so_vong)

    end_time = time.time()

    tour_chu = [aco.city_names[i] for i in best_tour]
    print("🔹 Đường đi tối ưu:", " → ".join(tour_chu))
    print("🔹 Độ dài:", round(best_do_dai, 4))
    print("⏱️ Thời gian chạy:", round(end_time - start_time, 4), "giây")

    aco.ve_bieu_do(toa_do, best_tour)
