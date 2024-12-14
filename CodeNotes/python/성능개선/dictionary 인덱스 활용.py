"""
[Index]
- .index() : 리스트의 크기가 클 경우, 검색 시간이 길어짐 => 성능저하
- dictionary, set 이용으로 검색속도 향상
--->  dictionary는 hash값을 가진 트리구조로 Key값을 저장하여 속도가 빠름
"""

# 프로그래머스 - 달리기 경주 문제
def solution(players, callings):
    player_dic={key: i for i, key in enumerate(players)}  # *딕셔너리로 index값 지정
    for i in callings:
        idx=player_dic[i]
        player_dic[i]-=1
        player_dic[players[idx-1]]+=1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    answer = players
    return answer
