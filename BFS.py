from collections import defaultdict

class Node:
    def __init__(self, pos, Cha=None):
        self.ten = pos  # pos là tuple (x, y)
        self.Cha = Cha

maze = [
    ['S', 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 'E', 0]
]

def find_start_end(maze):
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    return start, end

def is_valid(maze, visited, x, y):
    rows, cols = len(maze), len(maze[0])
    return (0 <= x < rows and 0 <= y < cols and maze[x][y] != 1 and (x, y) not in visited)

def kiemTra(tam, lst):
    for n in lst:
        if n.ten == tam.ten:
            return True
    return False

def DuongDi(n):
    path = []
    while n is not None:
        path.append(n.ten)
        n = n.Cha
    path.reverse()
    print("Đường đi ngắn nhất là:", ' -> '.join(str(p) for p in path))

def BFS():
    start, end = find_start_end(maze)
    To = Node(start)
    Tg = Node(end)

    MO = []
    DONG = []
    MO.append(To)

    while MO:
        n = MO.pop(0)
        if n.ten == Tg.ten:
            print("Tìm kiếm thành công")
            DuongDi(n)
            return
        DONG.append(n)

        x, y = n.ten
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if is_valid(maze, [d.ten for d in DONG], nx, ny):
                tam = Node((nx, ny))
                if not kiemTra(tam, MO) and not kiemTra(tam, DONG):
                    tam.Cha = n
                    MO.append(tam)

    print("Tìm kiếm không thành công")
BFS()