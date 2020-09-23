from collections import*
def add(x1, x2, y1, y2, prev):
    global q, visit
    if (x1, x2, y1, y2) not in visit:
        visit[x1, x2, y1, y2] = prev+1
        q.append((x1, x2, y1, y2))
def solution(board):
    global q, visit
    visit={}
    q=deque()
    visit[0,0,0,1] = 0
    q.append((0,0,0,1))
    n=len(board)
    while q:
        x1, y1, x2, y2 = q.popleft()
        if (x1==n-1 and y1==n-1) or (x2==n-1 and y2==n-1): return visit[x1, y1, x2, y2]
        #4방향 이동
        prev = visit[x1, y1, x2, y2]
        for dx, dy in [(0,-1), (0,1), (1,0), (-1,0)]:
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if nx1<0 or nx2<0 or ny1<0 or ny2<0 or nx1>n-1 or nx2>n-1 or ny1>n-1 or ny2>n-1 or board[nx1][ny1] or board[nx2][ny2]: continue
            add(nx1, ny1, nx2, ny2, prev)
        #회전!
        for d in [1, -1]:
            if x1==x2: #가로 방향
                nx = x1+d
                if nx<0 or nx>n-1 or board[nx][y1] or board[nx][y2]: continue
                add(nx, y1, x1, y1, prev)
                add(nx, y2, x2, y2, prev)
            if y1==y2:
                ny = y1+d
                if ny<0 or ny>n-1 or board[x1][ny] or board[x2][ny]: continue
                add(x1, ny, x1, y1, prev)
                add(x2, ny, x2, y2, prev)
    print(visit)
    return -1
print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
