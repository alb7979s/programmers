def solution(numbers, hand):
    ans = ''
    lPick = [1,4,7]
    rPick = [3,6,9]
    mPick = [2,5,8,0]
    l = (3, 0)
    r = (3, 2)
    for num in numbers:
        if num in lPick:
            ans += 'L'
            l = (lPick.index(num), 0)
        elif num in rPick:
            ans += 'R'
            r = (rPick.index(num), 2)
        else:
            mx, my = mPick.index(num), 1
            ld = abs(l[0]-mx) + abs(l[1]-my)
            rd = abs(r[0]-mx) + abs(r[1]-my)
            if ld > rd:
                ans += 'R'
                r = (mx, my)
            elif ld < rd:
                ans += 'L'
                l = (mx, my)
            else:
                if hand=='left':
                    ans+='L'
                    l = (mx, my)
                else:
                    ans+='R'
                    r = (mx, my)
    return ans
