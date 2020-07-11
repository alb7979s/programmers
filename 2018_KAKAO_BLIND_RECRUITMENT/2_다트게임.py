def solution(dart):
    num, bonus, option=[], [], []
    ans=0
    ten=False
    for i in range(len(dart)):
        if ten:
            ten=False
            continue
        if dart[i]=='1':
            if dart[i+1]=='0':
                num.append(10)
                ten=True
            else:
                num.append(1)
        elif '0' <= dart[i] <= '9':
            num.append(int(dart[i]))
        if dart[i]=='S' or dart[i]=='D' or dart[i]=='T':
            bonus.append(dart[i])
            if i+1 < len(dart) and (dart[i+1]=='#' or dart[i+1]=='*'):
                option.append(dart[i+1])
            else:
                option.append('!')
    prev=1e9
    print(num, bonus, option)
    for i in range(3):
        n, b, o = num[i], bonus[i], option[i]
        if b=='D': n **= 2
        elif b=='T': n **= 3
        if o=='#': n *= -1
        elif o=='*':
            if prev!=1e9:
                ans+=prev
            n*=2
        ans+=n
        prev=n
    return ans
