import re
def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(nums):
        numbers = re.sub(num, str(i), numbers)
    return int(numbers)