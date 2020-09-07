from heapq import*
dd=[(-1,0),(0,1),(1,0),(0,-1)]  #URDL
def solution(board):
    n = len(board)
    INF = int(1e9)
    dist=[[[INF]*4 for _ in range(n)]for _ in range(n)]
    for i in range(4):dist[0][0][i] = 0
    pq = []
    heappush(pq, (0, 0, 0, 1))
    heappush(pq, (0, 0, 0, 2))
    while pq:
        cost, x, y, d = heappop(pq)
        for i in range(4):
            dx, dy = dd[i]
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or board[nx][ny]: continue
            c = 100 if d==i else 600        #같은 방향 100, 꺾으면 600
            nc = cost + c
            if dist[nx][ny][i] > nc:
                dist[nx][ny][i] = nc
                heappush(pq, (nc, nx, ny, i))
    return min(dist[n-1][n-1])
solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
