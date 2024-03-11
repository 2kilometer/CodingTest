def solution(array, n):
    answer = min(array)
    for num in array:
        if abs(n - num) < abs(n - answer):
            answer = num
        elif abs(n - num) == abs(n - answer):
            answer = min(num, answer)
    return answer