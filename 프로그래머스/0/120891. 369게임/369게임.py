import re
def solution(order):
    return len(re.findall("[369]", str(order)))