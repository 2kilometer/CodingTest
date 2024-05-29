from collections import deque
def solution(bandage, health, attacks):
    rcvr_time, rcvr_heal, rcvr_bonus = bandage
    now = 0

    for i, (time, attack) in enumerate(attacks):
        if i == 0:
            now = health - attack
            if now <= 0:
                return -1
        else:
            time_gap = time - attacks[i-1][0] - 1
            rcvr = time_gap * rcvr_heal + (time_gap // rcvr_time) * rcvr_bonus
            now = min(health, now+rcvr)
            now -= attack
            if now <= 0:
                return -1
    
    return now
