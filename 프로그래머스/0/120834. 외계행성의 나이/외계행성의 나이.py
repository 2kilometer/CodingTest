def solution(age):
    return ''.join(chr(97+int(n)) for n in str(age))