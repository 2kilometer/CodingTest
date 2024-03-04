def solution(rsp):
    win = {'0':'5', '2':'0', '5':'2'}
    return ''.join(win[v] for v in rsp)