import heapq

# Bản đồ mê cung: 0 là đường đi, 1 là tường
ban_do = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

bat_dau = (0, 0)
dich = (4, 4)

# Hàm tính khoảng cách Heuristic (Manhattan)
def kc(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def Astar(ban_do, bat_dau, dich):
    so_dong = len(ban_do)
    so_cot = len(ban_do[0])
    hang_doi = []
    heapq.heappush(hang_doi, (kc(bat_dau, dich), 0, bat_dau, [bat_dau]))
    da_di = set()

    while hang_doi:
        f, g, o_hien_tai, duong_di = heapq.heappop(hang_doi)
        if o_hien_tai in da_di:
            continue
        da_di.add(o_hien_tai)
        if o_hien_tai == dich:
            return duong_di
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x_moi = o_hien_tai[0] + dx
            y_moi = o_hien_tai[1] + dy
            o_moi = (x_moi, y_moi)
            if 0 <= x_moi < so_dong and 0 <= y_moi < so_cot and ban_do[x_moi][y_moi] == 0:
                if o_moi not in da_di:
                    duong_moi = duong_di + [o_moi]
                    g_moi = g + 1
                    f_moi = g_moi + kc(o_moi, dich)
                    heapq.heappush(hang_doi, (f_moi, g_moi, o_moi, duong_moi))
    return None


ket_qua = Astar(ban_do, bat_dau, dich)


if ket_qua:
    print("Đường đi ngắn nhất là:")
    for i, buoc in enumerate(ket_qua):
        print(f"Bước {i + 1}: {buoc}", end='')
        if i < len(ket_qua) - 1:
            print(" → ", end='')
        if (i + 1) % 4 == 0 or i == len(ket_qua) - 1:
            print()  # Xuống dòng
else:
    print("Không tìm được đường đi.")
