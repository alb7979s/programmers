def AToI(A):
    return ord(A) % 65
def solution(skill, skill_trees):
    answer=0
    idx = [0] * 26
    j=1
    for i in range(len(skill)):
        idx[AToI(skill[i])] = j
        j+=1
    end = len(skill)
    for string in skill_trees:
        j=1; flag = True
        for i in range(len(string)):
            if idx[AToI(string[i])] > j:
                flag = False
                break
            elif idx[AToI(string[i])] == j:
                j+=1
        if flag: answer+=1
    return answer
