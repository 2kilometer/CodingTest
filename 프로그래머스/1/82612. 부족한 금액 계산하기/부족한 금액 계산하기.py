def solution(price, money, count):
    answer = money - (price * sum(range(1,count+1)))
    if answer<0 : answer = abs(answer)
    else : answer = 0
    return answer