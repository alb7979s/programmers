def solution(s):
    if len(s)==1: return 1
    answer = 1e9
    for l in range(1, len(s)//2+1):
        prev = s[:l]
        cnt=1
        res=0
        j=l
        while 1:
            j += l
            if j > len(s):
                if cnt>=2: res+=len(str(cnt))+l
                else: res += l
                res += len(s)-(j-l)
                break
            curr = s[j-l:j]
            if curr == prev:
                cnt += 1
            else:
                if cnt>=2:res += len(str(cnt))+l
                else: res += l
                cnt = 1
            prev = curr
        answer = min(answer, res)
    return answer
