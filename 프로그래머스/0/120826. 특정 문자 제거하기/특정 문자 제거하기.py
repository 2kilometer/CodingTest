# 메모리: 10.1 MB, 시간: 0.00 ms
def solution(my_string, letter):
    return my_string.replace(letter, '')

# 메모리: 10.2 MB, 시간: 0.01 ms
def solution(my_string, letter):
    return ''.join(str for str in my_string if str != letter)
