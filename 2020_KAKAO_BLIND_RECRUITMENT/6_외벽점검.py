from itertools import*
def solution(n, weak, dist):
    lw = len(weak)
    ld = len(dist)
    for i in range(lw):
        weak.append(weak[i]+n)
    ans = ld+1
    for i in range(lw):
        ws = [weak[x] for x in range(i, i+lw)]
        for d in permutations(dist, ld):
            posd, cnt = 0, 1
            covered = ws[0] + d[0]
            for j in range(lw):
                if covered < ws[j]:
                    cnt+=1
                    if cnt > ld: break
                    posd+=1
                    covered = ws[j] + d[posd]
            ans = min(ans, cnt)
    return -1 if ans > ld else ans
