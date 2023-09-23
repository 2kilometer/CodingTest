import re
def solution(s):
    num_dict = ["zero", "one", "two", "three", "four", "five", 
                 "six", "seven", "eight", "nine"]
    for i in range(len(num_dict)):
        s = s.replace(num_dict[i], str(i))
    return int(s)