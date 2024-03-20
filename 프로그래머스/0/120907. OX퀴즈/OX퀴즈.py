def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split(" ")
        if q[1] == "+":
            if int(q[4]) == int(q[0]) + int(q[2]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(q[4]) == int(q[0]) - int(q[2]):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer