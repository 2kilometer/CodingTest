def solution(my_string):
    answer = []
    for v in my_string:
        if v not in answer:
            answer.append(v)
    return ''.join(answer)