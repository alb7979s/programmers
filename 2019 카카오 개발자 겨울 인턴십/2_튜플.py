#문자열 처리 어찌해야할지 몰라서 하드코딩함.. 정규식 배워 놓으면 좋을듯
def solution(s):
    st = []
    res = []
    temp = ''
    for i in range(1, len(s)-1):
        if s[i] == '{':
            st.append('{')
        elif s[i] == '}':
            if st and st[-1] == '{':
                res.append(temp)
                temp = ''
                st.pop()
        else:
            temp+=s[i]
    visit = {}
    ans=[[]for _ in range(len(res))]
    temp = []
    for i in range(len(res)):
        res[i] = res[i].split(',')
        for j in range(len(res[i])):
            if not res[i][j]=='': ans[i].append(res[i][j])
    ans.sort(key = lambda x: len(x))
    res = []
    for a in ans:
        for x in a:
            if x not in visit:
                visit[x] = 1
                res.append(int(x))
    return res

solution(	"{{1,2,3},{2,1},{1,2,4,3},{2}}")
