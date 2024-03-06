import re
def solution(my_string):
    return re.sub("(a|e|i|o|u)", "", my_string)