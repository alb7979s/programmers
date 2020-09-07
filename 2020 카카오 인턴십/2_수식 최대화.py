from collections import*
from itertools import*
def cal(x, o, y):
    if o=='+': return x+y
    if o=='-': return x-y
    if o=='*': return x*y
def solution(expression):
    temp=''
    exp=deque()
    op='+-*'
    for i in range(len(expression)):
        if expression[i] in op:
            exp.append(int(temp))
            temp=''
            exp.append(expression[i])
        else:
            temp+=expression[i]
    exp.append(int(temp))
    ans=0
    for p in permutations([0,1,2], 3):
        tq = deque()
        for _ in range(len(exp)):
            tq.append(exp[_])
        for curr in p:
            resq=deque()
            while tq:
                x = tq.popleft()
                if x != op[curr]:
                    resq.append(x)
                else:
                    resq.append(cal(resq.pop(), x, tq.popleft()))
            for k in range(len(resq)):
                tq.append(resq[k])
        ans=max(ans, abs(resq[0]))
    print(ans)
    return ans
solution("100-200*300*100")
