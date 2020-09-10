#이분탐색 :: O(nlogn)
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
####################################################
#슬라이딩 윈도우 + pq :: O(nlogn)?? 힙큐 삽입이 O(logn)이고 총 n개 하니까
from sys import*
from heapq import*
input=lambda:stdin.readline().strip()
setrecursionlimit(10**6)
def solution(stones, k):
    pq = []
    cnt = {}
    for i in range(k):
        if stones[i] not in cnt: cnt[stones[i]]=1
        else: cnt[stones[i]]+=1
        heappush(pq, -stones[i])
    res = -pq[0]
    for i in range(k, len(stones)):
        cnt[stones[i-k]]-=1
        # print(pq, cnt)
        while len(pq) >= k and not cnt[-pq[0]]:
            heappop(pq)
        heappush(pq, -stones[i])
        if stones[i] not in cnt: cnt[stones[i]]=1
        else: cnt[stones[i]]+=1
        res = min(res, -pq[0])
    # print(res)
    return res
solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)

'''
#징검다리 O(nlogn) 이분탐색
테스트 1 〉	통과 (317.23ms, 17.9MB)
테스트 2 〉	통과 (341.61ms, 17.9MB)
테스트 3 〉	통과 (373.17ms, 18MB)
테스트 4 〉	통과 (207.74ms, 17.9MB)
테스트 5 〉	통과 (197.68ms, 17.9MB)
테스트 6 〉	통과 (206.45ms, 17.9MB)
테스트 7 〉	통과 (499.18ms, 17.9MB)
테스트 8 〉	통과 (721.63ms, 17.9MB)
테스트 9 〉	통과 (548.06ms, 17.9MB)
테스트 10 〉	통과 (704.84ms, 17.9MB)
테스트 11 〉	통과 (515.49ms, 17.9MB)
테스트 12 〉	통과 (672.60ms, 17.9MB)
테스트 13 〉	통과 (414.92ms, 18MB)
테스트 14 〉	통과 (319.14ms, 17.9MB)

#pq, sliding window
테스트 1 〉	통과 (166.17ms, 38.9MB)
테스트 2 〉	통과 (172.98ms, 38.9MB)
테스트 3 〉	통과 (165.31ms, 29.7MB)
테스트 4 〉	통과 (254.95ms, 26.6MB)
테스트 5 〉	통과 (276.66ms, 26.7MB)
테스트 6 〉	통과 (249.63ms, 26.8MB)
테스트 7 〉	통과 (143.35ms, 38.9MB)
테스트 8 〉	통과 (119.74ms, 38.9MB)
테스트 9 〉	통과 (141.17ms, 38.8MB)
테스트 10 〉	통과 (126.77ms, 38.9MB)
테스트 11 〉	통과 (142.39ms, 29.7MB)
테스트 12 〉	통과 (137.85ms, 29.8MB)
테스트 13 〉	통과 (164.92ms, 34.7MB)
테스트 14 〉	통과 (150.72ms, 38.9MB)
'''
