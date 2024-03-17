# 누적 계산 : reduce(집계 함수, 순회 가능한 데이터[, 초기값])
reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1

"""
[프로그래머스 옷 조합 문제]
- 초기값 안넘기면 lambda를 최초로 계산할 때 x에 iterable[0] 이 들어감
  -> 해당 문제에선 초기값 = 1 을 입력해야 함
https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""
