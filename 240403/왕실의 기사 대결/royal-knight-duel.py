# 10시 시작
BLANK, TRAP, WALL = 0, 1, 2
VANISHED = -1
l,n,q = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(l)]
infos = [tuple(map(int, input().split())) for i in range(n)]  # 기사들 정보
damages = [0 for i in range(n)] # 각 기사의 누적 대미지 배열(-1이면 사라진 상태를 의미)
def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end = '\t')
        print()
    print()

# 초기화
new_grid = [[0 for i in range(l)] for i in range(l)]
knights = [[VANISHED for i in range(l)] for i in range(l)]
for (idx, info) in enumerate(infos):
    r, c, h, w, k = info
    r, c = r-1, c-1
    # 어느 기사가 어디 땅따먹었는지 idx값으로 위치 표기하기
    for i in range(r, r+h):
        for j in range(c, c+w):
            knights[i][j] = idx
print_grid(knights)


def in_range(nx, ny):
    if 0 <= nx < l and 0 <= ny < l:
        return True
    return False

def can_go(nx, ny):
    pass

dxs = [-1, 0, 1, 0]  # 위,오,아,왼
dys = [ 0, 1, 0,-1]
def move(x, y, dirr):
    nx, ny = x + dxs[dirr], y + dys[dirr]
    if not in_range(nx, ny):
        # print("out of range")
        return
    if not can_go(nx, ny, dirr):
        # print("cannot go")
        return
    pass

def start(idx, dirr):
    # 1. idx번째 기사를 dirr 방향으로 움직여라
    # 1-1. 일단, 다른 기사와 겹치는지 확인.
    print(idx, dirr)


for _ in range(q):
    i, d = map(int, input().split())
    start(i-1, d)