def solution(code):
    mode = 0
    ret = ""
    for i, v in enumerate(code):
        if v == "1":
            mode += 1
            continue
        if i%2 == mode%2:
            ret += v
    return ret if ret != "" else "EMPTY"