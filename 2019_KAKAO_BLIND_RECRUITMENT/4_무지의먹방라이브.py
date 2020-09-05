#애증의 효율성 문제..
from heapq import*
def solution(food_times, k):
    pq=[]
    lf=len(food_times)
    for i in range(lf):
        heappush(pq, (food_times[i], i+1))
    eated, cnt = 0, 0
    while pq:
        temp = (pq[0][0] - eated) * len(pq)
        if temp <= k:
            k -= temp
            eated = pq[0][0]
            while pq:
                if pq[0][0] > eated: break
                heappop(pq)
        else:
            temp = []
            while pq:
                time, idx = heappop(pq)
                temp.append((idx, time))
            temp.sort()
            return temp[k%len(temp)][0]
    return -1
