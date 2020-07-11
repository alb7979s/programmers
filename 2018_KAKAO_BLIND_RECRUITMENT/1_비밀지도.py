def solution(n, arr1, arr2):
    answer=[]
    for i in range(n):
        ans=(arr1[i] | arr2[i])
        temp=''
        for i in range(n):
            if ans & (1<<i):temp+='#'
            else: temp+=' '
        answer.append(temp[::-1])
    return answer
