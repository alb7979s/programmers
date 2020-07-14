from heapq import *

def solution(n, t, m, timetable):
    pq = []
    for x in timetable:
        h,mi = map(str, x.split(':'))
        v = int(h)*60 + int(mi)
        heappush(pq, (v))
    time = 540  #분으로 통일, 9시 출발
    ans=0
    for i in range(n):
        if i == n - 1:
            for j in range(m - 1):
                if pq:
                    heappop(pq)
            if pq:
                x = heappop(pq)
                if x <= time:
                    ans = x-1
                    break
            ans = time
        else:
            for j in range(m):
                if pq:
                    x = heappop(pq)
                    if x > time:
                        heappush(pq, x)
                        break
        time += t
    h = ans//60
    mi = ans%60
    res=''
    if h < 10:
        res+='0'
    res += str(h)+':'
    if mi < 10:
        res+='0'
    res+=str(mi)
    return res
