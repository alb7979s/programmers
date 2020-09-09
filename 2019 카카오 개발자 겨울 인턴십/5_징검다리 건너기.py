#얘도 반례있음.. 오답 정리 때 반례 찾기
#sliding windows
from sys import*
from heapq import*
input=lambda:stdin.readline().strip()
def solution(stones, k):
    pq = []
    cnt = {}
    for i in range(k+1):
        heappush(pq, -stones[i])    #MAX heap
        cnt[stones[i]] = 1
    ans = -pq[0]
    removeSet = set()
    for i in range(k+1, len(stones)):
        # print(pq)
        removeSet.add(stones[i-k])
        if stones[i] not in cnt:
            cnt[stones[i]] = 1
        else:cnt[stones[i]] += 1
        while len(pq)>=k and -pq[0] in removeSet:
            x = -heappop(pq)
            cnt[x] -= 1
            if not cnt[x]:
                removeSet.remove(x)
        heappush(pq, -stones[i])
        ans = min(ans, -pq[0])
    return ans
solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
