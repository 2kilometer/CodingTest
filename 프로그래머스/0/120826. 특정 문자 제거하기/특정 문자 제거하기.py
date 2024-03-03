def solution(my_string, letter):
    return ''.join(str for str in my_string if str != letter)