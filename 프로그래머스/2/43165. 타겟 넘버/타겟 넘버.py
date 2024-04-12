def solution(numbers, target):
    answer =[[numbers[0]],[-numbers[0]]]
    for num in numbers[1:]:
        temp = []
        for i in range(len(answer)):
            temp += [answer[i] + [num]]
            temp += [answer[i] + [-num]]
        answer = temp
    
    return sum(1 for a in answer if sum(a) == target)