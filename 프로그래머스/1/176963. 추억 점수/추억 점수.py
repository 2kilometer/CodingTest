def solution(name, yearning, photo):
    def cal_yearning(names):
        return sum(yearning[name.index(n)] for n in names if n in name)
    return [cal_yearning(p) for p in photo]