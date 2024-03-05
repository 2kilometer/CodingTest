def solution(numbers, direction):
    dir = {'right':(-1,0), 'left':(0,len(numbers)-1)}    
    move = numbers.pop(dir[direction][0])
    numbers.insert(dir[direction][1], move)
    
    return numbers