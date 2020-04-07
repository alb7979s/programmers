def solution(p, l):
    s, c = sorted(p, reverse=True), 0
    while 1:
        for i, prt in enumerate(p):
            t = s[c]
            if prt == t:            #중요도 제일 높으면
                c+=1                #다음으로
                if i == l: return c #그게 찾는거면 인쇄
