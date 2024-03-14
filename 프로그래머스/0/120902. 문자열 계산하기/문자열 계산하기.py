def solution(my_string):
    return sum(int(v) for v in my_string.replace(' - ', ' + -').split(' + '))