def solution(new_id):
    id_rule = 'abcdefghijklmnopqrstuvwxyz0123456789.-_'
    new_id = new_id.lower()   #1단계
    temp = ''
    for i in range(len(new_id)):    #2단계
        if new_id[i] in id_rule: temp += (new_id[i])
    new_id, temp = temp, ''
    for i in range(len(new_id)):    #3단계
        if new_id[i] == '.':
            if temp and temp[-1]=='.': continue
        temp += new_id[i]
    #4단계
    if temp and temp[0] == '.': temp = temp[1:]
    if temp and temp[-1] == '.': temp = temp[:-1]
    #5단계
    if len(temp) == 0: temp = 'a'
    new_id, temp = temp, ''
    #6단계
    if len(new_id) >= 16:
        temp = new_id[:15] if new_id[14] != '.' else new_id[:14]
    else:
        temp = new_id
    #7단계
    if len(temp) <= 2:
        temp += (temp[-1])*(3-len(temp))
    return temp

print(solution("=.="))
