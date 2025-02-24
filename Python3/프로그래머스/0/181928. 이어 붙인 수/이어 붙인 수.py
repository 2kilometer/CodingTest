def solution(num_list):
    odd_num = ""
    even_num = ""
    for num in num_list:
        if num % 2 == 0:
            even_num += str(num)
        else:
            odd_num += str(num)     
    return int(odd_num) + int(even_num)