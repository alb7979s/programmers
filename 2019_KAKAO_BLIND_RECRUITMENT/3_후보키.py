def solution(relation):
    ans_list = []
    for i in range(1, 1 << len(relation[0])):   #1, 10, 11, 100, 101, 110, 111, ...
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += relation[j][k]
            tmp_set.add(tmp)
        if len(tmp_set) == len(relation):       #중복 없어서 개수 같으면
            not_duplicate = True
            for num in ans_list:                #이 전에 선택 했었나 확인
                if (num & i) == num:            #이 전에 선택 된거면 추가안함
                    not_duplicate = False
                    break
            if not_duplicate:
                ans_list.append(i)
    return len(ans_list)
