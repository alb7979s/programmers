def solution(N, stages):
    ans = []
    cnt = [0]*(N+2)
    for s in stages:
        cnt[s]+=1
    player=len(stages)
    for i in range(1, N+1):
        if player==0: ans.append((0, i))
        else: ans.append((cnt[i]/player, i))
        player-=cnt[i]
    ans = sorted(sorted(ans, key = lambda x: x[1]), key = lambda x: x[0], reverse=True)
    res=[]
    for x, i in ans:
        res.append(i)
    return res
