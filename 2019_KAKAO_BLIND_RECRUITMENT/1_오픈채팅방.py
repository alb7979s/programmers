def solution(record):
    dic={}
    ans=[]
    for string in record:
        a=string.split()
        if len(a)>=3:
            state, key, value = a[0], a[1], a[2]
        else:
            state, key = a[0], a[1]
        if string[0] == 'E':
            dic[key] = value
        elif string[0] == 'C':
            dic[key] = value
    for string in record:
        a=string.split()
        if len(a)>=3:
            state, key, value = a[0], a[1], a[2]
        else:
            state, key = a[0], a[1]
        if string[0] == 'E':
            ans.append("{}님이 들어왔습니다.".format(dic[key]))
        elif string[0] == 'L':
            ans.append("{}님이 나갔습니다.".format(dic[key]))
    
    return ans
