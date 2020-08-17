from sys import*
setrecursionlimit(10**6)
def div(x):
    f = -1 if x[0]=='(' else 1
    for i in range(1, len(x)):
        if x[i]==')': f += 1
        else: f -= 1
        if not f: return x[:i+1], x[i+1:]
    return x, ''
def isGood(x):
    f = 0
    for i in range(len(x)):
        if x[i]=='(': f+=1
        else: f-=1
        if f < 0: return False
    return True
def solve(w):
    if not w: return w
    ans=''
    u, v = div(w)
    print(u, v)
    if isGood(u): 
        ans += u + solve(v)
    else:
        temp = '('
        temp += solve(v)
        temp += ')'
        for i in range(1, len(u)-1):
            if u[i]==')': temp+='('
            else: temp+=')'
        ans += temp
    return ans
def solution(p):
    return solve(p)
