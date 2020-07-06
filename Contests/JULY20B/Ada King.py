import math
from collections import deque
test = int(input())
def bfs(start, n, board):
    q = deque([start])
    nxt = deque()
    board[0][0] = "."
    r, c = [0,0,1,-1,-1,-1,1,1],[1,-1,0,0, -1, 1, -1, 1]
    while q and n:
        x, y = q.popleft()
        for i in range(8):
            a, b = x + r[i] , y + c[i]
            if n and 0 <= a < 8 and 0 <= b < 8 and board[a][b] != ".":
                n -= 1
                nxt.append((a,b))
                board[a][b] = "."
        if not q:
            q, nxt = nxt, q


for i in range(test):
    n = int(input())
    board = [["X"]*8 for _ in range(8)]
    bfs((0,0), n-1, board)
    # print(board)
    board[0][0] = "O"
    for i in range(8):
        print("".join(board[i]))
