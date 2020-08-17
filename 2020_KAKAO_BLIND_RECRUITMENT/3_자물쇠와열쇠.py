n,m=0,0
key, lock = [], []
def turn(key):
    temp=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = key[n-j-1][i]
    key = [x[:]for x in temp]
    return key
def solve(lockCnt):
    #make keymap
    SIZE = m*2 + n - 2
    keymap = [[0]*SIZE for _ in range(SIZE)]
    for i in range(n):
        for j in range(n):
            keymap[i+m-1][j+m-1] = key[i][j]
    #들어 맞는 곳 있는지 확인
    for i in range(m+n-1):
        for j in range(m+n-1):
            #자물쇠 확인
            cnt=0
            for k in range(m):
                for l in range(m):
                    if keymap[i+k][j+l] and not lock[k][l]: cnt+=1
                    elif keymap[i+k][j+l] and lock[k][l]:cnt=1e9
            if cnt==lockCnt: return True
    return False                    
def solution(KEY, LOCK):
    global key, lock, n, m
    key = [x[:]for x in KEY]
    lock = [x[:]for x in LOCK]
    n = len(key)
    m = len(lock)
    lockCnt = 0
    for i in range(m):
        for j in range(m):
            if not lock[i][j]:lockCnt+=1
    for i in range(4):
        if i: key = turn(key)
        if solve(lockCnt): return True
    return False
