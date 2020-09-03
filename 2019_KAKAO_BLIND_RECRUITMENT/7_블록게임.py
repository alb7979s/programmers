a=[]
def check(x, y):
    for i in range(x):
        if a[i][y]: return False
    return True

def find(x, y, h, w):
    global a
    empty = 0
    block = -1
    for i in range(x, x+h):
        for j in range(y, y+w):
            if not a[i][j]:
                if not check(i, j):
                    return False
                empty += 1
                if empty > 2: return False
            else:
                if block != -1 and a[i][j] != block: return False
                block = a[i][j]
    for i in range(x, x+h):
        for j in range(y, y+w):
            a[i][j] = 0
    return True

def solution(board):
    global a
    a=[x[:] for x in board]
    n=len(board)
    ans=0
    while 1:
        cnt=0
        for i in range(n):
            for j in range(n):
                #2*3
                if i<= n-2 and j<=n-3 and find(i, j, 2, 3):
                    cnt += 1
                if i<=n-3 and j<=n-2 and find(i, j, 3, 2):
                    cnt += 1
        ans += cnt
        if not cnt: break
    return ans
