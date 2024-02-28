def solution(n, lost, reserve):
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))
    
    answer = n - len(_lost)
    
    for num in _lost:
        if num-1 in _reserve:
            answer += 1
            _reserve.remove(num-1)
            continue

        elif num+1 in _reserve:
            answer += 1
            _reserve.remove(num+1)

    return answer