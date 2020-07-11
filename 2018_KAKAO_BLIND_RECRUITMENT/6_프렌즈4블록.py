from collections import*
def solution(n, m, board):
    a=[[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i].append(board[i][j])
    ans=0
    while 1:
        flag = True
        erase=[[0]*m for _ in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                if a[i][j] == a[i+1][j] == a[i][j+1] == a[i+1][j+1]:
                    if a[i][j]=='#': continue
                    erase[i][j] = erase[i+1][j] = erase[i][j+1] = erase[i+1][j+1] = 1
                    flag = False
        if flag: return ans
        for i in range(n):
            for j in range(m):
                if erase[i][j]: 
                    a[i][j]='#'
                    ans+=1
        #중력
        for i in range(m):
            q=deque()
            for j in range(n):
                if a[j][i]=='#':
                    continue
                q.append(a[j][i])
            temp = n-len(q)
            for j in range(n):
                if j >= temp:
                    a[j][i] = q.popleft()
                else:
                    a[j][i] = '#'
