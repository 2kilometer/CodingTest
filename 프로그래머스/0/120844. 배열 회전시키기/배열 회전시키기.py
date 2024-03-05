def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
    elif direction == 'left':
        return numbers[1:] + [numbers[0]]