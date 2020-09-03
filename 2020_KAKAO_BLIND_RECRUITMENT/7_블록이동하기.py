from collections import*
dd=[(-1, 0), (0, 1), (1, 0), (0, -1)]
def solution(board):
    ans = 0
    n=len(board)
    visit={}
    visit[0, 0, 0, 1] = 0
    q=deque()
    q.append((0, 0, 0, 1, 0))  #x1, y1, x2, y2, d(0이면 가로, 1이면 세로)
    while q:
        x1, y1, x2, y2, d = q.popleft()
        if (x1 == n-1 and y1 == n-1) or (x2 == n-1 and y2 == n-1): return visit[x1, y1, x2, y2]
        #그냥 이동
        for dx, dy in dd:
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if nx1<0 or ny1<0 or nx2<0 or ny2<0 or nx1>n-1 or ny1>n-1 or nx2>n-1 or ny2>n-1 or board[nx1][ny1] or board[nx2][ny2]: continue
            if (nx1, ny1, nx2, ny2) not in visit:
                visit[nx1, ny1, nx2, ny2] = visit[x1, y1, x2, y2] + 1
                q.append((nx1, ny1, nx2, ny2, d))
        #회전
        if not d:       #가로면
            for dx in [1, -1]:
                if 0<= x1+dx < n and not board[x1+dx][y1] and not board[x2+dx][y2]:
                    if (x2+dx, y2, x2, y2) not in visit:
                        visit[x2+dx, y2, x2, y2] = visit[x1, y1, x2, y2] + 1
                        q.append((x2+dx, y2, x2, y2, not d))
                    if (x1, y1, x1+dx, y1) not in visit:
                        visit[x1, y1, x1+dx, y1] = visit[x1, y1, x2, y2] + 1
                        q.append((x1, y1, x1+dx, y1, not d))
        else:
            for dy in [1, -1]:
                if 0<= y1+dy < n and not board[x1][y1+dy] and not board[x2][y2+dy]:
                    if (x1, y1, x1, y1+dy) not in visit:
                        visit[x1, y1, x1, y1+dy] = visit[x1, y1, x2, y2] + 1
                        q.append((x1, y1, x1, y1+dy, not d))
                    if (x2, y2+dy, x2, y2) not in visit:
                        visit[x2, y2+dy, x2, y2] = visit[x1, y1, x2, y2] + 1
                        q.append((x2, y2+dy, x2, y2, not d))
