def solution(board, moves):
    n=len(board)
    cnt = 0
    st=[]
    for move in moves:
        move-=1
        for i in range(n):
            if board[i][move]:
                if st and st[-1] == board[i][move]:
                    cnt+=2
                    st.pop()
                else:
                    st.append(board[i][move])
                board[i][move] = 0
                break
    return cnt
