#범위 설정 같은거 할때 막 하지말고 차분히 차근차근 예제 그려가는게 더 빠
def solution(lines):
    info=[]
    for line in lines:
        day, hour, processing = line.split()
        hour = int(hour[:2])*1000*60*60 + int(hour[3:5])*1000*60 + int(hour[6:8])*1000 + int(hour[9:])
        if '.' in processing:
            dot=processing.index('.')
            processing = int(processing[:dot])*1000 + int(processing[dot+1:-1])
        else:
            processing = int(processing[:-1])*1000
        info.append((hour-processing+1, hour))
    ans=0
    temp=999
    for i in range(len(info)):
        s, e = info[i]
        for k in range(2):
            s_cnt, e_cnt = 1, 1
            for j in range(len(info)):
                cs, ce = info[j]
                if i==j: continue
                if k==0:    #앞의 1초
                    if (cs <= s <= ce) or (s-temp <= cs <= s) or (s-temp <= ce <= s):
                        s_cnt+=1
                    if (cs <= e <= ce) or (e-temp <= cs <= e) or (e-temp <= ce <= e):
                        e_cnt+=1
                elif k==1:
                    if (cs <= s <= ce) or (s <= cs <= s+temp) or (s <= ce <= s+temp):
                        s_cnt+=1
                    if (cs <= e <= ce) or (e <= cs <= e+temp) or (e <= ce <= e+temp):
                        e_cnt+=1
            ans = max(ans, s_cnt, e_cnt)
    return ans
