def solution(board, moves):
    answer = 0; st=[]
    for x in moves:
        x-=1
        for i in range(len(board)):
            if board[i][x]:
                if len(st)==0: st.append(board[i][x])
                else:
                    if st[-1] == board[i][x]:
                        st.pop()
                        answer+=2
                    else:
                        st.append(board[i][x])
                board[i][x]=0
                break
    return answer
