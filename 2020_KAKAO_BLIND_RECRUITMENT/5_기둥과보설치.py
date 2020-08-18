res = set()
def check():
    for x, y, a in res:
        if a:
            if (x, y - 1, 0) in res or (x + 1, y - 1, 0) in res or ((x - 1, y, 1) in res and (x + 1, y, 1) in res):
                continue
            else:
                return 0
        else:
            if y==0 or (x-1, y, 1) in res or (x, y, 1) in res or (x, y-1, 0) in res:
                continue
            else:
                return 0
    return 1
def solution(n, build_frame):
    global res
    for x, y, a, b in build_frame:
        if b:
            res.add((x, y, a))
            if not check(): res.remove((x, y, a))
        else:
            res.remove((x, y, a))
            if not check(): res.add((x, y, a))
    res = [list(x) for x in res]
    return sorted(res)
