solution = lambda *x:sum(x)

"""
[note]
- 람다 -> 익명함수
- *x -> 인자로 받는 여러 개의 값을 하나의 객체(튜플)로 packing
  (※packing : *매개변수, unpacking : **인자) 
  [참고] https://wikidocs.net/22801

-> 기존 풀이
    def solution(num1, num2):
        answer = num1 + num2
        return answer
"""
