#O(N)어케하누
from sys import*
from collections import*
input=lambda:stdin.readline.strip()
setrecursionlimit(10**6)
def check(m, stones, k):
    cnt = 0
    for stone in stones:
        if stone <= m:
            cnt += 1
            if cnt >= k: return 0
        else:
            cnt = 0
    return 1
def solution(stones, k):
    #사람 지나간 횟수임
    s, e = 1, 1e18
    while s<=e:
        m = (s+e)//2
        if check(m, stones, k):    #되면 ++
            s = m+1
        else:
            e = m-1
    return s
