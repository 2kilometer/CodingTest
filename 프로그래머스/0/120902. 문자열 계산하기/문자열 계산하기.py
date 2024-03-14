def solution(my_string):
    answer = 0
    mark = '+'
    for v in my_string.split(' '):
        if v.isdigit():
            if mark == '+':
                answer += int(v)
            else: 
                answer -= int(v)
        else:
            mark = v
    return answer