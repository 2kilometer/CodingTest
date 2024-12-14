# x의 약수 계산
answer = []
for i in range(1, int(x**0.5)+1):
    answer += [i, x//i]
